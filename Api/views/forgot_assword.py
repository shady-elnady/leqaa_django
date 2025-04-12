from django.conf import settings
from django.urls import reverse
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import ValidationError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.serializers import (
    ValidationError as DRFValidationError,
    Serializer,
    EmailField,
)
import logging

from Api.exceptions import (
    SuccessResponse,
    ValidationException,
    DatabaseException,
    ServerException,
    NotFoundException,
)
from django.db import IntegrityError

from App.messages import AuthMessages
from App.helpers import send_my_email
from User.models import User

logger = logging.getLogger(__name__)


class EmailSerializer(Serializer):
    """
    Serializer for password reset email request.
    Validates email format and checks if user exists.
    """

    email = EmailField(
        required=True, max_length=255, help_text="Registered email address"
    )

    def validate_email(self, value):
        """Additional email validation"""
        if not User.objects.filter(email=value).exists():
            raise DRFValidationError(AuthMessages.USER_NOT_FOUND)
        return value


class ForgotPasswordAPIView(GenericAPIView):
    """
    API endpoint to request password reset link.
    Generates secure token and sends reset link to user's email.
    """

    serializer_class = EmailSerializer
    throttle_scope = "forgot_password"

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        user = User.objects.get(email=email)

        try:
            reset_link = self._generate_reset_link(request, user)
            self._send_reset_email(user, reset_link)

            logger.info(
                f'Password reset link sent to {email}, "reset_link": {reset_link}'
            )
            return SuccessResponse.create(
                data={"reset_link": reset_link},
                message=AuthMessages.PASSWORD_RESET_EMAIL_SENT,
                status_code=status.HTTP_200_OK,
            )

        except ValidationError as e:
            logger.warning(
                "Password reset validation failed",
                extra={
                    "error": str(e),
                    "email": request.data.get("email"),
                    "ip": self._get_client_ip(request),
                },
            )
            raise ValidationException(
                message=AuthMessages.VALIDATION_ERROR, detail=e.detail
            )

        except User.DoesNotExist:
            logger.warning(
                "Password reset attempt for non-existent user",
                extra={
                    "email": request.data.get("email"),
                    "ip": self._get_client_ip(request),
                },
            )
            raise NotFoundException(message=AuthMessages.USER_NOT_FOUND)

        except IntegrityError as e:
            logger.error(
                "Database error during password reset",
                extra={
                    "error": str(e),
                    "email": request.data.get("email"),
                    "ip": self._get_client_ip(request),
                },
                exc_info=True,
            )
            raise DatabaseException(
                message=AuthMessages.REGISTER_DUPLICATE,
                extra_data={"email": request.data.get("email")},
            )

        except Exception as e:
            logger.critical(
                "Unexpected error in password reset",
                extra={
                    "error": str(e),
                    "email": request.data.get("email"),
                    "ip": self._get_client_ip(request),
                },
                exc_info=True,
            )
            raise ServerException(message=AuthMessages.PASSWORD_RESET_ERROR)

    def _generate_reset_link(self, request, user):
        """Generate secure password reset link"""
        token = PasswordResetTokenGenerator().make_token(user)
        encoded_pk = user.encoded_uid()

        reset_path = reverse(
            "reset-password", kwargs={"encoded_pk": encoded_pk, "token": token}
        )

        protocol = "https" if request.is_secure() else "http"
        host = self._get_valid_host(request)

        return f"{protocol}://{host}{reset_path}"

    def _get_valid_host(self, request):
        """Get valid host from request or settings"""
        host = request.get_host().split(":")[0]  # Remove port if present
        if host in settings.ALLOWED_HOSTS:
            return request.get_host()
        return settings.ALLOWED_HOSTS[0] if settings.ALLOWED_HOSTS else "localhost:8000"

    def _send_reset_email(self, user, reset_link):
        """Send password reset email (implement your email logic here)"""
        # Implementation depends on your email service
        # Example: send_mail(), Celery task, etc.
        send_my_email(
            recipient_list=[user.email],
            subject="Password Reset",
            template_name="emails/password_reset.html",
            plain_message="Your password reset link: {reset_link}",
            context={"reset_link": reset_link},
        )
