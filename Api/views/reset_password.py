from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.serializers import Serializer, CharField
from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import ValidationError
from django.utils import timezone
from rest_framework import status
from django.db import IntegrityError
import logging

from Api.exceptions import (
    ValidationException,
    DatabaseException,
    ServerException,
    SuccessResponse,
)
from App.messages import AuthMessages
from User.models import User

logger = logging.getLogger(__name__)


class ResetPasswordSerializer(Serializer):
    """
    Secure password reset validation with enhanced security checks.
    """

    password = CharField(
        write_only=True,
        min_length=8,
        max_length=128,
        style={"input_type": "password"},
        help_text="New password (min 8 characters)",
    )
    confirm_password = CharField(
        write_only=True,
        style={"input_type": "password"},
        help_text="Confirm new password",
    )

    def validate(self, data):
        """Comprehensive password and token validation"""
        try:
            self._validate_passwords_match(data)
            user = self._validate_reset_token()
            self._validate_password_complexity(data["password"])
            data["user"] = user
            return data
        except ValidationError as e:
            logger.warning(
                "Password reset validation failed",
                extra={
                    "error": str(e),
                    "validation_errors": e.detail if hasattr(e, "detail") else str(e),
                },
            )
            raise ValidationException(
                message=AuthMessages.VALIDATION_ERROR,
                detail=e.detail if hasattr(e, "detail") else {"error": str(e)},
            )

    def _validate_passwords_match(self, data):
        if data["password"] != data["confirm_password"]:
            raise ValidationError(AuthMessages.PASSWORDS_DO_NOT_MATCH)

    def _validate_reset_token(self):
        token = self.context["kwargs"]["token"]
        encoded_pk = self.context["kwargs"]["encoded_pk"]

        if not token or not encoded_pk:
            raise ValidationError(AuthMessages.INVALID_RESET_LINK)

        user = User.get_user_by_encoded_uid(encoded_pk)
        if not user:
            raise ValidationError(AuthMessages.USER_NOT_FOUND)

        if not PasswordResetTokenGenerator().check_token(user, token):
            raise ValidationError(AuthMessages.TOKEN_INVALID_OR_EXPIRED)

        return user

    def _validate_password_complexity(self, password):
        """Ensure password meets complexity requirements"""
        if len(password) < 8:
            raise ValidationError(AuthMessages.PASSWORD_TOO_SHORT)
        if not any(char.isdigit() for char in password):
            raise ValidationError(AuthMessages.PASSWORD_NO_NUMBER)
        if not any(char.isupper() for char in password):
            raise ValidationError(AuthMessages.PASSWORD_NO_UPPER)


class PasswordResetAPIView(GenericAPIView):
    """
    Secure password reset confirmation endpoint with comprehensive exception handling.
    """

    serializer_class = ResetPasswordSerializer
    throttle_scope = "password_reset"

    def patch(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(
                data=request.data, context={"kwargs": kwargs}
            )
            serializer.is_valid(raise_exception=True)

            user = serializer.validated_data["user"]
            password = serializer.validated_data["password"]

            self._perform_password_reset(user, password)

            logger.info(
                "Password reset successful",
                extra={
                    "user_id": user.id,
                    "email": user.email,
                    "action": "password_reset",
                    "ip": self._get_client_ip(request),
                },
            )

            return SuccessResponse.create(
                message=AuthMessages.RESET_PASSWORD_SUCCESS,
                status_code=status.HTTP_200_OK,
            )

        except ValidationException as e:  # noqa: F841
            # Already logged in serializer
            raise

        except IntegrityError as e:
            logger.error(
                "Database integrity error during password reset",
                exc_info=True,
                extra={
                    "user_id": user.id if "user" in locals() else None,
                    "error": str(e),
                    "ip": self._get_client_ip(request),
                },
            )
            raise DatabaseException(message=AuthMessages.DATABASE_ERROR, detail=str(e))

        except Exception as e:
            logger.critical(
                "Unexpected error during password reset",
                exc_info=True,
                extra={
                    "user_id": user.id if "user" in locals() else None,
                    "error": str(e),
                    "ip": self._get_client_ip(request),
                },
            )
            raise ServerException(
                message=AuthMessages.RESET_PASSWORD_FAILED, detail=str(e)
            )

    def _perform_password_reset(self, user, password):
        """Secure password update with session termination"""
        try:
            user.set_password(password)
            user.password_changed_at = timezone.now()
            user.save()

            # Terminate all existing sessions
            user.auth_token_set.all().delete()

            # Additional session cleanup if needed
            if hasattr(user, "session_set"):
                user.session_set.all().delete()

        except Exception as e:
            logger.error(
                "Failed to complete password reset",
                exc_info=True,
                extra={"user_id": user.id, "error": str(e)},
            )
            raise DatabaseException(message=AuthMessages.DATABASE_ERROR, detail=str(e))

    def _get_client_ip(self, request):
        """Extract client IP from request"""
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0]
        return request.META.get("REMOTE_ADDR")
