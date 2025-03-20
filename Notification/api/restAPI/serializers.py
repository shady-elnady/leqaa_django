from rest_framework.serializers import HyperlinkedModelSerializer

from Notification.models import Notification
from User.api import UserSerializer
from Event.api import EventSerializer

# Serializers define the API representation.


class NotificationSerializer(HyperlinkedModelSerializer):
    user = UserSerializer(many=False)
    event = EventSerializer(many=False)

    class Meta:
        model = Notification
        fields = [
            "url",
            "id",
            "user",
            "event",
            "created_at",
            "last_updated",
        ]
