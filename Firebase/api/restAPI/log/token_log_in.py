from rest_framework.serializers import ModelSerializer, CharField
from rest_framework.decorators import permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login
from rest_framework.authtoken.models import Token
from django.core.exceptions import ValidationError
from firebase_admin.auth import UserRecord
from django.utils.timezone import now
import logging

from Firebase.api.restAPI.throttle import FirebaseLogInByIdTokenThrottle
from Firebase.helpers import FirebaseAdminHelper
from App.messages import AuthMessages
from User.models import User
from Api.exceptions import (
    SuccessResponse,
    ValidationException,
    AuthenticationException,
    UnverifiedAccountException,
    NotFoundException,
    ServerException,
)

logger = logging.getLogger(__name__)

firebase_helper: "FirebaseAdminHelper" = FirebaseAdminHelper()


class FirebaseLogInByIdTokenSerializer(ModelSerializer):
    """
    Serializer for Firebase token authentication
    """

    id_token = CharField(
        max_length=2048,  # Firebase tokens can be quite long
        required=True,
        help_text="Firebase ID token for authentication",
    )

    class Meta:
        model = User
        fields = ["id_token"]
        extra_kwargs = {
            "id_token": {"required": True, "write_only": True},
        }


@permission_classes([AllowAny])
class FirebaseLogInByIdTokenAPIView(GenericAPIView):
    """
    API endpoint for authenticating users with Firebase ID tokens
    """

    serializer_class = FirebaseLogInByIdTokenSerializer
    throttle_classes = [FirebaseLogInByIdTokenThrottle]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            if not serializer.is_valid():
                logger.warning(
                    "Invalid Firebase token login attempt",
                    extra={"errors": serializer.errors},
                )
                raise ValidationException(errors=serializer.errors)

            return self._authenticate_with_firebase(
                id_token=serializer.validated_data["id_token"], request=request
            )

        except ValidationException:
            raise  # Re-raise explicitly caught validation exceptions
        except Exception as e:
            logger.critical(
                "Unexpected Firebase token login error",
                exc_info=True,
                extra={"error": str(e)},
            )
            raise ServerException(message=AuthMessages.LOGIN_ERROR)

    def _authenticate_with_firebase(self, id_token: str, request) -> Response:
        """
        Core authentication logic with Firebase token
        """

        try:
            # Verify Firebase token
            decoded_token = firebase_helper.verify_id_token(id_token)
            uid = decoded_token.get("uid")

            if not uid:
                logger.error("Firebase token missing UID")
                raise AuthenticationException(message=AuthMessages.INVALID_TOKEN)

            # Get or create user
            user = self._get_user_by_firebase_uid(uid)

            # Perform login
            auth_token = self._perform_login(user, request)

            logger.info(
                "Firebase token login successful",
                extra={
                    "user_id": user.id,
                    "firebase_uid": uid,
                    "ip": request.META.get("REMOTE_ADDR"),
                },
            )

            return SuccessResponse.create(
                data={
                    "token": auth_token.key,
                    "user": {"id": user.id, "firebase_uid": uid},
                },
                message=AuthMessages.LOGIN_SUCCESS,
                status_code=status.HTTP_200_OK,
            )

        except (AuthenticationException, UnverifiedAccountException, NotFoundException):
            raise  # Re-raise custom exceptions
        except Exception as e:
            logger.error(
                "Firebase authentication processing error",
                exc_info=True,
                extra={"firebase_uid": uid, "error": str(e)},
            )
            raise ServerException(message=AuthMessages.LOGIN_ERROR)

    def _get_fire_user_by_uid(self, uid: str) -> "UserRecord":
        try:
            return firebase_helper.get_user(uid)
        except Exception as e:
            logger.error(
                "Error retrieving user data from Firebase",
                exc_info=True,
                extra={"firebase_uid": uid, "error": str(e)},
            )
            raise ValidationError(str(e))

    def _get_user_by_firebase_uid(self, uid: str) -> User:
        """Retrieve user by Firebase UID with validation"""
        try:
            user = User.objects.filter(firebase_uid=uid).first()
            if not user:
                logger.warning(
                    "Firebase UID not found in system", extra={"firebase_uid": uid}
                )
                raise NotFoundException(message=AuthMessages.USER_NOT_FOUND)
        except User.DoesNotExist:
            logger.error("User not found in database", extra={"firebase_uid": uid})
            fire_user_data: "UserRecord" = self._get_fire_user_by_uid(uid)
            return User.objects.create_user(
                username=(
                    fire_user_data.display_name
                    if fire_user_data.display_name
                    else str(fire_user_data.email.split("@")[0])
                    .replace("_", " ")
                    .capitalize()
                ),
                email=fire_user_data.email,
                password=(
                    fire_user_data.password
                    if fire_user_data.password
                    else User.generate_password()
                ),
                firebase_uid=uid,
                email_verified_at=now(),
                is_active=True,
                mobile=(
                    fire_user_data.phone_number if fire_user_data.phone_number else None
                ),
            )
        except Exception as e:
            logger.error(
                "Error retrieving user data from Firebase",
                exc_info=True,
                extra={"firebase_uid": uid, "error": str(e)},
            )
            raise ValidationError(str(e))

        return user

    def _perform_login(self, user: User, request) -> Token:
        """Perform Django login and token creation"""
        try:
            # Create or get authentication token
            token, _created = Token.objects.get_or_create(user=user)

            # Activate user if not active
            if not user.is_active:
                user.is_active = True
                user.save()

            # Create session
            login(request, user)

            return token

        except Exception as e:
            logger.error(
                "Login processing failed",
                exc_info=True,
                extra={"user_id": user.id, "error": str(e)},
            )
            raise ServerException(message=AuthMessages.LOGIN_ERROR)
