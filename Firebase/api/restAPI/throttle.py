# throttles.py
from rest_framework.throttling import AnonRateThrottle
import logging
from django.core.cache import cache
from Firebase.helpers import FirebaseAdminHelper
from firebase_admin.exceptions import FirebaseError

logger = logging.getLogger(__name__)


class FirebaseLogInByIdTokenThrottle(AnonRateThrottle):
    """
    Custom throttle for Firebase authentication endpoints.
    Throttles based on Firebase UID if available, falls back to IP address.
    """

    scope = "firebase_log_in_by_id_token"
    cache_prefix = "firebase_log_in_by_id_token_throttle"

    def get_cache_key(self, request, view):
        # Only throttle POST requests with id_token
        if request.method != "POST" or "id_token" not in request.data:
            return None

        try:
            # Verify the Firebase token and extract UID
            id_token = request.data["id_token"]
            decoded_token = FirebaseAdminHelper().verify_id_token(id_token)
            uid = decoded_token.get("uid")

            if not uid:
                logger.warning(
                    "Firebase token missing UID", extra={"token": id_token[:10] + "..."}
                )
                return self._get_ip_based_key(request)

            return self._generate_cache_key(uid)

        except FirebaseError as e:
            logger.error(
                "Firebase token verification failed",
                exc_info=True,
                extra={"error": str(e), "token": id_token[:10] + "..."},
            )
            return self._get_ip_based_key(request)
        except Exception as e:
            logger.critical(
                "Unexpected error in Firebase throttle",
                exc_info=True,
                extra={"error": str(e)},
            )
            return self._get_ip_based_key(request)

    def _generate_cache_key(self, identifier):
        """Generate consistent cache key format"""
        return f"{self.cache_prefix}_{self.scope}_{identifier}"

    def _get_ip_based_key(self, request):
        """Fallback to IP-based throttling"""
        ident = self.get_ident(request)
        return self._generate_cache_key(f"ip_{ident}")

    def throttle_failure(self):
        """Additional actions when throttling occurs"""
        logger.warning(
            "Firebase authentication throttled",
            extra={"scope": self.scope, "rate": self.rate},
        )
        return super().throttle_failure()
