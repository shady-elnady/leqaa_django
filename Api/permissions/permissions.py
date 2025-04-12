from rest_framework.permissions import BasePermission, SAFE_METHODS
from User.utils.enums import USERS_TYPES

POST_METHODS = ("POST", "PUT", "PATCH", "DELETE")


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
