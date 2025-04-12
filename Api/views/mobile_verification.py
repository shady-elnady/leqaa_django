from datetime import timezone
from django.conf import settings
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import Serializer, CharField
from rest_framework.generics import GenericAPIView
from firebase_admin import auth, exceptions as firebase_exceptions
from django.db import DatabaseError, IntegrityError
from django.core.exceptions import ValidationError as DjangoValidationError
import logging

from Api.exceptions import (
    SuccessResponse,
    ValidationException,
    DatabaseException,
    ServerException,
    FirebaseException,
)
from Api.views.log_in import LoginThrottle
from App.messages import AuthMessages
from Firebase.helpers import FirebaseAdminHelper
from User.models import User

logger = logging.getLogger(__name__)


class MobileVerificationSerializer(Serializer):
    """
    Validates mobile verification request data
    """

    mobile = CharField(
        required=True,
        max_length=20,
        help_text="E.164 formatted phone number (+1234567890)",
    )
    firebase_id_token = CharField(
        required=True, help_text="Firebase ID token from phone authentication"
    )

    def validate_mobile(self, value):
        """Validate mobile number format"""
        if not value.startswith("+"):
            raise DjangoValidationError(AuthMessages.INVALID_MOBILE_FORMAT)
        return value.strip()


class MobileVerificationAPIView(GenericAPIView):
    """
    API endpoint for mobile number verification using Firebase Authentication

    Throttle: 5 attempts/hour per mobile number
    """

    serializer_class = MobileVerificationSerializer
    permission_classes = [AllowAny]  # AllowAny is default
    throttle_scope = "mobile_verification"

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)

            if not serializer.is_valid():
                logger.warning(
                    "Mobile verification validation failed",
                    extra={
                        "errors": serializer.errors,
                        "mobile": request.data.get("mobile"),
                        "attempt": self._get_throttle_attempts(request),
                    },
                )
                raise ValidationException(errors=serializer.errors)

            return self._verify_mobile(
                mobile=serializer.validated_data["mobile"],
                firebase_id_token=serializer.validated_data["firebase_id_token"],
            )

        except ValidationException:
            raise  # Re-raise explicitly handled exceptions
        except Exception as e:
            logger.critical(
                "Unexpected mobile verification error",
                exc_info=True,
                extra={
                    "mobile": request.data.get("mobile"),
                    "error": str(e),
                    "type": type(e).__name__,
                },
            )
            raise ServerException(message=AuthMessages.MOBILE_VERIFICATION_FAILED)

    def _verify_mobile(self, mobile: str, firebase_id_token: str) -> Response:
        """Core verification logic with proper error handling"""
        try:
            # Verify Firebase token first
            decoded_token = self._verify_firebase_token(firebase_id_token)
            firebase_uid = decoded_token["uid"]

            # Process user account
            user = self._get_or_create_user(mobile, firebase_uid)
            self._mark_mobile_verified(user)

            logger.info(
                "Mobile verification successful",
                extra={
                    "user_id": user.id,
                    "mobile": user.mobile,
                    "firebase_uid": user.firebase_uid,
                    "ip": self.request.META.get("REMOTE_ADDR"),
                },
            )

            return SuccessResponse.create(
                data={
                    "user_id": user.id,
                    "mobile_verified": True,
                    "firebase_uid": user.firebase_uid,
                },
                message=AuthMessages.MOBILE_VERIFICATION_SUCCESS,
                status_code=status.HTTP_200_OK,
            )

        except (FirebaseException, DatabaseException):
            raise  # Re-raise custom exceptions
        except Exception as e:
            logger.error(
                "Verification processing error",
                exc_info=True,
                extra={"mobile": mobile, "error": str(e)},
            )
            raise ServerException(message=AuthMessages.MOBILE_VERIFICATION_FAILED)

    def _verify_firebase_token(self, id_token: str) -> dict:
        """Verify Firebase ID token with proper error handling"""
        try:
            decoded_token = FirebaseAdminHelper().verify_id_token(
                id_token,
                check_revoked=True,
            )

            # Validate token audience
            if decoded_token["aud"] != settings.PYREBASE_CONFIG["projectId"]:
                logger.error(
                    "Invalid Firebase token audience",
                    extra={"audience": decoded_token["aud"]},
                )
                raise FirebaseException(
                    message=AuthMessages.FIREBASE_AUTH_ERROR,
                    status_code=status.HTTP_401_UNAUTHORIZED,
                )

            return decoded_token

        except firebase_exceptions.InvalidIdTokenError as e:
            logger.warning(
                "Invalid Firebase token", exc_info=True, extra={"error": str(e)}
            )
            raise FirebaseException(
                message=AuthMessages.INVALID_FIREBASE_TOKEN,
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        except firebase_exceptions.FirebaseError as e:
            logger.error(
                "Firebase authentication error", exc_info=True, extra={"error": str(e)}
            )
            raise FirebaseException(
                message=AuthMessages.FIREBASE_AUTH_ERROR,
                status_code=status.HTTP_502_BAD_GATEWAY,
            )

    def _get_or_create_user(self, mobile: str, firebase_uid: str) -> User:
        """Get or create user account with proper error handling"""
        try:
            # Try existing Firebase user first
            try:
                user: "User" = User.objects.get(firebase_uid=firebase_uid)
                if user.mobile != mobile:
                    user.mobile = mobile
                    user.save()
                return user
            except User.DoesNotExist:
                pass

            # Try existing mobile user
            user: "User" = User.objects.filter(mobile=mobile).first()
            if user:
                if user.firebase_uid and user.firebase_uid != firebase_uid:
                    logger.warning(
                        "Mobile number conflict",
                        extra={
                            "mobile": mobile,
                            "existing_firebase_uid": user.firebase_uid,
                            "new_firebase_uid": firebase_uid,
                        },
                    )
                    raise DatabaseException(
                        message=AuthMessages.MOBILE_NUMBER_CONFLICT,
                        status_code=status.HTTP_409_CONFLICT,
                    )
                user.firebase_uid = firebase_uid
                user.save()
                return user

            # Create new user
            return User.objects.create(
                mobile=mobile,
                firebase_uid=firebase_uid,
                is_active=True,
                mobile_verified_at=timezone.now(),
            )

        except IntegrityError as e:
            logger.error(
                "User creation integrity error",
                exc_info=True,
                extra={"mobile": mobile, "error": str(e)},
            )
            raise DatabaseException(
                message=AuthMessages.DATABASE_ERROR,
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            )
        except DatabaseError as e:
            logger.error(
                "Database operation failed",
                exc_info=True,
                extra={"mobile": mobile, "error": str(e)},
            )
            raise DatabaseException(
                message=AuthMessages.DATABASE_ERROR,
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

    def _mark_mobile_verified(self, user: "User"):
        """Mark mobile as verified with proper error handling"""
        try:
            user.mobile_verified_at = timezone.now()
            user.is_active = True
            user.save()

            # Revoke previous sessions for security
            try:
                auth.revoke_refresh_tokens(user.firebase_uid)
                logger.debug(
                    "Revoked previous Firebase sessions", extra={"user_id": user.id}
                )
            except firebase_exceptions.FirebaseError as e:
                logger.warning(
                    "Firebase session revocation failed",
                    extra={"user_id": user.id, "error": str(e)},
                )

        except DatabaseError as e:
            logger.error(
                "Failed to update verification status",
                exc_info=True,
                extra={"user_id": user.id, "error": str(e)},
            )
            raise DatabaseException(
                message=AuthMessages.DATABASE_ERROR,
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

    def _get_throttle_attempts(self, request) -> int:
        """Get current throttle attempt count"""
        throttle = LoginThrottle()
        throttle.request = request
        return throttle.get_throttle_attempts()
