from rest_framework.permissions import BasePermission, SAFE_METHODS

from User.models import User


class IsAdminOrReadOnlyForUser(BasePermission):
    """
    Custom permission to:
    - Allow read-only access to authenticated users.
    - Restrict write operations to admin users (customizable via `is_admin_user` method).
    """

    def is_admin_user(self, user: "User"):
        """Override this method for custom admin checks."""
        return user.is_admin

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        return request.user.is_authenticated and self.is_admin_user(request.user)
