import random
import string
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import (
    CharField,
    EmailField,
    BooleanField,
    DateTimeField,
    PositiveSmallIntegerField,
    ForeignKey,
    CASCADE,
)
from django.utils.translation import gettext_lazy as _


from User.utils.userRegexValidators import UserRegexValidators
from User.utils.enums import USERS_TYPES
from User.utils.usereMessages import UserMessages
from Utils.models.BaseModel import BaseModel, BasePhotoModel, BaseUUIDTimeModel
from .managers.user_manager import UserManager

# Create your models here.


class User(
    AbstractBaseUser,
    PermissionsMixin,
    BaseUUIDTimeModel,
):
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
        "password",
    ]

    objects = UserManager()

    user_type = CharField(
        max_length=2,
        choices=USERS_TYPES.choices,
        default=USERS_TYPES.User,
        verbose_name=_("User Type"),
    )
    username = CharField(
        max_length=100,
        unique=True,
        error_messages={"unique": UserMessages.NAME_UNIQUE_VALIDATION},
        validators=[UserRegexValidators.name_regex],
        verbose_name=_("User Name"),
    )
    email = EmailField(
        unique=True,
        error_messages={"unique": UserMessages.EMAIL_UNIQUE_VALIDATION},
        verbose_name=_("E-mail"),
    )
    mobile = CharField(
        max_length=16,
        unique=True,
        blank=True,
        null=True,
        error_messages={"unique": UserMessages.MOBILE_UNIQUE_VALIDATION},
        validators=[UserRegexValidators.mobile_regex],
        verbose_name=_("Mobile"),
    )
    otp = CharField(
        max_length=4,
        blank=True,
        verbose_name=_("OTP"),
    )
    is_active = BooleanField(
        default=True,
        verbose_name=_("is Active"),
    )
    email_verified_at = DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("E-mail Verified At"),
    )
    mobile_verified_at = DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Mobile Verified At"),
    )
    last_login = DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Last LogIn"),
    )
    is_blocked = BooleanField(
        default=False,
        verbose_name=_("is Blocked"),
    )
    is_staff = BooleanField(
        default=False,
        editable=False,
        help_text=_("Designates whether the user can log into this Staff Site."),
        verbose_name=_("Staff Status"),
    )
    is_admin = BooleanField(
        default=False,
        editable=False,
        help_text=_("Designates whether the user can log into this admin Site."),
        verbose_name=_("Admin Status"),
    )
    is_superuser = BooleanField(
        default=False,
        editable=False,
        help_text=_("Designates that this user has Super User permissions"),
        verbose_name=_("Super User Status"),
    )

    def __str__(self) -> str:
        return f"{self.username}"

    def __decode__(self) -> str:
        return f"{self.username}"

    def save(self, *args, **kwargs):
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
            self.otp = "".join(random.choice(string.digits) for _ in range(4))
        return super(User, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-last_updated"]


class UserAlbum(BaseModel, BasePhotoModel):
    user = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name="UserPhotosAlbum",
        verbose_name=_("User"),
    )
    order = PositiveSmallIntegerField(
        default=1,
        verbose_name=_("Order"),
    )

    def __str__(self) -> str:
        return f"{self.pk}-{self.user.username}"

    def __decode__(self) -> str:
        return f"{self.pk}-{self.user.username}"

    # # importing required modules
    # from os.path import join, exists
    # from os import remove, rename
    # from PIL import Image

    # # resizing images
    # def save(self, *args, **kwargs):
    #     super().save()
    #     img = Image.open(self.photo.path)
    #     if img.height > 100 or img.width > 100:
    #         new_img = (100, 100)
    #         img.thumbnail(new_img)
    #         img.save(self.avatar.path)

    class Meta:
        verbose_name = _("User Album")
        verbose_name_plural = _("Users Albums")
