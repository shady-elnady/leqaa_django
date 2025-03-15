from rest_framework.serializers import HyperlinkedModelSerializer

from Advertisement.models import Advertisement

# Serializers define the API representation.


class AdvertisementSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Advertisement
        fields = [
            "url",
            "id",
            "title",
            "url",
            "description",
            "image",
            "created_at",
            "last_updated",
        ]
