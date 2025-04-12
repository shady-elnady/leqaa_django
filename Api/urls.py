from django.urls import path
from Api.views import (
    LogInAPIView,
    LogOutAPIView,
    PasswordResetAPIView,
    ForgotPasswordAPIView,
    VeifyEmailByOTPAPIView,
    MobileVerificationAPIView,
    VerifyEmailByURLAPIView,
)

from Firebase.api import FirebaseLogInByIdTokenAPIView

app_name = "Api"

urlpatterns = [
    path("log-in/", LogInAPIView.as_view(), name="api_log_in"),
    path(
        "firebase-log-in-by-id-token/",
        FirebaseLogInByIdTokenAPIView.as_view(),
        name="firebase_log_in_by_id_token",
    ),
    path(
        "verify-email-by-otp/",
        VeifyEmailByOTPAPIView.as_view(),
        name="verify_email_by_otp",
    ),
    path(
        "verify-email-by-url/",
        VerifyEmailByURLAPIView.as_view(),
        name="verify_email_by_url",
    ),
    path(
        "mobile-verification/",
        MobileVerificationAPIView.as_view(),
        name="verify_mobile",
    ),
    path("log-out/", LogOutAPIView.as_view(), name="api_log_out"),
    path(
        "forgot-password",
        ForgotPasswordAPIView.as_view(),
        name="forgot_password",
    ),
    path(
        "password-reset/<str:encoded_pk>/<str:token>/",
        PasswordResetAPIView.as_view(),
        name="password_reset",
    ),
]

"""
  https://codevoweb.com/django-implement-2fa-two-factor-authentication/

  https://studygyaan.com/tag/django-rest-framework

"""
