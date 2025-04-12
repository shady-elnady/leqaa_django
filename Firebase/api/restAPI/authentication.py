from django.core.exceptions import ObjectDoesNotExist
from rest_framework import authentication
import firebase_admin.auth as auth

from User.models import User


class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):

        token = request.headers.get("Authorization")
        if not token:
            return None

        try:
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token["uid"]
        except auth.InvalidIdTokenError:
            return None
        except Exception:
            return None

        try:
            user: User = User.objects.get(firebase_uid=uid)
            return user

        except ObjectDoesNotExist:
            return None
