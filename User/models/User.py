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

# from PIL import Image

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
        # "user_type",
        "username",
        "mobile",
        "password",
    ]

    objects = UserManager()

    user_type = CharField(
        max_length=2,
        choices=USERS_TYPES.choices,
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
        error_messages={"unique": UserMessages.MOBILE_UNIQUE_VALIDATION},
        validators=[UserRegexValidators.mobile_regex],
        verbose_name=_("Mobile"),
    )
    otp = CharField(
        max_length=4,
        null=True,
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

    @property
    def is_admin(self) -> bool:
        return self.user_type in [
            USERS_TYPES.Developer,
            USERS_TYPES.SuperUser,
            USERS_TYPES.Admin,
        ]

    @property
    def is_superuser(self) -> bool:
        return self.user_type == USERS_TYPES.SuperUser

    @property
    def is_staff(self) -> bool:
        return self.user_type in [
            USERS_TYPES.Developer,
            USERS_TYPES.SuperUser,
            USERS_TYPES.Admin,
            USERS_TYPES.Staff,
        ]

    def __str__(self) -> str:
        return f"{self.username}"

    def __decode__(self) -> str:
        return f"{self.username}"

    def save(self, *args, **kwargs):
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
        verbose_name_plural = _("Users Album")
