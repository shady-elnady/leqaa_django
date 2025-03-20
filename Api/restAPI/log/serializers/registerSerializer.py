from rest_framework.serializers import (
    ModelSerializer,
    EmailField,
    CharField,
    ChoiceField,
)
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from rest_framework.validators import UniqueValidator

from User.utils.userRegexValidators import UserRegexValidators
from User.utils.enums import USERS_TYPES
from User.models.User import User


class RegisterSerializer(ModelSerializer):
    user_type = ChoiceField(
        choices=USERS_TYPES.choices,
    )
    username = CharField(
        max_length=100,
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message=_("User Name is Used. choose Another"),
            ),
        ],
    )
    email = EmailField(
        required=False,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message=_(
                    "E-Mail is Used.",
                ),
            ),
        ],
    )
    mobile = CharField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message=_(
                    "Mobile is Used. choose Another",
                ),
            ),
            UserRegexValidators.mobile_regex,
        ],
    )
    password = CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )

    def create(self, validated_data) -> "User":
        user: User = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = [
            "user_type",
            "username",
            "email",
            "mobile",
            "password",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "password": {
                "required": True,
                "write_only": True,
            },
        }


class UserRegisterSerializer(ModelSerializer):
    username = CharField(
        max_length=100,
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message=_("User Name is Used. choose Another"),
            ),
        ],
    )
    email = EmailField(
        required=False,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message=_(
                    "E-Mail is Used.",
                ),
            ),
        ],
    )
    mobile = CharField(
        required=False,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message=_(
                    "Mobile is Used. choose Another",
                ),
            ),
            UserRegexValidators.mobile_regex,
        ],
    )
    password = CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )

    def create(self, validated_data) -> "User":
        user: User = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "mobile",
            "password",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "password": {
                "required": True,
                "write_only": True,
            },
        }


"""
https://www.geeksforgeeks.org/choice-selection-fields-in-serializers-django-rest-framework/

"""
