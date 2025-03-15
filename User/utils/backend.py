from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import MultipleObjectsReturned

# from django.contrib.auth.models import User
from User.models import User


class UserBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        # for if user recorded or not
        try:
            user = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            pass
        except MultipleObjectsReturned:
            return User.objects.filter(email=email).order_by(id).first()
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
