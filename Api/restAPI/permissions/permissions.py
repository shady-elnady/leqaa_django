from rest_framework.permissions import BasePermission
from User.utils.enums import USERS_TYPES


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


class IsOwner(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Instance must have an attribute named `owner`.
        return obj.owner == request.user
