from rest_framework.serializers import (
    Serializer,
    ModelSerializer,
    CharField,
    EmailField,
    ChoiceField,
    ValidationError,
)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import permission_classes
from django.utils.translation import gettext_lazy as _
from rest_framework.generics import RetrieveAPIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth import login
from rest_framework import status

from User.models import User
from User.utils.enums import USERS_TYPES

from User.utils.userRegexValidators import UserRegexValidators


class LogInSerializer(ModelSerializer):
    user_type = ChoiceField(
        choices=USERS_TYPES.choices,
        required=True,
    )
    email = EmailField(
        required=True,
        validators=[
            UserRegexValidators.email_regex,
        ],
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
            "user_type",
            "email",
            "password",
        ]
        extra_kwargs = {
            "user_type": {
                "required": True,
            },
            "email": {
                "required": True,
            },
            "password": {
                "required": True,
                "write_only": True,
            },
        }


@permission_classes([AllowAny])
class LogInAPIView(RetrieveAPIView):
    permission_classes = AllowAny
    serializer_class = LogInSerializer

    def post(self, request, *args, **kwargs):

        email = str(request.data["email"])
        password = str(request.data["password"])

        try:
            user: User = User.objects.filter(email=email).first()
            print(user)
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
                    return Response(
                        {
                            "success": False,
                            "message": "Please Verfy Your Account",
                        },
                        status=status.HTTP_426_UPGRADE_REQUIRED,
                    )
                login(request, user=user)
                token, created = Token.objects.get_or_create(user=user)
                if not user.is_active:
                    user.is_active = True
                    user.save()
                return Response(
                    {
                        "success": True,
                        "message": _("User logged successfully"),
                        "token": token.key,
                        "data": {
                            "User ID": user.uid,
                        },
                    },
                    status=status.HTTP_200_OK,
                )
        except Exception as e:
            return Response(
                {
                    "success": False,
                    "message": f"Error is {e}, with type {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


##########################################


class AuthTokenSerializer(Serializer):
    email = CharField(
        label=_("email"),
        write_only=True,
    )
    password = CharField(
        label=_("Password"),
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )
    token = CharField(
        label=_("Token"),
        read_only=True,
    )

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(
                request=self.context.get("request"),
                username=email,
                password=password,
            )

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _("Unable to log in with provided credentials.")
                raise ValidationError(
                    msg,
                    code="authorization",
                )
        else:
            msg = _('Must include "username" and "password".')
            raise ValidationError(
                msg,
                code="authorization",
            )

        attrs["user"] = user
        return attrs


class CustomAuthToken(ObtainAuthToken):
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "success": True,
                "message": _("User logged successfully"),
                "token": token.key,
                "data": {
                    "User ID": user.uid,
                },
            },
            status=status.HTTP_200_OK,
        )
