from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    Serializer,
    ListField,
    ImageField,
    ValidationError,
)

from Address.api import LocationSerializer
from App.fields import DateTimeDRFField
from Event.models import Event, EventType, EventAlbum

# # Imports may needed
# from django.utils.dateparse import parse_datetime
# from Organization.api import (
#     UniversitySerializer,
# )
# from Reservation.api import ReservationSerializer

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
            "image",
            "order",
            "created_at",
            "last_updated",
        ]


class MultipleImageEventAlbumSerializer(Serializer):
    photos = ListField(child=ImageField())


class EventSerializer(HyperlinkedModelSerializer):
    # university = UniversitySerializer(many=False, read_only=True)
    # EventPhotosAlbum = EventAlbumSerializer(many=True)
    # Reservations = ReservationSerializer(many=True, read_only=True)
    # location = LocationSerializer(many=False, read_only=True)
    start_date_time = DateTimeDRFField()
    end_date_time = DateTimeDRFField()

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
            "location",
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

    def validate(self, data):
        """Validate datetime logic at serializer level"""
        start = data.get("start_date_time")
        end = data.get("end_date_time")

        if start and end and end <= start:
            raise ValidationError(
                {
                    "end_date_time": "Must be after start date time",
                },
            )
        return data
