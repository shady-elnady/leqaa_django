from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from rest_framework.authtoken.models import Token


from firebase_admin import auth
from django.contrib.auth.models import User
import json


# def login_view(request):
#     if request.method != "POST":
#         return JsonResponse({"error": "Method not allowed"}, status=405)

#     try:
#         data = json.loads(request.body)
#         id_token = data.get("idToken")
#         print_debug_info("Id Token", id_token)
#         decoded_token = auth.verify_id_token(id_token)
#         print_debug_info("decoded_token", decoded_token)

#         firebase = getattr(decoded_token, "firebase", None)
#         if firebase:
#             user = get_user_from_firebase(firebase, decoded_token)
#             if user:
#                 return authenticate_and_login(request, user)
#             else:
#                 return JsonResponse({"error": "Authentication failed"}, status=401)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=400)


# def print_debug_info(label, value):
#     print(100 * "!#")
#     print(f"from Log In View > {label}>> {value}")
#     print(100 * "!#")


# def get_user_from_firebase(firebase, decoded_token):
#     sign_in_provider = getattr(firebase, "sign_in_provider", None)
#     if not sign_in_provider:
#         return None

#     try:
#         if sign_in_provider == "phone":
#             mobile = firebase["identities"]["phone"].first()
#             return User.objects.filter(mobile=mobile).first()
#         elif sign_in_provider == "google":
#             email = decoded_token.get("email")
#             return User.objects.filter(email=email).first()
#     except User.DoesNotExist:
#         return None


# def authenticate_and_login(request, user):
#     login(request, user)
#     token, _ = Token.objects.get_or_create(user=user)
#     return JsonResponse(
#         {
#             "token": str(token),
#             "message": "Login successful",
#         }
#     )


def login_page(request):
    return render(request, "Logs/fire_login.html")
