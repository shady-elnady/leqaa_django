from rest_framework.permissions import BasePermission, SAFE_METHODS
from User.utils.enums import USERS_TYPES

POST_METHODS = ("POST", "PUT", "PATCH", "DELETE")


class IsAdminOrReadOnlyForUser(BasePermission):
    """
    Custom permission to allow only admins to edit and allow read-only access for the user.
    """

    def has_permission(self, request, view):
        # Allow all authenticated users to list views (GET requests)
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        # For other requests (POST, PUT, DELETE, etc.), only admins are allowed
        return request.user.is_authenticated and request.user.is_admin

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD, OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the object (if it has an owner)
        # or if the user is an admin.
        if hasattr(obj, "user"):  # Assuming your model has a 'user' field
            return obj.user == request.user or request.user.is_admin
        elif hasattr(obj, "owner"):  # Or if it has an 'owner' field
            return obj.owner == request.user or request.user.is_admin
        elif request.user.is_admin:
            return True  # Allow admins to modify any object

        return False


class IsAdminOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or request.user and request.user.is_admin
        )


# # Not Used
class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == USERS_TYPES.Student


class IsLecturer(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == USERS_TYPES.Lecturer


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == USERS_TYPES.Admin


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == USERS_TYPES.SuperUser


class IsDeveloper(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == USERS_TYPES.Developer
