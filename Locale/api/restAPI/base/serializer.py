from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField
from django.utils.translation import get_language

from Currency.models import Currency

# Serializers define the API representation.


def to_locale(language):
    """Turn a language name (en-us) into a locale name (en_US)."""
    lang, _, country = language.lower().partition("-")
    if not country:
        return language[:3].lower() + language[3:]
    # A language with > 2 characters after the dash only has its first
    # character after the dash capitalized; e.g. sr-latn becomes sr-Latn.
    # A language with 2 characters after the dash has both characters
    # capitalized; e.g. en-us becomes en-US.
    country, _, tail = country.partition("-")
    country = country.title() if len(country) > 2 else country.upper()
    if tail:
        country += "-" + tail
    return lang + "-" + country


class BaseTranslationsSerializer(HyperlinkedModelSerializer):
    native = SerializerMethodField("get_native_name")

    def get_native_name(self, obj) -> str:
        return obj.translations[to_locale(get_language())]

    # class Meta:
    #     model = Currency
    #     fields = [
    #         "url",
    #         "id",
    #         "name",
    #         # "native",
    #         "iso_code",
    #         "symbol",
    #         "translated_name",
    #         "native",
    #         "created_at",
    #         "last_updated",
    #     ]
