from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    Serializer,
    ListField,
    ImageField,
)

from Category.api import CategorySerializer
from Event.models import Event, EventType, EventAlbum
from Organization.api import (
    CollegeSerializer,
    OrganizationSerializer,
    UniversitySerializer,
)
from Reservation.api import ReservationSerializer
from User.api import LecturerSerializer

# Serializers define the API representation.


class EventTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = EventType
        fields = [
            "url",
            "name",
            "image",
            "translations",
            "created_at",
            "last_updated",
        ]


class EventAlbumSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = EventAlbum
        fields = [
            # "url",
            # "id",
            # "event",
            "photo",
            "order",
            "created_at",
            "last_updated",
        ]


class MultipleImageEventAlbumSerializer(Serializer):
    photos = ListField(child=ImageField())


class EventSerializer(HyperlinkedModelSerializer):
    # event_type = EventTypeSerializer(many=False)
    # category = CategorySerializer(many=False)
    # lecturer = LecturerSerializer(many=False)
    # college = CollegeSerializer(many=False)
    # organizer = OrganizationSerializer(many=False)
    university = UniversitySerializer(many=False, read_only=True)
    EventPhotosAlbum = EventAlbumSerializer(many=True)
    Reservations = ReservationSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = [
            "url",
            "id",
            "title",
            "hall",
            "event_type",
            "category",
            "lecturer",
            "university",
            "college",
            "organizer",
            "lecturer_financial_dues",
            "lecturer_financial_system",
            "event_paid_status",
            "on_or_off_line",
            "short_description",
            "complete_description",
            "end_date_time",
            "start_date_time",
            "registration_link",
            "image",
            "EventPhotosAlbum",
            "Reservations",
            "created_at",
            "last_updated",
        ]
