from rest_framework.serializers import HyperlinkedModelSerializer

from Category.models import Category

# Serializers define the API representation.


class CategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = [
            "url",
            "id",
            "name",
            "translations",
            "created_at",
            "last_updated",
        ]
