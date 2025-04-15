from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    EmailField,
)
from rest_framework.decorators import permission_classes
from rest_framework.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from rest_framework.generics import RetrieveAPIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework import status
import logging

from App.helpers import send_my_email
from User.models import User

logger = logging.getLogger(__name__)


class LogInSerializer(ModelSerializer):
    email = EmailField(
        required=True,
    )
    password = CharField(
        max_length=128,
        write_only=True,
        required=True,
        style={"input_type": "password"},
    )

    class Meta:
        model = User
        fields = [
            "email",
            "password",
        ]
        extra_kwargs = {
            "email": {
                "required": True,
            },
            "password": {
                "required": True,
                "write_only": True,
            },
        }


@method_decorator(csrf_exempt, name="dispatch")
@permission_classes([AllowAny])
class LogInAPIView(RetrieveAPIView):
    serializer_class = LogInSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            logger.warning(
                "Login validation failed",
                extra={
                    "errors": serializer.errors,
                    "email": request.data.get("email"),
                    "attempt": self._get_throttle_attempts(request),
                },
            )
            raise ValidationError(errors=serializer.errors)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        try:
            user: User = User.objects.filter(email=email).first()
            if user is None:
                return Response(
                    {
                        "success": False,
                        "message": "User Not Found",
                        "status": status.HTTP_400_BAD_REQUEST,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            elif (user is not None) and (not user.check_password(password)):
                return Response(
                    {
                        "success": False,
                        "message": "Password Wrong",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            else:
                if not user.email_verified_at:
                    try:
                        from Event.models import Event

                        send_my_email(
                            subject="Verify Your E-Mail",
                            plain_message=user.otp,
                            recipient_list=[user.email],
                            template_name=r"emails/wasla_verfiy_email.html",
                            context={
                                "events": Event.objects.all()[:2],
                                "otp": user.otp,
                                "verification_url": user.get_email_verification_url(
                                    request
                                ),
                                "our_facebook_account_ulr": "https://www.facebook.com/",
                                "our_twitter_account_ulr": "https://x.com/i/flow/login",
                                "our_instagram_account_ulr ": "https://www.instagram.com/accounts/login/?hl=en",
                                "our_linkedin_account_ulr  ": "https://www.linkedin.com/feed/",
                            },
                        )
                        return Response(
                            {
                                "success": False,
                                "message": "Please Verfy Your Account, Got to Your E-Mail",
                            },
                            status=status.HTTP_426_UPGRADE_REQUIRED,
                        )
                    except Exception as e:
                        logger.error(
                            f"Error sending verification email: {str(e)}",
                            extra={
                                "email": user.email,
                                "user_id": user.pk,
                            },
                        )
                        return Response(
                            {
                                "success": False,
                                "message": f"Error on sending verification email > {str(e)}",
                            },
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        )
                login(request, user=user)
                token, _created = Token.objects.get_or_create(user=user)
                if not user.is_active:
                    user.is_active = True
                    user.save()

                logger.info(
                    "Login successful",
                    extra={
                        "user_id": user.id,
                        "email": user.email,
                        "ip": request.META.get("REMOTE_ADDR"),
                    },
                )
                return Response(
                    {
                        "success": True,
                        "message": _("User logged successfully"),
                        "token": token.key,
                        "data": {
                            "User ID": user.encoded_uid,
                        },
                    },
                    status=status.HTTP_200_OK,
                )
        except Exception as e:
            return Response(
                {
                    "success": False,
                    "message": f"Error is {str(e)}, with type {str(e)}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request, *args, **kwargs):
        return Response(
            {
                "success": False,
                "message": "Method Not Allowed",
            },
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )
