from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField
from django.utils.translation import get_language

# Serializers define the API representation.


class BaseTranslationsSerializer(HyperlinkedModelSerializer):
    translated_name = SerializerMethodField("get_translated_name")

    def get_translated_name(self, obj) -> str:
        return obj.translated_name
