from rest_framework.serializers import HyperlinkedModelSerializer

from Currency.models import Currency


# Serializers define the API representation.


class CurrencySerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Currency
        fields = [
            "url",
            "id",
            "name",
            "iso_code",
            "symbol",
            "translated_name",
            "created_at",
            "last_updated",
        ]
