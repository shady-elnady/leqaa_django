from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError

from Api.permissions import RegisterPermission
from Api.exceptions import (
    SuccessResponse,
    ValidationException,
    DatabaseException,
    ServerException,
    SendEmailException,
    FirebaseException,
)
from App.messages import AuthMessages
from User.models import User
from .serializers import RegisterSerializer
import logging

logger = logging.getLogger(__name__)


class RegisterViewSet(ModelViewSet):
    """
    User registration endpoint with comprehensive error handling
    """

    queryset = User.objects.none()  # Empty queryset since we only need create
    serializer_class = RegisterSerializer
    permission_classes = [RegisterPermission]
    http_method_names = ["post"]  # Only allow POST for registration

    def create(self, request, *args, **kwargs) -> Response:
        """
        Handle user registration with proper exception handling
        """
        serializer = self.get_serializer(data=request.data)

        try:
            # Validate input data
            if not serializer.is_valid():
                raise ValidationException(
                    errors=serializer.errors,
                    message=AuthMessages.REGISTER_VALIDATION_ERROR,
                )

            # Create user
            user = self.perform_create(serializer)

            # Successful registration
            logger.info(f"New user registered: {user.email}")
            return SuccessResponse.create(
                data=serializer.data,
                message=AuthMessages.REGISTER_SUCCESS,
                status_code=status.HTTP_201_CREATED,
            )

        except IntegrityError as e:
            logger.warning(
                f"Duplicate registration attempt for email: {serializer.initial_data.get('email')}",
                exc_info=True,
                extra={"email": serializer.initial_data.get("email"), "error": str(e)},
            )
            raise DatabaseException(
                message=AuthMessages.REGISTER_DUPLICATE,
                data={"email": serializer.initial_data.get("email")},
                status_code=status.HTTP_409_CONFLICT,
            )

        except ValidationException as e:
            # Re-raise explicitly caught validation exceptions
            logger.warning(
                f"Registration validation failed: {str(e)}",
                exc_info=True,
                extra={
                    "errors": e.errors,
                    "email": serializer.initial_data.get("email"),
                },
            )
            raise

        except SendEmailException as e:
            # Handle email sending failures separately
            logger.error(
                f"Verification email failed to send: {str(e)}",
                exc_info=True,
                extra={"email": serializer.initial_data.get("email")},
            )
            raise DatabaseException(
                message=AuthMessages.REGISTER_SUCCESS_BUT_EMAIL_FAILED,
                data={
                    "email": serializer.initial_data.get("email"),
                    "warning": "User created but verification email failed",
                },
                status_code=status.HTTP_201_CREATED,
            )

        except FirebaseException as e:
            # Handle Firebase integration errors
            logger.critical(
                "Firebase integration failure during registration",
                exc_info=True,
                extra={"error": str(e)},
            )
            raise ServerException(
                message=AuthMessages.FIREBASE_INTEGRATION_ERROR,
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        except Exception as e:
            # Catch-all for unexpected errors
            logger.critical(
                f"Unexpected registration error: {str(e)}",
                exc_info=True,
                extra={
                    "email": serializer.initial_data.get("email"),
                    "error_type": type(e).__name__,
                },
            )
            raise ServerException(
                message=f"{AuthMessages.REGISTER_FAILED}: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def perform_create(self, serializer) -> User:
        """Save the user instance and return it"""
        return serializer.save()

    def list(self, request, *args, **kwargs):
        raise ValidationException(
            message=AuthMessages.POST_URL_ONLY,
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    def retrieve(self, request, *args, **kwargs):
        raise ValidationException(
            message=AuthMessages.POST_URL_ONLY,
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    # Override all other disallowed methods
    def update(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
