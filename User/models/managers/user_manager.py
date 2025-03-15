from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from typing import TYPE_CHECKING, Any  # , Optional
from django.db import transaction

from User.utils.enums import USERS_TYPES

if TYPE_CHECKING:
    from ..User import User


class UserManager(BaseUserManager):
    def create_user(
        self,
        username: str,
        email: str,
        mobile: str,
        password: str,
        user_type: str = USERS_TYPES.User,
        **extra_fields,
    ) -> "User":
        # if not email:
        #     raise ValueError("The Email must be set")
        values = [username, email, mobile, user_type]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))

        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError(f"{_('The')} {field_name} {_('value must be set')}.")

        with transaction.atomic():
            user: User = self.model(
                user_type=user_type,
                username=username,
                email=self.normalize_email(email),
                mobile=mobile,
                **extra_fields,
            )
            user.set_password(password)
            user.save(using=self._db)
            return user

    def create_admin(
        self,
        username: str,
        email: str,
        mobile: str,
        password: str,
        user_type: str = USERS_TYPES.Admin,
        **extra_fields,
    ) -> "User":
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("email_verified_at", now())
        extra_fields.setdefault("mobile_verified_at", now())
        return self.create_user(
            username, email, mobile, password, user_type, **extra_fields
        )

    def create_superuser(
        self,
        username: str,
        email: str,
        mobile: str,
        password: str,
        user_type: str = USERS_TYPES.SuperUser,
        **extra_fields,
    ) -> "User":
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("email_verified_at", now())
        extra_fields.setdefault("mobile_verified_at", now())
        return self.create_user(
            username, email, mobile, password, user_type, **extra_fields
        )

    def create_developer(
        self,
        username: str,
        email: str,
        mobile: str,
        password: str,
        user_type: str = USERS_TYPES.Developer,
        **extra_fields,
    ) -> "User":
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("email_verified_at", now())
        extra_fields.setdefault("mobile_verified_at", now())
        return self.create_user(
            username, email, mobile, password, user_type, **extra_fields
        )

    def get_if_exist(self, **extra_fields: Any) -> "User":
        try:
            return self.get(
                **extra_fields,
            )
        except ObjectDoesNotExist:
            raise ValueError(_("User is Not Exist."))
