from rest_framework.permissions import BasePermission

from User.models import Interest


class IsOwnerOnlyForInterests(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj: Interest):
        # Instance must have an attribute named `user`.
        return bool(obj.user == request.user)

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated())
