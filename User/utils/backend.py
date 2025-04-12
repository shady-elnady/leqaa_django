from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import MultipleObjectsReturned
from typing import Optional

from User.models import User


class UserBackend(ModelBackend):
    def authenticate(
        self, request, username=None, email=None, password=None, **kwargs
    ) -> Optional["User"]:
        if username is None:
            username = kwargs.get(User.USERNAME_FIELD)
        if username is None or password is None:
            return
        # for if user recorded or not
        try:
            user: "User" = User.objects.get_by_natural_key(username)
        except User.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            User().set_password(password)
        except MultipleObjectsReturned:
            user: "User" = (
                User.objects.filter(**{self.model.USERNAME_FIELD: username})
                .order_by(id)
                .first()
            )
            return user
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
