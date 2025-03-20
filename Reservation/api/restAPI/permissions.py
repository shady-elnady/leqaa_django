from rest_framework.permissions import BasePermission

from Reservation.models import Reservation


class IsRegistrant(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, reservation: Reservation):
        # Instance must have an attribute named `owner`.
        return reservation.user == request.user
