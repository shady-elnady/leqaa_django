from django.forms import ModelForm

from Event.models import EventType  # , EventAlbum ,Event


class EventTypeAdminForm(ModelForm):
    class Meta:
        model = EventType
        fields = [
            "id",
            "name",
            "image",
            "translations",
        ]


# class EventAdminForm(ModelForm):
#     class Meta:
#         model = Event
#         fields = [
#             "id",
#             "title",
#             "hall",
#             "event_type",
#             "category",
#             "lecturer",
#             "university",
#             "college",
#             "organizer",
#             "lecturer_financial_dues",
#             "lecturer_financial_system",
#             "event_paid_status",
#             "description",
#             "start_date_time",
#             "image",
#         ]


# class EventAlbumAdminForm(ModelForm):
#     class Meta:
#         model = EventAlbum
#         fields = [
#             "id",
#             "event",
#             "photo",
#             "order",
#         ]
