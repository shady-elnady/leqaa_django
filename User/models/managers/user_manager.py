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
        password: str,
        user_type: str = USERS_TYPES.User,
        **extra_fields,
    ) -> "User":
        values = [username, email, user_type]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))

        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError(f"{_('The')} {field_name} {_('value must be set')}.")

        with transaction.atomic():
            user: User = self.model(
                user_type=user_type,
                username=username,
                email=self.normalize_email(email),
                **extra_fields,
            )
            user.set_password(password)
            user.save(using=self._db)
            return user

    def create_staff(
        self,
        username: str,
        email: str,
        password: str,
        user_type: str = USERS_TYPES.Staff,
        **extra_fields,
    ) -> "User":
        extra_fields.setdefault("is_active", True)
        return self.create_user(username, email, password, user_type, **extra_fields)

    def create_admin(
        self,
        username: str,
        email: str,
        password: str,
        user_type: str = USERS_TYPES.Admin,
        **extra_fields,
    ) -> "User":
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("email_verified_at", now())
        extra_fields.setdefault("mobile_verified_at", now())
        return self.create_user(username, email, password, user_type, **extra_fields)

    def create_superuser(
        self,
        username: str,
        email: str,
        password: str,
        user_type: str = USERS_TYPES.SuperUser,
        **extra_fields,
    ) -> "User":
        return self.create_admin(username, email, password, user_type, **extra_fields)

    def get_if_exist(self, **extra_fields: Any) -> "User":
        try:
            return self.get(
                **extra_fields,
            )
        except ObjectDoesNotExist:
            raise ValueError(_("User is Not Exist."))
