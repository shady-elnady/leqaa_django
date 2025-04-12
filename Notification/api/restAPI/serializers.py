from rest_framework.serializers import HyperlinkedModelSerializer

from Notification.models import Notification
from User.api import UserSerializer
from Category.api import CategorySerializer

# Serializers define the API representation.


class NotificationSerializer(HyperlinkedModelSerializer):
    user = UserSerializer(many=False)
    category = CategorySerializer(many=False)

    class Meta:
        model = Notification
        fields = [
            "url",
            "id",
            "user",
            "category",
            "created_at",
            "last_updated",
        ]
