from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from django.core.signing import BadSignature, SignatureExpired
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.throttling import AnonRateThrottle

from Api.exceptions import ValidationException
from User.models import User
import logging

logger = logging.getLogger(__name__)


class VerifyEmailByURLThrottle(AnonRateThrottle):
    scope = "verify_email_by_url"

    def get_cache_key(self, request, view):
        if request.method == "GET" and "token" in request.query_params:
            try:
                token = request.query_params["token"]
                user_id = token.split(":")[0].split("-")[-1]
                return f"{self.scope}_{self.get_ident(request)}_{user_id}"
            except Exception as e:
                logger.warning(f"Token parsing failed for throttling: {e}")
        return super().get_cache_key(request, view)


@permission_classes([AllowAny])
class VerifyEmailByURLAPIView(APIView):
    """
    Email verification endpoint that supports:
    - Web browser redirects
    - API JSON responses
    - Rate limiting
    - Token validation
    """

    throttle_classes = [VerifyEmailByURLThrottle]

    def get_response_format(self, request):
        """Determine if client expects HTML (browser) or JSON (API)"""
        accept_header = request.META.get("HTTP_ACCEPT", "")
        if "text/html" in accept_header and "application/json" not in accept_header:
            return "html"
        return "json"

    def get_success_response(self, request, user, already_verified=False):
        """Generate appropriate success response based on client type"""
        response_data = {
            "status": "success",
            "message": (
                "Email already verified"
                if already_verified
                else "Email successfully verified"
            ),
            "user_id": user.id,
            "email": user.email,
            "verified_at": (
                user.email_verified_at.isoformat() if user.email_verified_at else None
            ),
        }

        if self.get_response_format(request) == "html":
            success_url = reverse("Api:email_verified_success")
            # success_url = getattr(
            #     settings, "EMAIL_VERIFICATION_SUCCESS_URL", "/email-verified/"
            # )
            redirect_url = request.GET.get("redirect", success_url)

            # Security check for redirect URLs
            if not redirect_url.startswith(("http://", "https://")):
                return redirect(
                    f"{redirect_url}?message={'Email+already+verified' if already_verified else 'Email+verified+successfully'}"
                )
            return redirect(success_url)
        else:
            return Response(response_data, status=status.HTTP_200_OK)

    def get_error_response(self, request, error_type, error_message=None):
        """Generate appropriate error response based on client type"""
        error_data = {
            "status": "error",
            "error": error_type,
            "message": error_message or self.get_error_message(error_type),
        }

        if self.get_response_format(request) == "html":
            return redirect(
                f"{reverse('Api:email-verification-error')}?error={error_type}"
            )
        else:
            return Response(error_data, status=self.get_error_status_code(error_type))

    def get_error_message(self, error_type):
        messages = {
            "token_expired": "Verification link has expired",
            "invalid_token": "Invalid verification token",
            "validation_error": "Validation failed",
            "server_error": "Internal server error",
            "missing_token": "Verification token is required",
        }
        return messages.get(error_type, "An error occurred")

    def get_error_status_code(self, error_type):
        codes = {
            "token_expired": status.HTTP_400_BAD_REQUEST,
            "invalid_token": status.HTTP_400_BAD_REQUEST,
            "validation_error": status.HTTP_400_BAD_REQUEST,
            "server_error": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "missing_token": status.HTTP_400_BAD_REQUEST,
        }
        return codes.get(error_type, status.HTTP_400_BAD_REQUEST)

    def throttled(self, request, wait):
        """Custom throttled response that works for both API and browser"""
        if self.get_response_format(request) == "html":
            return redirect(
                f"{reverse('email-verification-error')}?error=rate_limit&wait={wait}"
            )
        else:
            return super().throttled(request, wait)

    def get(self, request):
        token = request.query_params.get("token")
        if not token:
            logger.warning("Email verification attempt without token")
            return self.get_error_response(request, "missing_token")

        try:
            user = User.verify_token(token)

            if user.email_verified_at is None:
                user.email_verified_at = timezone.now()
                user.save()
                logger.info(f"Email verified for user {user.id}")
                return self.get_success_response(request, user)

            logger.info(f"Email already verified for user {user.id}")
            return self.get_success_response(request, user, already_verified=True)

        except SignatureExpired:
            logger.warning(f"Expired verification token: {token}")
            return self.get_error_response(request, "token_expired")

        except BadSignature:
            logger.warning(f"Invalid verification token: {token}")
            return self.get_error_response(request, "invalid_token")

        except ValidationException as e:
            logger.warning(f"Validation failed for token {token}: {str(e)}")
            return self.get_error_response(request, "validation_error", str(e))

        except Exception as e:
            logger.error(
                f"Unexpected error during email verification: {str(e)}", exc_info=True
            )
            return self.get_error_response(request, "server_error")
