from rest_framework.permissions import BasePermission, SAFE_METHODS

POST_METHODS = ("POST", "PUT", "PATCH", "DELETE")


class IsOwnerOrReadOnly(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user


class IsAuthenticatedOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        if (
            request.method in SAFE_METHODS
            or request.user
            and request.user.is_authenticated()
        ):
            return True
        return False


"""

https://stackoverflow.com/questions/19773869/django-rest-framework-separate-permissions-per-methods

"""
