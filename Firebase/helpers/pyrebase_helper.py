import pyrebase
from django.conf import settings
from django.core.exceptions import ValidationError
from functools import wraps
import logging
from typing import Dict, Any, Optional

from App.messages import AuthMessages

logger = logging.getLogger(__name__)


def handle_pyrebase_errors(func):
    """Decorator to handle Pyrebase exceptions consistently."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except pyrebase.pyrebase.HTTPError as e:
            error_msg = e.args[0].get("error", {}).get("message", str(e))
            logger.error(f"Pyrebase HTTP error: {error_msg}", exc_info=True)
            raise ValidationError(AuthMessages.PYREBASE_HTTP_ERROR)
        except Exception as e:
            logger.error(f"Pyrebase operation failed: {str(e)}", exc_info=True)
            raise ValidationError(AuthMessages.PYREBASE_ERROR)

    return wrapper


class PyrebaseHelper:
    """
    Singleton wrapper for Pyrebase with comprehensive error handling.
    Handles authentication and storage operations with Firebase.
    """

    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._initialize()
            self._initialized = True

    def _initialize(self):
        """Initialize Pyrebase services with configuration validation."""
        if not hasattr(settings, "PYREBASE_CONFIG"):
            logger.critical("Pyrebase configuration missing in settings")
            raise ValidationError(AuthMessages.CONFIG_MISSING)

        try:
            self.app = pyrebase.initialize_app(settings.PYREBASE_CONFIG)
            self.auth = self.app.auth()
            self.storage = self.app.storage()
            self.db = self.app.database()
            logger.info("Pyrebase initialized successfully")
        except Exception as e:
            logger.critical(f"Pyrebase initialization failed: {str(e)}", exc_info=True)
            raise ValidationError(AuthMessages.PYREBASE_INIT_FAILED)

    # ==================== Authentication Methods ====================

    @handle_pyrebase_errors
    def sign_in_with_email_and_password(
        self, email: str, password: str
    ) -> Dict[str, Any]:
        """
        Authenticate user with email/password.

        Args:
            email: User's email address
            password: User's password

        Returns:
            Dictionary containing user credentials

        Raises:
            ValidationError: If authentication fails
        """
        try:
            return self.auth.sign_in_with_email_and_password(email, password)
        except pyrebase.pyrebase.HTTPError as e:
            error_data = e.args[0].get("error", {})
            if error_data.get("message") == "INVALID_EMAIL":
                raise ValidationError(AuthMessages.INVALID_EMAIL)
            elif error_data.get("message") == "INVALID_PASSWORD":
                raise ValidationError(AuthMessages.INVALID_PASSWORD)
            raise

    @handle_pyrebase_errors
    def verify_phone_otp(self, verification_id: str, otp: str) -> Dict[str, Any]:
        """
        Verify phone OTP and authenticate user.

        Args:
            verification_id: Verification ID from SMS request
            otp: One-time password from user

        Returns:
            Dictionary containing user credentials

        Raises:
            ValidationError: If verification fails
        """
        credential = self.auth.PhoneAuthProvider.credential(verification_id, otp)
        return self.auth.sign_in_with_credential(credential)

    @handle_pyrebase_errors
    def get_user(self, uid: str) -> Dict[str, Any]:
        """Get user data by UID."""
        return self.auth.get_user(uid)

    @handle_pyrebase_errors
    def update_user_profile(self, uid: str, updates: Dict[str, Any]) -> None:
        """Update user profile information."""
        self.auth.update_user(uid, **updates)

    # ==================== Storage Methods ====================

    @handle_pyrebase_errors
    def upload_file(self, file_path: str, destination_path: str) -> str:
        """
        Upload file to Firebase Storage.

        Args:
            file_path: Local path to file
            destination_path: Destination path in Firebase Storage

        Returns:
            Download URL of the uploaded file
        """
        storage_child = self.storage.child(destination_path)
        storage_child.put(file_path)
        return storage_child.get_url(None)

    @handle_pyrebase_errors
    def delete_file(self, storage_path: str) -> None:
        """Delete file from Firebase Storage."""
        self.storage.child(storage_path).delete()

    # ==================== Database Methods ====================

    @handle_pyrebase_errors
    def get_data(self, path: str) -> Optional[Dict[str, Any]]:
        """Read data from Firebase Realtime Database."""
        return self.db.child(path).get().val()

    @handle_pyrebase_errors
    def set_data(self, path: str, data: Dict[str, Any]) -> None:
        """Write data to Firebase Realtime Database."""
        self.db.child(path).set(data)

    @handle_pyrebase_errors
    def update_data(self, path: str, updates: Dict[str, Any]) -> None:
        """Update data in Firebase Realtime Database."""
        self.db.child(path).update(updates)
