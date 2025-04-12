import firebase_admin
from firebase_admin import (
    credentials,
    auth,
    storage,
    messaging,
    exceptions as firebase_exceptions,
)
from firebase_admin.auth import (
    EmailAlreadyExistsError,
    PhoneNumberAlreadyExistsError,
    # UserNotFoundError,
    # InvalidIdTokenError,
    # ExpiredIdTokenError,
    # RevokedIdTokenError,
    # CertificateFetchError,
)
from django.core.exceptions import ValidationError
from django.conf import settings
import logging
from typing import Optional, Dict, Any, List, Union
from functools import wraps

from App.messages import AuthMessages

logger = logging.getLogger(__name__)


def handle_firebase_errors(func):
    """Decorator to handle Firebase exceptions consistently."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except EmailAlreadyExistsError:
            logger.error("Resource Email Already exists", exc_info=True)
            raise ValidationError(AuthMessages.EMAIL_ALREADY_EXISTS)
        except PhoneNumberAlreadyExistsError:
            logger.error("Resource PhoneNumber Already Exists", exc_info=True)
            raise ValidationError(AuthMessages.PHONE_ALREADY_EXISTS)
        except firebase_exceptions.AlreadyExistsError as e:
            logger.error(f"Resource already exists: {str(e)}", exc_info=True)
            raise ValidationError(AuthMessages.RESOURCE_EXISTS)
        except firebase_exceptions.NotFoundError as e:
            logger.error(f"Resource not found: {str(e)}", exc_info=True)
            raise ValidationError(AuthMessages.RESOURCE_NOT_FOUND)
        except firebase_exceptions.InvalidArgumentError as e:
            logger.error(f"Invalid argument: {str(e)}", exc_info=True)
            raise ValidationError(AuthMessages.INVALID_ARGUMENT)
        except firebase_exceptions.FirebaseError as e:
            logger.error(f"Firebase operation failed: {str(e)}", exc_info=True)
            raise ValidationError(AuthMessages.FIREBASE_ERROR)
        except Exception as e:
            logger.critical(f"Unexpected error: {str(e)}", exc_info=True)
            print(f"Unexpected error: {str(e)}")
            raise ValidationError(AuthMessages.UNEXPECTED_ERROR)

    return wrapper


class FirebaseAdminHelper:
    """
    Singleton wrapper for Firebase Admin SDK with comprehensive error handling.
    Handles authentication, storage, and messaging operations.
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
        """Initialize Firebase Admin SDK with configuration validation."""
        if not hasattr(settings, "FIREBASE_CONFIG_ADMIN_SDK_PATH"):
            logger.critical("Firebase config path missing in settings")
            raise ValidationError(AuthMessages.CONFIG_MISSING)

        try:
            self.cred = credentials.Certificate(
                settings.FIREBASE_CONFIG_ADMIN_SDK_PATH,
            )
            self.app = firebase_admin.initialize_app(
                credential=self.cred,
                options=settings.PYREBASE_CONFIG,
            )
            logger.info("Firebase Admin SDK initialized successfully")
        except firebase_exceptions.FirebaseError as e:
            logger.critical(f"Firebase initialization failed: {str(e)}", exc_info=True)
            raise ValidationError(AuthMessages.FIREBASE_INIT_FAILED)

    # ==================== Authentication Methods ====================

    # @handle_firebase_errors
    def create_user(
        self,
        email: str,
        password: str,
        display_name: Optional[str] = None,
        phone_number: Optional[str] = None,
        email_verified: bool = False,
        disabled: bool = False,
        photo_url: Optional[str] = None,
        **kwargs,
    ) -> auth.UserRecord:
        """Create a new Firebase user with comprehensive validation."""
        return auth.create_user(
            email=email,
            password=password,
            display_name=display_name,
            phone_number=phone_number,
            email_verified=email_verified,
            photo_url=photo_url,
            disabled=disabled,
            **kwargs,
        )

    @handle_firebase_errors
    def verify_id_token(self, token: str, check_revoked: bool = True) -> Dict[str, Any]:
        """Verify Firebase ID token with audience validation."""
        decoded_token = auth.verify_id_token(token, check_revoked=check_revoked)

        # Validate token audience
        if decoded_token.get("aud") != settings.PYREBASE_CONFIG.get("project_id"):
            logger.error(
                "Invalid token audience", extra={"audience": decoded_token.get("aud")}
            )
            raise ValidationError(AuthMessages.INVALID_TOKEN_AUDIENCE)

        return decoded_token

    @handle_firebase_errors
    def set_custom_claims(self, uid: str, claims: Dict[str, Any]) -> bool:
        """Set custom claims for a Firebase user."""
        auth.set_custom_user_claims(uid, claims)
        logger.info(f"Custom claims set for user {uid}")
        return True

    @handle_firebase_errors
    def get_user(self, identifier: Union[str, Dict[str, str]]) -> "auth.UserRecord":
        """Get user by UID, email, or phone number."""
        if isinstance(identifier, dict):
            if "email" in identifier:
                return auth.get_user_by_email(identifier["email"])
            elif "mobile" in identifier:
                return auth.get_user_by_phone_number(identifier["mobile"])
        return auth.get_user(identifier)

    @handle_firebase_errors
    def update_user(
        self,
        uid: str,
        email: Optional[str] = None,
        password: Optional[str] = None,
        display_name: Optional[str] = None,
        phone_number: Optional[str] = None,
        photo_url: Optional[str] = None,
        **kwargs,
    ) -> auth.UserRecord:
        """Update user attributes with proper validation."""
        update_params = {
            k: v
            for k, v in locals().items()
            if k not in ["self", "uid", "kwargs"] and v is not None
        }
        update_params.update(kwargs)
        return auth.update_user(uid, **update_params)

    @handle_firebase_errors
    def delete_user(self, uid: str) -> None:
        """Delete a Firebase user."""
        auth.delete_user(uid)
        logger.info(f"Deleted user {uid}")

    # ==================== Storage Methods ====================

    @handle_firebase_errors
    def upload_file(
        self,
        file_path: str,
        destination_path: str,
        content_type: Optional[str] = None,
        public: bool = True,
    ) -> str:
        """Upload file to Firebase Storage with optional public access."""
        bucket = storage.bucket()
        blob = bucket.blob(destination_path)

        if content_type:
            blob.upload_from_filename(file_path, content_type=content_type)
        else:
            blob.upload_from_filename(file_path)

        if public:
            blob.make_public()

        return blob.public_url if public else blob.path

    @handle_firebase_errors
    def delete_file(self, file_path: str) -> None:
        """Delete file from Firebase Storage."""
        bucket = storage.bucket()
        blob = bucket.blob(file_path)
        blob.delete()
        logger.info(f"Deleted file {file_path}")

    # ==================== Messaging Methods ====================

    @handle_firebase_errors
    def send_message(
        self,
        token: Optional[str] = None,
        topic: Optional[str] = None,
        title: Optional[str] = None,
        body: Optional[str] = None,
        data: Optional[Dict[str, str]] = None,
        **kwargs,
    ) -> str:
        """Send FCM message to device or topic."""
        message = messaging.Message(
            notification=(
                messaging.Notification(title=title, body=body)
                if title and body
                else None
            ),
            data=data,
            token=token,
            topic=topic,
            **kwargs,
        )
        return messaging.send(message)

    @handle_firebase_errors
    def subscribe_to_topic(
        self, tokens: List[str], topic: str
    ) -> messaging.BatchResponse:
        """Subscribe devices to a topic."""
        return messaging.subscribe_to_topic(tokens, topic)

    @handle_firebase_errors
    def unsubscribe_from_topic(
        self, tokens: List[str], topic: str
    ) -> messaging.BatchResponse:
        """Unsubscribe devices from a topic."""
        return messaging.unsubscribe_from_topic(tokens, topic)


"""
    Usage Examples:
        User Management:

            firebase = FirebaseAdminHelper()

            # Create user
            try:
                user = firebase.create_user(
                    email="user@example.com",
                    password="securepassword123",
                    display_name="John Doe"
                )
            except ValidationError as e:
                print(f"Error: {e}")



            # Verify token
            try:
                decoded = firebase.verify_id_token(id_token)
            except ValidationError as e:
                print(f"Invalid token: {e}")


            ################### File Storage:########################
            try:
                url = firebase.upload_file(
                    "/local/path/image.jpg",
                    "users/user123/profile.jpg",
                    content_type="image/jpeg"
                )
            except ValidationError as e:
                print(f"Upload failed: {e}")

            ################################ Notifications########################

            # Send notification
            try:
                response = firebase.send_message(
                    token="device_token",
                    title="Hello",
                    body="This is a test message",
                    data={"key": "value"}
                )
            except ValidationError as e:
                print(f"Notification failed: {e}")
"""
