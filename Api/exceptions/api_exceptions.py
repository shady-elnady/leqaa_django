from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status
from typing import Any, Dict, Optional
from App.messages import AuthMessages  # Your messages module


class CustomAPIException(APIException):
    """
    Base custom exception class that formats responses in the standard structure
    {
        "data": ...,
        "success": False,
        "message": ...,
        "status": ...
    }
    """

    status_code = status.HTTP_400_BAD_REQUEST
    default_message = AuthMessages.UNKNOWN_ERROR  # Your default message
    default_data = None

    def __init__(
        self,
        message: Optional[str] = None,
        data: Optional[Any] = None,
        status_code: Optional[int] = None,
        **kwargs,
    ):
        self.message = f"{message or self.default_message}. ❌"
        self.data = data or self.default_data
        if status_code is not None:
            self.status_code = status_code
        self.extra = kwargs

    def to_response(self) -> Response:
        response_data = {
            "data": self.data,
            "success": False,
            "message": self.message,
            "status": self.status_code,
            **self.extra,
        }
        return Response(
            response_data,
            status=self.status_code,
            exception=True,
        )


# Specific Exception Examples
class NotFoundException(CustomAPIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_message = AuthMessages.NOT_FOUND


class ValidationException(CustomAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_message = AuthMessages.VALIDATION_ERROR

    def __init__(self, errors: Dict, **kwargs):
        super().__init__(data=errors, **kwargs)


class AuthenticationException(CustomAPIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_message = AuthMessages.AUTHENTICATION_FAILED


class PermissionException(CustomAPIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_message = AuthMessages.PERMISSION_DENIED


class DatabaseException(APIException):
    """For database-related errors (duplicate entries, constraints)"""

    status_code = status.HTTP_409_CONFLICT
    default_message = "Database error occurred"

    def __init__(self, message=None, data=None):
        super().__init__(detail=message or self.default_message)
        self.data = data


class ServerException(APIException):
    """For unexpected server errors"""

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_message = "Internal server error"

    def __init__(self, message=None):
        super().__init__(detail=message or self.default_message)


class SendEmailException(APIException):
    """Email service failure"""

    status_code = status.HTTP_424_FAILED_DEPENDENCY
    default_message = "Email service failed"


class FirebaseException(APIException):
    """Firebase integration failure"""

    status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    default_message = "Firebase service unavailable"


# In your exceptions.py
class UnverifiedAccountException(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "Account not verified"
    default_code = "unverified_account"

    def __init__(self, message, extra_data=None):
        self.detail = {
            "message": message,
            "code": self.default_code,
            "extra": extra_data or {},
        }


class InvalidOTPException(APIException):
    """Custom exception for invalid OTP cases"""

    status_code = status.HTTP_400_BAD_REQUEST
    default_message = "Invalid verification code"


class SuccessResponse:
    """
    Utility class for successful responses that match the exception format
    """

    @staticmethod
    def create(
        data: Any = None,
        message: str = AuthMessages.SUCCESS,
        status_code: int = status.HTTP_200_OK,
        **kwargs,
    ) -> Response:
        return Response(
            {
                "data": data,
                "success": True,
                "message": f"{message} ✅",
                "status": status_code,
                **kwargs,
            },
            status=status_code,
            exception=False,
        )


"""
    # Usage Examples:
    def example_view(request):
        try:
            # Your logic here
            serializer = MySerializer(data=request.data)
            if not serializer.is_valid():
                raise ValidationException(errors=serializer.errors)

            # On success
            return SuccessResponse.create(
                data=serializer.data,
                message=AuthMessages.REGISTER_SUCCESS,
                status_code=status.HTTP_201_CREATED,
            )

        except SomeError:
            raise NotFoundException(message="Resource not found")
"""
