from rest_framework.serializers import HyperlinkedModelSerializer

from Event.api import EventSerializer
from Reservation.models import Reservation
from User.api import UserSerializer

# Serializers define the API representation.


class ReservationSerializer(HyperlinkedModelSerializer):
    student = UserSerializer(many=False)
    event = EventSerializer(many=False)

    class Meta:
        model = Reservation
        fields = [
            "url",
            "id",
            "student",
            "event",
            "reservation_status",
            "rating",
            "canceled_reason",
            "comment",
            "created_at",
            "last_updated",
        ]
