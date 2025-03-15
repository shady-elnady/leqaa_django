from rest_framework.serializers import HyperlinkedModelSerializer

from Currency.api import CurrencySerializer
from Locale.api import LanguageSerializer

from Address.models import Address, Locality, Street, State, City, Governorate, Country


class CountrySerializer(HyperlinkedModelSerializer):
    currency = CurrencySerializer(many=False)
    language = LanguageSerializer(many=False)

    class Meta:
        model = Country
        fields = [
            "url",
            "id",
            "name",
            "country_code",
            "continent",
            "capital",
            "flag_emoji",
            "flag",
            "currency",
            "language",
            "tel_code",
            "time_zone",
            "translations",
            "created_at",
            "last_updated",
        ]


class GovernorateSerializer(HyperlinkedModelSerializer):
    country = CountrySerializer(many=False)

    class Meta:
        model = Governorate
        fields = [
            "url",
            "id",
            "name",
            "country",
            "governorate_tel_code",
            "translations",
            "created_at",
            "last_updated",
        ]


class CitySerializer(HyperlinkedModelSerializer):
    country = CountrySerializer(many=False)
    governorate = GovernorateSerializer(many=False)

    class Meta:
        model = City
        fields = [
            "url",
            "id",
            "name",
            "country",
            "governorate",
            "translations",
            "created_at",
            "last_updated",
        ]


class StateSerializer(HyperlinkedModelSerializer):
    city = CitySerializer(many=False)

    class Meta:
        model = State
        fields = [
            "url",
            "id",
            "name",
            "city",
            "postal_code",
            "state_type",
            "translations",
            "created_at",
            "last_updated",
        ]


class StreetSerializer(HyperlinkedModelSerializer):
    state = StateSerializer(many=False)

    class Meta:
        model = Street
        geo_field = "geo_location"
        fields = [
            "url",
            "id",
            "name",
            "state",
            "translations",
            "created_at",
            "last_updated",
        ]
        auto_bbox = True


class LocalitySerializer(HyperlinkedModelSerializer):
    state = StateSerializer(many=False)

    class Meta:
        model = Locality
        fields = [
            "url",
            "id",
            "name",
            "state",
            "translations",
            "created_at",
            "last_updated",
        ]


class AddressSerializer(HyperlinkedModelSerializer):
    locality = LocalitySerializer(many=False)
    street = StreetSerializer(many=False)

    class Meta:
        model = Address
        fields = [
            "url",
            "id",
            "name",
            "locality",
            "street",
            "translations",
            "created_at",
            "last_updated",
        ]
