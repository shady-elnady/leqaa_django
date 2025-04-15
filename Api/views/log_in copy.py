from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer, CharField, EmailField
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.throttling import AnonRateThrottle
from django.contrib.auth import login
from django.utils import timezone
from django.db import DatabaseError
import logging

from Api.exceptions import (
    ValidationException,
    DatabaseException,
    ServerException,
    SuccessResponse,
    NotFoundException,
    AuthenticationException,
    UnverifiedAccountException,
)
from User.models import User
from App.messages import AuthMessages

logger = logging.getLogger(__name__)


class LoginThrottle(AnonRateThrottle):
    """Custom throttle for login endpoint (5 attempts/hour per email)"""

    scope = (
        "api_log_in"  # Matches the setting in REST_FRAMEWORK['DEFAULT_THROTTLE_RATES']
    )

    def get_cache_key(self, request, view):
        if request.method == "POST" and "email" in request.data:
            return self.cache_format % {
                "scope": self.scope,
                "ident": request.data["email"].lower().strip(),  # Normalized email
            }
        return None


class LogInSerializer(ModelSerializer):
    """Serializer for user login credentials"""

    email = EmailField(required=True, max_length=255)
    password = CharField(
        max_length=128,
        write_only=True,
        required=True,
        style={"input_type": "password"},
        trim_whitespace=False,
    )

    class Meta:
        model = User
        fields = ["email", "password"]
        extra_kwargs = {
            "email": {"required": True},
            "password": {"required": True, "write_only": True},
        }


@permission_classes([AllowAny])
class LogInAPIView(APIView):
    """
    Authenticates users and returns an auth token.
    Throttles: 5 attempts/hour per email (configured in settings)
    """

    serializer_class = LogInSerializer
    throttle_classes = [LoginThrottle]

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)

            if not serializer.is_valid():
                logger.warning(
                    "Login validation failed",
                    extra={
                        "errors": serializer.errors,
                        "email": request.data.get("email"),
                        "attempt": self._get_throttle_attempts(request),
                    },
                )
                raise ValidationException(errors=serializer.errors)

            return self._authenticate_user(
                email=serializer.validated_data["email"],
                password=serializer.validated_data["password"],
                request=request,
            )

        except UnverifiedAccountException as e:
            return Response(
                {
                    "success": False,
                    "message": e.detail["message"],
                    "verification_url": e.detail["extra"]["verification_url"],
                    "verified": False,
                },
                status=status.HTTP_403_FORBIDDEN,
            )
        except ValidationException:
            raise  # Re-raise as is
        except Exception as e:
            logger.critical(
                "Unexpected login error",
                exc_info=True,
                extra={
                    "email": request.data.get("email"),
                    "error": str(e),
                    "type": type(e).__name__,
                },
            )
            raise ServerException(message=AuthMessages.LOGIN_ERROR)

    def _authenticate_user(self, email: str, password: str, request) -> Response:
        """Core authentication logic with proper error handling"""
        try:
            user = self._get_user(email)
            self._validate_credentials(user, password, request)
            self._check_account_verification(user, request)
            token = self._get_or_update_token(user)
            self._activate_user_if_needed(user)
            self._create_session(request, user)

            logger.info(
                "Login successful",
                extra={
                    "user_id": user.id,
                    "email": user.email,
                    "ip": request.META.get("REMOTE_ADDR"),
                },
            )

            return SuccessResponse.create(
                data={
                    "token": token.key,
                    "user": {
                        "id": user.encoded_uid,
                        "email": user.email,
                        "is_active": user.is_active,
                    },
                },
                message=AuthMessages.LOGIN_SUCCESS,
                status_code=status.HTTP_200_OK,
            )
        except (NotFoundException, AuthenticationException, UnverifiedAccountException):
            raise
        except DatabaseError as e:
            logger.error(
                "Database error during authentication",
                exc_info=True,
                extra={"email": email, "error": str(e)},
            )
            raise DatabaseException(message=AuthMessages.DATABASE_ERROR)
        except Exception as e:
            logger.error(
                "Authentication processing error",
                exc_info=True,
                extra={"email": email, "error": str(e)},
            )
            raise ServerException(message=AuthMessages.LOGIN_ERROR)

    def _get_user(self, email: str) -> "User":
        """Retrieve user with validation"""
        user = User.objects.filter(email__iexact=email).first()
        if not user:
            logger.warning(
                "Login attempt for non-existent user",
                extra={"email": email},
            )
            raise NotFoundException(message=AuthMessages.USER_NOT_FOUND)
        return user

    def _validate_credentials(self, user: "User", password: str, request):
        """Verify user password"""
        if not user.check_password(password):
            logger.warning(
                "Invalid password attempt",
                extra={
                    "user_id": user.id,
                    "email": user.email,
                    "attempt": self._get_throttle_attempts(request),
                },
            )
            raise AuthenticationException(message=AuthMessages.PASSWORD_WRONG)

    def _check_account_verification(self, user: "User", request):
        """Check if account is verified"""
        if not user.email_verified_at:
            logger.warning(
                "Attempt to login with unverified account",
                extra={"user_id": user.id, "email": user.email},
            )
            verification_url = user.get_email_verification_url(request)
            raise UnverifiedAccountException(
                message=AuthMessages.VERIFY_ACCOUNT,
                extra_data={"verification_url": verification_url},
            )

    def _get_or_update_token(self, user: "User") -> Token:
        """Get or create auth token, updating timestamp if exists"""
        token, created = Token.objects.get_or_create(user=user)
        if not created:
            token.created = timezone.now()
            token.save()
            logger.debug("Updated existing auth token", extra={"user_id": user.id})
        return token

    def _activate_user_if_needed(self, user: "User"):
        """Activate user account if inactive"""
        if not user.is_active:
            user.is_active = True
            user.save()
            logger.info(
                "Activated previously inactive user", extra={"user_id": user.id}
            )

    def _create_session(self, request, user: "User"):
        """Create Django session if needed"""
        login(request, user)
        logger.debug("Created user session", extra={"user_id": user.id})

    def _get_throttle_attempts(self, request) -> int:
        """Get current throttle attempt count"""
        throttle = LoginThrottle()
        throttle.request = request  # Use the passed request parameter
        return throttle.num_requests  # More direct way to get attempts
