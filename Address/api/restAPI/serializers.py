from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField

from Currency.api import CurrencySerializer
from Language.api import LanguageSerializer

from Address.models import Location, Locality, Street, State, City, Governorate, Country


class CountrySerializer(HyperlinkedModelSerializer):
    currency = CurrencySerializer(many=False)
    language = LanguageSerializer(many=False)

    # # to convert Flag to url
    # flag = SerializerMethodField()  # Add this line
    # def get_flag(self, obj):
    #     """
    #     Custom method to return the flag image URL
    #     """
    #     if obj.flag:  # This checks if the flag field has a value
    #         request = self.context.get("request")
    #         if request:
    #             return request.build_absolute_uri(obj.flag.url)
    #         return obj.flag.url
    #     return None

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
            "flag",  # Add this to include the flag field
            "firebase_image_url",  # Include this if you want the Firebase URL too
            "currency",
            "language",
            "tel_code",
            "time_zone",
            "translations",
            "translated_name",
            "created_at",
            "last_updated",
        ]
        extra_kwargs = {
            "flag": {"required": False}  # Makes the field optional in the API
        }


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
            "translated_name",
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
            "translated_name",
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
            "translated_name",
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
            "translated_name",
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
            "translated_name",
            "created_at",
            "last_updated",
        ]


class LocationSerializer(HyperlinkedModelSerializer):
    locality = LocalitySerializer(many=False)
    street = StreetSerializer(many=False)

    class Meta:
        model = Location
        fields = [
            "url",
            "id",
            "name",
            "locality",
            "street",
            "lat",
            "lng",
            "address",
            "translations",
            "translated_name",
            "created_at",
            "last_updated",
        ]
