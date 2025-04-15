from django.conf import settings
from django.urls import reverse
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.serializers import (
    ModelSerializer,
    EmailField,
    CharField,
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
from User.models import User

logger = logging.getLogger(__name__)


class EMailOTPSerializer(ModelSerializer):
    email = EmailField(
        required=True,
    )
    otp = CharField(
        max_length=4,
        required=True,
    )

    class Meta:
        model = User
        fields = [
            "email",
            "otp",
        ]
        extra_kwargs = {
            "email": {
                "required": True,
            },
            "otp": {
                "required": True,
            },
        }


@method_decorator(csrf_exempt, name="dispatch")
@permission_classes([AllowAny])
class OTPResetPasswordAPIView(GenericAPIView):
    """
    API endpoint to request password reset link.
    Generates secure token and sends reset link to user's email.
    """

    serializer_class = EMailOTPSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        otp = serializer.validated_data["otp"]

        try:
            user: "User" = User.objects.get(email=email)
            if not user:
                return Response(
                    {
                        "success": False,
                        "message": "E-Mail Not Found",
                        "status": status.HTTP_400_BAD_REQUEST,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if user.otp != otp:
                return Response(
                    {
                        "success": False,
                        "message": "OTP Not Correct",
                        "status": status.HTTP_400_BAD_REQUEST,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            reset_link = self._generate_reset_link(request, user)

            logger.info(
                f'Password reset link sent to {email}, "reset_link": {reset_link}'
            )
            return SuccessResponse.create(
                data={
                    "reset_link": reset_link,
                },
                message=AuthMessages.PASSWORD_RESET_EMAIL_SENT,
                status_code=status.HTTP_200_OK,
            )

        except Exception as e:
            logger.critical(
                "Unexpected error in password reset",
                extra={
                    "error": str(e),
                    "email": request.data.get("email"),
                },
                exc_info=True,
            )
            raise ServerException(
                message=f"{AuthMessages.PASSWORD_RESET_ERROR}, Error > {str(e)}"
            )

    def _generate_reset_link(self, request, user: "User"):
        """Generate secure password reset link"""
        token = PasswordResetTokenGenerator().make_token(user)
        encoded_pk = user.encoded_uid

        return request.build_absolute_uri(
            reverse("Api:api_password_reset", args=[encoded_pk, token])
        )
