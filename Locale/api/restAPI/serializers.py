from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    SerializerMethodField,
    ImageField,
)
from django.utils.translation import get_language

from Locale.models import Language, Locale

# from Address.api import CountrySerializer

# Serializers define the API representation.


class LanguageSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = [
            "url",
            "id",
            "name",
            "native_name",
            "language_iso_code",
            "is_bidirectional",
            "created_at",
            "last_updated",
        ]


class LocaleSerializer(HyperlinkedModelSerializer):
    language = LanguageSerializer(many=False)
    # country = CountrySerializer(many=False)
    locale_flag = ImageField()

    class Meta:
        model = Locale
        fields = [
            "url",
            "id",
            "country",
            "language",
            "locale_code",
            "locale_flag",
            "is_app_suport",
            "is_bidirectional",
            "language_native_name",
            "created_at",
            "last_updated",
        ]


class AppLocaleSerializer(HyperlinkedModelSerializer):
    language_name = SerializerMethodField("get_language_native_name")
    language_code = SerializerMethodField("get_language_code")
    language_is_bidir = SerializerMethodField("get_language_is_bidirectional")
    locale_flag = ImageField()

    def get_language_native_name(self, obj: Locale) -> str:
        return obj.language.native_name

    def get_language_code(self, obj: Locale) -> bool:
        return obj.language.language_iso_code

    def get_language_is_bidirectional(self, obj: Locale) -> bool:
        return obj.language.is_bidirectional

    class Meta:
        model = Locale
        fields = [
            "language_name",
            "language_code",
            "language_is_bidir",
            "locale_code",
            "locale_flag",
        ]
