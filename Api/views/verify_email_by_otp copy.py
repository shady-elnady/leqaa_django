from django.conf import settings
from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    ValidationError as DRFValidationError,
)
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now
from django.db import DatabaseError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.throttling import AnonRateThrottle
from django.core.signing import TimestampSigner
import logging

from Api.exceptions import (
    SuccessResponse,
    ValidationException,
    DatabaseException,
    ServerException,
    NotFoundException,
    InvalidOTPException,
)
from Api.views.log_in import LoginThrottle
from App.messages import AuthMessages
from User.models import User

logger = logging.getLogger(__name__)


class VerifyEmailByOTPThrottle(AnonRateThrottle):
    scope = "verify_email_by_otp"

    def get_cache_key(self, request, view):
        # Throttle by IP and email (if available in token)
        if request.method == "GET" and "token" in request.query_params:
            try:
                token = request.query_params["token"]
                signer = TimestampSigner()
                unsigned_value = signer.unsign(token)
                user_id = unsigned_value.split("-")[1]
                return f"{self.scope}_{self.get_ident(request)}_{user_id}"
            except:
                # Fallback to IP-only throttling if token parsing fails
                return f"{self.scope}_{self.get_ident(request)}"
        return None


class VerifyEMailByOTPSerializer(ModelSerializer):
    """
    Serializer for email verification with OTP validation
    """

    email = EmailField(
        required=True, max_length=255, help_text="Registered email address"
    )
    otp = CharField(
        max_length=settings.OTP_CHARACTER_LENGTH,
        min_length=settings.OTP_CHARACTER_LENGTH,
        required=True,
        trim_whitespace=True,
        help_text="{}-digit verification code".format(
            settings.OTP_CHARACTER_LENGTH,
        ),
    )

    class Meta:
        model = User
        fields = ["email", "otp"]
        extra_kwargs = {
            "email": {"required": True},
            "otp": {"required": True},
        }

    def validate_email(self, value):
        """Validate email exists and is not already verified"""
        user = User.objects.filter(email=value).first()
        if not user:
            raise DRFValidationError(AuthMessages.USER_NOT_FOUND)
        if user.email_verified_at:
            raise DRFValidationError(AuthMessages.EMAIL_ALREADY_VERIFIED)
        return value


class VeifyEmailByOTPAPIView(GenericAPIView):
    """
    API endpoint for email verification with OTP
    Throttle: 5 attempts/hour per email
    """

    serializer_class = VerifyEMailByOTPSerializer
    permission_classes = [AllowAny]
    throttle_classes = [VerifyEmailByOTPThrottle]

    def throttled(self, request, wait):
        """Custom response when rate limit is exceeded"""
        data = {
            "message": "Too many verification attempts",
            "available_in": f"{wait} seconds",
            "detail": "Please wait before trying again or request a new verification email",
        }
        return Response(data, status=status.HTTP_429_TOO_MANY_REQUESTS)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)

            if not serializer.is_valid():
                logger.warning(
                    "Email verification validation failed",
                    extra={
                        "errors": serializer.errors,
                        "email": request.data.get("email"),
                        "attempt": self._get_throttle_attempts(request),
                    },
                )
                raise ValidationException(errors=serializer.errors)

            return self._verify_email(
                email=serializer.validated_data["email"],
                otp=serializer.validated_data["otp"],
            )

        except ValidationException:
            raise  # Re-raise explicitly handled exceptions
        except Exception as e:
            logger.critical(
                "Unexpected email verification error",
                exc_info=True,
                extra={
                    "email": request.data.get("email"),
                    "error": str(e),
                    "type": type(e).__name__,
                },
            )
            raise ServerException(message=AuthMessages.EMAIL_VERIFICATION_ERROR)

    def _verify_email(self, email: str, otp: str) -> Response:
        """Core verification logic with proper error handling"""
        try:
            user: "User" = self._get_user(email)
            self._verify_otp(user, otp)
            self._mark_as_verified(user)

            logger.info(
                "Email verification successful",
                extra={
                    "user_id": user.id,
                    "email": user.email,
                    "ip": self.request.META.get("REMOTE_ADDR"),
                },
            )

            return SuccessResponse.create(
                message=AuthMessages.EMAIL_VERIFICATION_SUCCESS,
                status_code=status.HTTP_200_OK,
            )

        except (NotFoundException, InvalidOTPException):
            raise  # Re-raise custom exceptions
        except DatabaseError as e:
            logger.error(
                "Database error during verification",
                exc_info=True,
                extra={"email": email, "error": str(e)},
            )
            raise DatabaseException(message=AuthMessages.DATABASE_ERROR)
        except Exception as e:
            logger.error(
                "Verification processing error",
                exc_info=True,
                extra={"email": email, "error": str(e)},
            )
            raise ServerException(message=AuthMessages.EMAIL_VERIFICATION_ERROR)

    def _get_user(self, email: str) -> "User":
        """Retrieve user with validation"""
        try:
            user: "User" = User.objects.filter(email__iexact=email).first()
            if not user:
                logger.warning(
                    "Verification attempt for non-existent user",
                    extra={
                        "email": email,
                        "attempt": self._get_throttle_attempts(self.request),
                    },
                )
                raise NotFoundException(message=AuthMessages.USER_NOT_FOUND)
            return user
        except ObjectDoesNotExist:
            raise NotFoundException(message=AuthMessages.USER_NOT_FOUND)

    def _verify_otp(self, user: "User", otp: str):
        """Verify OTP with time-based validation if implemented"""
        if user.otp != otp:
            logger.warning(
                "Invalid OTP attempt",
                extra={
                    "user_id": user.id,
                    "email": user.email,
                    "attempt": self._get_throttle_attempts(self.request),
                },
            )
            raise InvalidOTPException(message=AuthMessages.INVALID_OTP)

        # Optional: Add OTP expiration check
        # if user.otp_created_at < timezone.now() - timedelta(minutes=15):
        #     raise InvalidOTPException(message=AuthMessages.OTP_EXPIRED)

    def _mark_as_verified(self, user: "User"):
        """Mark email as verified and clear OTP"""
        try:
            user.email_verified_at = now()
            user.otp = None
            user.save()
            logger.debug("Email marked as verified", extra={"user_id": user.id})
        except DatabaseError as e:
            logger.error(
                "Failed to update verification status",
                exc_info=True,
                extra={"user_id": user.id, "error": str(e)},
            )
            raise DatabaseException(message=AuthMessages.DATABASE_ERROR)

    def _get_throttle_attempts(self, request) -> int:
        """Get current throttle attempt count"""
        throttle = LoginThrottle()
        throttle.request = request
        return throttle.get_throttle_attempts()
