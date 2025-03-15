from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.serializers import (
    Serializer,
    EmailField,
    CharField,
    ValidationError,
)
from rest_framework.generics import GenericAPIView
from django.utils.encoding import force_bytes
from rest_framework import status, response
from django.urls import reverse

from User.models import User


class EmailSerializer(Serializer):
    """
    Reset Password Email Request Serializer.
    """

    email = EmailField(required=True)

    class Meta:
        fields = ("email",)


class ResetPasswordSerializer(Serializer):
    """
    Reset Password Serializer.
    """

    password = CharField(
        write_only=True,
        min_length=1,
    )

    class Meta:
        field = "password"

    def validate(self, data):
        """
        Verify token and encoded_pk and then set new password.
        """
        password = data.get("password")
        token = self.context.get("kwargs").get("token")
        encoded_pk = self.context.get("kwargs").get("encoded_pk")

        if token is None or encoded_pk is None:
            raise ValidationError("Missing data.")

        pk = urlsafe_base64_decode(encoded_pk).decode()
        user = User.objects.get(pk=pk)
        if not PasswordResetTokenGenerator().check_token(user, token):
            raise ValidationError("The reset token is invalid")

        user.set_password(password)
        user.save()
        return data


class PasswordReset(GenericAPIView):
    """
    Request for Password Reset Link.
    """

    serializer_class = EmailSerializer

    def post(self, request):
        """
        Create token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data["email"]
        user = User.objects.filter(email=email).first()
        if user:
            encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            reset_url = reverse(
                "reset-password",
                kwargs={"encoded_pk": encoded_pk, "token": token},
            )
            reset_link = f"localhost:8000{reset_url}"

            # send the rest_link as mail to the user.

            return response.Response(
                {
                    "message": f"Your password rest link: {reset_link}",
                },
                status=status.HTTP_200_OK,
            )
        else:
            return response.Response(
                {
                    "message": "User doesn't exists",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class ResetPasswordAPI(GenericAPIView):
    """
    Verify and Reset Password Token View.
    """

    serializer_class = ResetPasswordSerializer

    def patch(self, request, *args, **kwargs):
        """
        Verify token & encoded_pk and then reset the password.
        """
        serializer = self.serializer_class(
            data=request.data, context={"kwargs": kwargs}
        )
        serializer.is_valid(raise_exception=True)
        return response.Response(
            {"message": "Password reset complete"},
            status=status.HTTP_200_OK,
        )
