from firebase_admin import auth, exceptions as firebase_exceptions
from rest_framework import status
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.db import DatabaseError
import logging

from Api.exceptions import (
    SuccessResponse,
    FirebaseException,
    DatabaseException,
    ServerException,
    AuthenticationException,
)
from App.messages import AuthMessages

logger = logging.getLogger(__name__)


class LogOutAPIView(APIView):
    """
    Handles user logout by:
    1. Revoking Firebase tokens
    2. Clearing Django session
    3. Deleting DRF auth token

    Raises:
        FirebaseException: For Firebase-related errors
        DatabaseException: For database operations failures
        AuthenticationException: For session/token issues
        ServerException: For unexpected server errors
    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        try:
            # Firebase logout
            self._handle_firebase_logout(user)

            # Django session logout
            self._handle_django_logout(request)

            # DRF token deletion
            self._handle_token_deletion(user)

            logger.info(
                f"User logout successful - User ID: {user.id}, Email: {user.email}",
                extra={"user_id": user.id, "email": user.email, "action": "logout"},
            )

            return SuccessResponse.create(
                message=AuthMessages.LOGOUT_SUCCESS,
                status_code=status.HTTP_200_OK,
            )

        except firebase_exceptions.FirebaseError as e:
            logger.error(
                f"Firebase logout failed - User ID: {user.id}, Error: {str(e)}",
                exc_info=True,
                extra={
                    "user_id": user.id,
                    "error_type": "firebase",
                    "firebase_uid": getattr(user, "firebase_uid", None),
                },
            )
            raise FirebaseException(
                message=AuthMessages.FIREBASE_LOGOUT_ERROR,
                data={"firebase_uid": getattr(user, "firebase_uid", None)},
                status_code=status.HTTP_502_BAD_GATEWAY,
            )

        except DatabaseError as e:
            logger.error(
                f"Token deletion failed - User ID: {user.id}, Error: {str(e)}",
                exc_info=True,
                extra={"user_id": user.id, "error_type": "database"},
            )
            raise DatabaseException(
                message=AuthMessages.LOGOUT_ERROR,
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        except Exception as e:
            logger.critical(
                f"Unexpected logout error - User ID: {user.id}, Error: {str(e)}",
                exc_info=True,
                extra={
                    "user_id": user.id,
                    "error_type": "unexpected",
                    "exception_type": type(e).__name__,
                },
            )
            raise ServerException(
                message=AuthMessages.LOGOUT_ERROR,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def _handle_firebase_logout(self, user):
        """Handle Firebase token revocation with validation"""
        if not hasattr(user, "firebase_uid") or not user.firebase_uid:
            logger.warning(
                "No Firebase UID associated with user", extra={"user_id": user.id}
            )
            return

        try:
            auth.revoke_refresh_tokens(user.firebase_uid)
            logger.debug(
                f"Firebase tokens revoked - UID: {user.firebase_uid}",
                extra={"firebase_uid": user.firebase_uid},
            )
        except firebase_exceptions.NotFoundError:
            logger.warning(
                f"Firebase user not found - UID: {user.firebase_uid}",
                extra={"firebase_uid": user.firebase_uid},
            )
        except firebase_exceptions.InvalidArgumentError as e:
            logger.error(
                f"Invalid Firebase UID format - UID: {user.firebase_uid}",
                extra={"firebase_uid": user.firebase_uid},
            )
            raise FirebaseException(
                message=AuthMessages.FIREBASE_AUTH_ERROR + str(e),
                status_code=status.HTTP_400_BAD_REQUEST,
            )

    def _handle_django_logout(self, request):
        """Handle Django session cleanup with validation"""
        try:
            if "firebase_uid" in request.session:
                del request.session["firebase_uid"]
            logout(request)
            logger.debug("Django session cleared successfully")
        except Exception as e:
            logger.error(
                "Django session cleanup failed", exc_info=True, extra={"error": str(e)}
            )
            raise AuthenticationException(
                message=AuthMessages.LOGOUT_ERROR,
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

    def _handle_token_deletion(self, user):
        """Handle DRF token deletion with validation"""
        try:
            deleted_count, _ = Token.objects.filter(user=user).delete()
            if deleted_count == 0:
                logger.warning(
                    "No auth tokens found for user during logout",
                    extra={"user_id": user.id},
                )
            else:
                logger.debug(
                    f"Deleted {deleted_count} auth tokens for user",
                    extra={"user_id": user.id},
                )
        except DatabaseError as e:
            logger.error(
                "Token deletion database error",
                exc_info=True,
                extra={"user_id": user.id, "error": str(e)},
            )
            raise
