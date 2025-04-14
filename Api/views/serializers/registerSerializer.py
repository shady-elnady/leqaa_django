from rest_framework.serializers import (
    ModelSerializer,
    EmailField,
    CharField,
    ChoiceField,
)
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

from App.validators import RegexValidators
from App.messages import ValidationMessages, AuthMessages
from User.utils.enums import USERS_TYPES
from User.models.User import User


class RegisterSerializer(ModelSerializer):
    user_type = ChoiceField(
        choices=USERS_TYPES.choices,
        default=USERS_TYPES.User,
        required=False,
    )
    username = CharField(
        max_length=100,
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message=ValidationMessages.USER_NAME_INVALID_UNIQUE_VALIDATION_MESSAGE,
            ),
        ],
    )
    email = EmailField(
        required=False,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message=ValidationMessages.EMAIL_INVALID_UNIQUE_VALIDATION_MESSAGE,
            ),
        ],
    )
    mobile = CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message=ValidationMessages.MOBILE_INVALID_UNIQUE_VALIDATION_MESSAGE,
            ),
            RegexValidators.mobile_pattern_validator,
        ],
    )
    password = CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )

    def create(self, validated_data) -> "User":
        user_type = getattr(validated_data, "user_type", None)
        if user_type and user_type not in USERS_TYPES.choices:
            raise ValueError(ValidationMessages.USER_TYPE_INVALID_VALIDATION_MESSAGE)
        if user_type and user_type in [
            USERS_TYPES.Staff,
            USERS_TYPES.Admin,
            USERS_TYPES.SuperUser,
            USERS_TYPES.Developer,
        ]:
            raise ValueError(ValidationMessages.PERMISSION_ERROR)
        user: User = User.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance: User):
        representation = super().to_representation(instance)
        representation["message"] = AuthMessages.REGISTER_SUCCESS
        return representation

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
