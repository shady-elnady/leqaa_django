from rest_framework.serializers import HyperlinkedModelSerializer

from Favorite.models import Favorite
from User.api import UserSerializer
from Event.api import EventSerializer

# Serializers define the API representation.


class FavoriteSerializer(HyperlinkedModelSerializer):
    user = UserSerializer(many=False)
    event = EventSerializer(many=False)

    class Meta:
        model = Favorite
        fields = [
            "url",
            "id",
            "user",
            "event",
            "created_at",
            "last_updated",
        ]
