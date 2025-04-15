from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import (
    CharField,
    EmailField,
    BooleanField,
    DateTimeField,
    PositiveSmallIntegerField,
    ForeignKey,
    ManyToManyField,
    CASCADE,
    QuerySet,
)
from firebase_admin.exceptions import (
    AlreadyExistsError,
    FirebaseError,
    InvalidArgumentError,
)
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.utils.crypto import get_random_string
from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from datetime import timedelta
from django.urls import reverse
from firebase_admin.auth import (
    EmailAlreadyExistsError,
    PhoneNumberAlreadyExistsError,
    UserRecord,
    UserNotFoundError,
)
from typing import Optional, TYPE_CHECKING
from django.http import HttpRequest
from django.db import transaction
from django.conf import settings
import random
import string
import secrets
import logging

from Api.exceptions.api_exceptions import ValidationException
from App.fields import MobileModelField
from App.models import BaseModel, BaseImageModel
from App.messages import (
    ModelsMessages,
    ValidationMessages,
    FieldsMessages,
    AuthMessages,
)
from Firebase.helpers import FirebaseAdminHelper
from .managers.user_manager import UserManager
from Category.models import Category
from User.utils.enums import USERS_TYPES


if TYPE_CHECKING:
    from Event.models import Event


# Create your models here.

logger = logging.getLogger(__name__)

firebase_admin_helper: FirebaseAdminHelper = FirebaseAdminHelper()


# # Old Code
class User(
    AbstractBaseUser,
    PermissionsMixin,
    BaseModel,
):
    """
    Custom User model with Firebase integration and comprehensive type hints.
    """

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
        "password",
    ]

    objects: "UserManager" = UserManager()

    # ==================== Fields with Type Hints ====================
    user_type: "CharField" = CharField(
        max_length=2,
        choices=USERS_TYPES.choices,
        default=USERS_TYPES.User,
        verbose_name=FieldsMessages.USER_TYPE,
    )

    username: "CharField" = CharField(
        max_length=100,
        verbose_name=FieldsMessages.USER_NAME,
    )

    email: "EmailField" = EmailField(
        unique=True,
        verbose_name=FieldsMessages.EMAIL,
    )

    mobile: "MobileModelField" = MobileModelField()

    firebase_uid: "CharField" = CharField(
        max_length=255,
        unique=True,
        editable=False,
        verbose_name=FieldsMessages.FIREBASE_UID,
    )

    fcm_token: "CharField" = CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=FieldsMessages.FCM_DEVICE,
    )

    # Relationships with explicit type hints
    interesting_notifiable_categories: "QuerySet[Category]" = ManyToManyField(
        Category,
        through="User.Interest",
        related_name="Category_Favorited_by",
        verbose_name=FieldsMessages.INTERESTING_NOTIFIABLE_CATEGORIES,
    )
    favorite_events: "QuerySet[Event]" = ManyToManyField(
        "Event.Event",
        through="Favorite.Favorite",
        related_name="Event_Favorited_by",
        verbose_name=FieldsMessages.FAVORITE_EVENTS,
    )
    otp: "CharField" = CharField(
        max_length=settings.OTP_CHARACTER_LENGTH,
        error_messages={
            "max_length": ValidationMessages.OTP_MAX_LENGTH.format(
                settings.OTP_CHARACTER_LENGTH
            ),
            "invalid": ValidationMessages.OTP_INVALID.format(
                settings.OTP_CHARACTER_LENGTH
            ),
        },
        null=True,
        blank=True,
        verbose_name=FieldsMessages.OTP_KEY,
    )
    is_active: "BooleanField" = BooleanField(
        default=True,
        verbose_name=FieldsMessages.ACTIVE_STATUS,
    )
    email_verified_at: "DateTimeField" = DateTimeField(
        null=True,
        blank=True,
        verbose_name=FieldsMessages.EMAIL_VERIFIED_AT,
    )
    mobile_verified_at: "DateTimeField" = DateTimeField(
        null=True,
        blank=True,
        verbose_name=FieldsMessages.MOBILE_VERIFIED_AT,
    )
    last_login: "DateTimeField" = DateTimeField(
        null=True,
        blank=True,
        verbose_name=FieldsMessages.LAST_LOGIN,
    )
    is_blocked: "BooleanField" = BooleanField(
        default=False,
        verbose_name=FieldsMessages.BLOCKED_STATUS,
    )
    is_staff: "BooleanField" = BooleanField(
        default=False,
        editable=False,
        verbose_name=FieldsMessages.IS_STAFF,
    )
    is_admin: "BooleanField" = BooleanField(
        default=False,
        editable=False,
        verbose_name=FieldsMessages.IS_ADMIN,
    )
    is_superuser: "BooleanField" = BooleanField(
        default=False,
        editable=False,
        verbose_name=FieldsMessages.IS_SUPERUSER,
    )

    # ==================== Firebase Integration Methods ====================
    def create_or_get_firebase_user(self) -> "UserRecord":
        try:
            return firebase_admin_helper.create_user(
                email=self.email,
                password=self.password,
                display_name=self.username,
                phone_number=self.mobile,
                email_verified=bool(self.email_verified_at),
                disabled=self.is_blocked,
            )
        except (EmailAlreadyExistsError, AlreadyExistsError):
            return firebase_admin_helper.get_user(email=self.email)
        except PhoneNumberAlreadyExistsError:
            return firebase_admin_helper.get_user(mobile=self.mobile)
        except InvalidArgumentError:
            raise ValidationError(AuthMessages.INVALID_ARGUMENT)
        except FirebaseError as e:
            raise ValidationError(AuthMessages.FIREBASE_ERROR.format(str(e)))

    def set_user_custom_claims(self):
        try:
            firebase_admin_helper.set_custom_claims(
                uid=self.firebase_uid,
                claims={
                    "isAdmin": self.is_admin,
                    "isStaff": self.is_staff,
                    "isSuperUser": self.is_superuser,
                },
            )
        except Exception:
            pass

    def update_or_create_firebase_user(self) -> "UserRecord":
        try:
            firebase_updated_user: "UserRecord" = firebase_admin_helper.update_user(
                uid=self.firebase_uid,
                email=self.email,
                password=self.password,
                display_name=self.username,
                phone_number=self.mobile,
                email_verified=bool(self.email_verified_at),
                disabled=self.is_blocked,
            )
            return firebase_updated_user
        except UserNotFoundError:
            return self.create_or_get_firebase_user()
        except InvalidArgumentError:
            raise ValidationError(AuthMessages.INVALID_ARGUMENT)
        except FirebaseError as e:
            raise ValidationError(AuthMessages.FIREBASE_ERROR.format(str(e)))

        # ==================== Parameters ====================

    def _set_parameters(self) -> str:
        """Internal method to update permissions based on user_type"""
        self.is_staff = bool(
            self.user_type
            in [
                USERS_TYPES.Staff,
                USERS_TYPES.Admin,
                USERS_TYPES.SuperUser,
            ]
        )
        self.is_admin = bool(
            self.user_type in [USERS_TYPES.Admin, USERS_TYPES.SuperUser]
        )
        self.is_superuser = bool(
            self.user_type in [USERS_TYPES.Admin, USERS_TYPES.SuperUser]
        )
        if not self.otp:
            self.otp = self.generate_OTP()

    # ==================== E-Mail Verification URL ====================
    def get_email_verification_url(
        self, request: Optional["HttpRequest"] = None
    ) -> str:
        """
        Generate email verification URL with token using request.build_absolute_uri()
        Example: https://yourdomain.com/api/verify-email-by-url/?token=abc123
        """
        try:
            token = self.generate_verification_token()

            # Use request.build_absolute_uri() if request is available
            if request:
                base_url = request.build_absolute_uri(
                    reverse("Api:verify_email_by_url")
                )
                return f"{base_url}?token={token}"

            # Fallback for cases without request (e.g., celery tasks)
            from django.contrib.sites.models import Site

            protocol = getattr(settings, "URL_PROTOCOL", "https")
            domain = Site.objects.get_current().domain
            return f"{protocol}://{domain}{reverse('Api:verify_email_by_url')}?token={token}"

        except Exception as e:
            logger.error(f"Failed to generate verification URL: {e}", exc_info=True)
            return getattr(settings, "DEFAULT_VERIFICATION_URL", "")

    # ==================== Type Hint Properties ====================

    def generate_verification_token(self):
        """
        Generates a time-limited, signed verification token
        Valid for 24 hours by default
        """
        signer = TimestampSigner()
        return signer.sign(f"verify-{self.pk}-{get_random_string(8)}")

    @classmethod
    def verify_token(cls, token):
        """
        Verifies the token and returns the user if valid
        Raises exceptions for invalid/expired tokens
        """
        signer = TimestampSigner()
        try:
            # Verify token signature and expiration (default 24h)
            unsigned_value = signer.unsign(
                token,
                max_age=timedelta(
                    hours=getattr(settings, "EMAIL_VERIFICATION_TIMEOUT_HOURS", 24)
                ),
            )

            # Extract user ID from token
            user_id = unsigned_value.split("-")[1]
            return cls.objects.get(pk=user_id)

        except SignatureExpired:
            raise ValidationException("Verification link has expired")
        except BadSignature:
            raise ValidationException("Invalid verification link")
        except (IndexError, cls.DoesNotExist):
            raise ValidationException("Invalid user in verification link")

    # ==================== Type Hint Properties ====================

    @property
    def encoded_uid(self) -> str:

        from django.utils.http import urlsafe_base64_encode
        from django.utils.encoding import force_bytes

        return urlsafe_base64_encode(force_bytes(self.uid))

    @property
    def change_otp(self) -> str:
        """change OTP and saves it to the user's otp field."""
        self.otp = self.generate_OTP()
        self.save()
        return self.otp

    @property
    def clear_otp(self) -> bool:
        try:
            self.otp = None
            self.save()
            return True
        except Exception:
            return False

    # ==================== Static Methods ====================
    @staticmethod
    def generate_password(length=12):
        """
        Generates a strong random password.
        Default length is 12 characters.
        """
        alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
        while True:
            password = "".join(secrets.choice(alphabet) for _ in range(length))
            # Ensure the password meets basic requirements
            if (
                any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(c in "!@#$%^&*" for c in password)
            ):
                return password

    @staticmethod
    def get_user_by_encoded_uid(encoded_uid) -> Optional["User"]:
        """
        Decodes a base64-encoded user ID and retrieves the corresponding user.

        Args:
            encoded_uid (str): The base64-encoded user ID.

        Returns:
            User or None: The User object if found, otherwise None.
        """
        # try:

        #     return User.objects.get(uid=urlsafe_base64_decode(encoded_uid).decode())
        # except (ValueError, ObjectDoesNotExist, TypeError):
        #     return None

        from django.utils.encoding import force_str
        from django.utils.http import urlsafe_base64_decode

        try:
            uid = force_str(urlsafe_base64_decode(encoded_uid))
            return User.objects.get(uid=uid)
        except (TypeError, ValueError, OverflowError, ObjectDoesNotExist):
            return None

    @staticmethod
    def generate_OTP() -> str:
        characters = (
            string.digits
        )  # You can add string.ascii_letters for alphanumeric OTP
        return "".join(
            random.choice(characters)
            for _ in range(getattr(settings, "OTP_CHARACTER_LENGTH", 4))
        )

    def __str__(self) -> str:
        return f"{self.username}"

    def __decode__(self) -> str:
        return f"{self.username}"

    def save(self, *args, **kwargs):
        """
        Custom save method that handles both create and update operations
        with Firebase synchronization and comprehensive error handling.
        """
        with transaction.atomic():
            # Update parameters before saving
            self._set_parameters()  # If using method version
            # Handle Firebase operations
            try:
                firebase_user = (
                    self.update_or_create_firebase_user()
                    if self.pk
                    else self.create_or_get_firebase_user()
                )
                self.firebase_uid = firebase_user.uid
                self.set_user_custom_claims
                super().save(*args, **kwargs)
            except Exception as e:
                logger.error(f"Firebase operation failed: {str(e)}")
                raise

    def delete(self, *args, **kwargs):
        """
        Overrides the delete method to also delete the Firebase user.
        """
        """
        Deletes both Django and Firebase users with error handling.
        """
        if self.firebase_uid:
            try:
                firebase_admin_helper.delete_user(self.firebase_uid)
                logger.info(f"Deleted Firebase user {self.firebase_uid}")
            except Exception as e:
                logger.error(f"Failed to delete Firebase user: {str(e)}")
                raise ValueError(AuthMessages.FIREBASE_DELETE_ERROR) from e

        return super().delete(*args, **kwargs)

    class Meta:
        verbose_name = ModelsMessages.USER
        verbose_name_plural = ModelsMessages.USERS
        ordering = ["-last_updated"]


class UserAlbum(BaseModel, BaseImageModel):
    user = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name="UserPhotosAlbum",
        verbose_name=ModelsMessages.USER,
    )
    order = PositiveSmallIntegerField(
        default=1,
        verbose_name=FieldsMessages.ORDER,
    )

    def __str__(self) -> str:
        return f"{self.pk}-{self.user.username}"

    def __decode__(self) -> str:
        return f"{self.pk}-{self.user.username}"

    class Meta:
        verbose_name = ModelsMessages.USER_ALBUM
        verbose_name_plural = ModelsMessages.USER_ALBUMS
