from rest_framework.serializers import CharField, EmailField, ModelSerializer
from django.utils.translation import gettext_lazy as _
from rest_framework.decorators import permission_classes
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.utils.timezone import now
from rest_framework import status

from User.models import User


class EMailVerifySerializer(ModelSerializer):
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


@permission_classes([AllowAny])
class VeifyEmailByOTPAPIView(RetrieveAPIView):
    permission_classes = AllowAny
    serializer_class = EMailVerifySerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        otp = request.data.get("otp")

        user: User = User.objects.get(email=email)

        if user:
            if user.otp == otp:
                user.email_verified_at = now()
                user.save()
                return Response(
                    {
                        "success": True,
                        "message": _("E-Mail Verify Successfully. You Can Log IN now"),
                        "status": status.HTTP_202_ACCEPTED,
                    },
                    status=status.HTTP_202_ACCEPTED,
                )
            else:
                return Response(
                    {
                        "success": False,
                        "status": status.HTTP_400_BAD_REQUEST,
                        "message": _("OTP Not Correct.Try Again"),
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(
                {
                    "success": False,
                    "status": 404,
                    "message": _("Email not Found"),
                },
                status=status.HTTP_404_NOT_FOUND,
            )
