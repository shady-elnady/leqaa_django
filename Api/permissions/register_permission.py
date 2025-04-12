from rest_framework.permissions import BasePermission

from User.utils.enums import USERS_TYPES  # Import your User model


class RegisterPermission(BasePermission):
    """
    Permission class to control user registration based on user type:
    - Anyone can create a regular User or Student.
    - Only Admins can create Staff or Lecturer.
    - Only SuperUsers can create Admins.
    """

    message = "You do not have permission to create this user type."

    def has_permission(self, request, view):
        # Extract user_type from request data (e.g., POST payload)
        user_type = request.data.get("user_type")  # Adjust field name as needed

        # Allow User or Student creation for anyone (even unauthenticated)
        if not user_type or user_type in [
            USERS_TYPES.User.value,
            USERS_TYPES.Student.value,
        ]:
            return True

        # Block unauthenticated requests for other user types
        if not request.user.is_authenticated:
            return False

        # Only Admins can create Staff or Lecturer
        if user_type in [USERS_TYPES.Staff.value, USERS_TYPES.Lecturer.value]:
            return request.user.is_admin

        # Only SuperUsers can create Admins
        if user_type == USERS_TYPES.Admin.value:
            return request.user.is_superuser

        # Default deny (invalid user_type)
        return False
