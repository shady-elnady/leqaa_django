from rest_framework.serializers import Serializer, CharField, EmailField
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode as uid_decoder
from django.utils.encoding import force_str
from django.conf import settings  # noqa: F401

from User.models.User import User


class ResetPasswordEmailSerializer(Serializer):
    email = EmailField(required=True)


class VerifyEmailSerializer(Serializer):
    key = CharField(write_only=True)


class ResendEmailVerificationSerializer(Serializer):
    email = EmailField(required=True)


class ChangePasswordSerializer(Serializer):
    old_password = CharField(max_length=128, required=True)
    new_password1 = CharField(max_length=128, required=True)
    new_password2 = CharField(max_length=128, required=True)

    set_password_form_class = SetPasswordForm

    set_password_form = None

    def __init__(self, *args, **kwargs):
        self.old_password_field_enabled = True
        self.logout_on_password_change = True
        super().__init__(*args, **kwargs)

        if not self.old_password_field_enabled:
            self.fields.pop("old_password")

        self.request = self.context.get("request")
        self.user = getattr(self.request, "user", None)

    def validate_old_password(self, value):
        invalid_password_conditions = (
            self.old_password_field_enabled,
            self.user,
            not self.user.check_password(value),
        )

        if all(invalid_password_conditions):
            err_msg = _(
                "Your old password was entered incorrectly. Please enter it again."
            )
            raise ValidationError(err_msg)
        return value

    def custom_validation(self, attrs):
        pass

    def validate(self, attrs):
        self.set_password_form = self.set_password_form_class(
            user=self.user,
            data=attrs,
        )

        self.custom_validation(attrs)
        if not self.set_password_form.is_valid():
            raise ValidationError(self.set_password_form.errors)
        return attrs

    def save(self):
        self.set_password_form.save()
        if not self.logout_on_password_change:
            from django.contrib.auth import update_session_auth_hash

            update_session_auth_hash(self.request, self.user)


class PasswordResetSerializer(Serializer):
    """
    Serializer for confirming a password reset attempt.
    """

    new_password1 = CharField(max_length=128)
    new_password2 = CharField(max_length=128)
    uid = CharField()
    token = CharField()

    set_password_form_class = SetPasswordForm

    _errors = {}
    user = None
    set_password_form = None

    def custom_validation(self, attrs):
        pass

    def validate(self, attrs):
        # Decode the uidb64 (allauth use base36) to uid to get User object
        try:
            uid = force_str(uid_decoder(attrs["uid"]))
            self.user = User._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise ValidationError({"uid": [_("Invalid value")]})

        if not default_token_generator.check_token(self.user, attrs["token"]):
            raise ValidationError({"token": [_("Invalid value")]})

        self.custom_validation(attrs)
        # Construct SetPasswordForm instance
        self.set_password_form = self.set_password_form_class(
            user=self.user,
            data=attrs,
        )
        if not self.set_password_form.is_valid():
            raise ValidationError(self.set_password_form.errors)

        return attrs

    def save(self):
        return self.set_password_form.save()
