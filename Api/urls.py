from django.urls import path
from .restAPI import (
    EMailVerifyAPIView,
    LogInAPIView,
    LogOutAPIView,
    CustomAuthToken,
    PasswordReset,
    ResetPasswordAPI,
)

# from rest_framework.authtoken import views

app_name = "Api"

urlpatterns = [
    path("email-verify/", EMailVerifyAPIView.as_view(), name="apiEmailVerify"),
    path("log-in/", LogInAPIView.as_view(), name="apiLogIn"),
    path("log-out/", LogOutAPIView.as_view(), name="apiLogOut"),
    # path("token-auth/", views.obtain_auth_token, name="tokenAuth"),
    path("token-auth/", CustomAuthToken.as_view(), name="tokenAuth"),
    path(
        "forgot-password",
        PasswordReset.as_view(),
        name="forgotPassword",
    ),
    path(
        "password-reset/<str:encoded_pk>/<str:token>/",
        ResetPasswordAPI.as_view(),
        name="resetPassword",
    ),
]

"""
  https://codevoweb.com/django-implement-2fa-two-factor-authentication/

  https://studygyaan.com/tag/django-rest-framework

"""
