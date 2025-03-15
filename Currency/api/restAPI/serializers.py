from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField
from django.utils.translation import get_language

from Currency.models import Currency
from Locale.api.restAPI.base.serializer import BaseTranslationsSerializer

# Serializers define the API representation.


class CurrencySerializer(BaseTranslationsSerializer):
    # native = SerializerMethodField("get_native_name")

    # def get_native_name(self, obj) -> str:
    #     return obj.translations[to_locale(get_language())]

    class Meta:
        model = Currency
        fields = [
            "url",
            "id",
            "name",
            # "native",
            "iso_code",
            "symbol",
            "translated_name",
            "native",
            "created_at",
            "last_updated",
        ]
