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
