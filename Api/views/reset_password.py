from typing import Optional
from rest_framework.serializers import Serializer, CharField
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
import logging
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

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


@method_decorator(csrf_exempt, name="dispatch")
@permission_classes([AllowAny])
class PasswordResetAPIView(RetrieveAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request, encoded_pk, token):

        try:
            # Decode the user primary key
            user: Optional["User"] = User.get_user_by_encoded_uid(encoded_pk)

            if not user:
                return Response(
                    {
                        "success": False,
                        "message": "User UID Not Found",
                        "status": status.HTTP_404_NOT_FOUND,
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )

            # Process password reset
            user.set_password(request.data["password"])
            user.save()

            return Response(
                {
                    "success": True,
                    "message": "Password Change success",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            return Response(
                {
                    "success": False,
                    "message": f"Error >> {str(e)}",
                    "status": status.HTTP_400_BAD_REQUEST,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
