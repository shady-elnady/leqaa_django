from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.throttling import AnonRateThrottle
from django.utils import timezone
from django.core.signing import TimestampSigner

from Api.exceptions import ValidationException
from User.models import User


class VerifyEmailByURLThrottle(AnonRateThrottle):
    scope = "verify_email_by_url"

    def get_cache_key(self, request, view):
        # Throttle by IP and email (if available in token)
        if request.method == "GET" and "token" in request.query_params:
            try:
                token = request.query_params["token"]
                signer = TimestampSigner()
                unsigned_value = signer.unsign(token)
                user_id = unsigned_value.split("-")[1]
                return f"{self.scope}_{self.get_ident(request)}_{user_id}"
            except:
                # Fallback to IP-only throttling if token parsing fails
                return f"{self.scope}_{self.get_ident(request)}"
        return None


@permission_classes([AllowAny])
class VerifyEmailByURLAPIView(APIView):
    """
    Email verification endpoint with rate limiting
    Scope: 'verify_email_by_url' (6/hour)
    """

    throttle_classes = [VerifyEmailByURLThrottle]

    def throttled(self, request, wait):
        """Custom response when rate limit is exceeded"""
        data = {
            "message": "Too many verification attempts",
            "available_in": f"{wait} seconds",
            "detail": "Please wait before trying again or request a new verification email",
        }
        return Response(data, status=status.HTTP_429_TOO_MANY_REQUESTS)

    def get(self, request):
        token = request.query_params.get("token")
        if not token:
            # This counts against rate limit
            return Response(
                {"message": "Verification token is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = User.verify_token(token)
            if user.email_verified_at is None:
                user.email_verified_at = timezone.now()
                user.save()
                return Response(
                    {"message": "Email successfully verified"},
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"message": "Email was already verified"}, status=status.HTTP_200_OK
            )
        except ValidationException as e:
            # Failed attempts count against rate limit
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
