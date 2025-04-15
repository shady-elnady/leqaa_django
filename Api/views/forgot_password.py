from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (
    Serializer,
    EmailField,
)
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
import logging
from Api.exceptions import (
    SuccessResponse,
    ValidationException,
    ServerException,
    NotFoundException,
)

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
            raise ValidationError(AuthMessages.USER_NOT_FOUND)
        return value


@method_decorator(csrf_exempt, name="dispatch")
@permission_classes([AllowAny])
class ForgotPasswordAPIView(GenericAPIView):
    """
    API endpoint to request password reset link.
    Generates secure token and sends reset link to user's email.
    """

    serializer_class = EmailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]

        try:
            user: "User" = User.objects.get(email=email)

            from Event.models import Event

            send_my_email(
                subject="Verify Your E-Mail",
                plain_message=user.change_otp,
                recipient_list=[user.email],
                template_name=r"emails/wasla_verfiy_email.html",
                context={
                    "events": Event.objects.all()[:2],
                    "otp": user.otp,
                    "verification_url": user.get_email_verification_url(request),
                    "our_facebook_account_ulr": "https://www.facebook.com/",
                    "our_twitter_account_ulr": "https://x.com/i/flow/login",
                    "our_instagram_account_ulr ": "https://www.instagram.com/accounts/login/?hl=en",
                    "our_linkedin_account_ulr  ": "https://www.linkedin.com/feed/",
                },
            )
            return SuccessResponse.create(
                message="OTP send to Your E-Mail",
                status_code=status.HTTP_200_OK,
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
