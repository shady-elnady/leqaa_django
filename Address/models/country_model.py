from django.db.models import CharField, ForeignKey, OneToOneField, CASCADE
import pytz

from App.models import BaseImageModel
from App.validators import RegexValidators
from App.messages import ModelsMessages, FieldsMessages
from Address.utils.enums import CONTINENTS
from Language.models import BaseTranslationModel
from Language.models import Language
from Currency.models import Currency

# Create your models here.


class Country(BaseTranslationModel, BaseImageModel):

    ## https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes

    ALL_TIMEZONES = sorted((item, item) for item in pytz.all_timezones)

    country_code = CharField(
        max_length=3,
        unique=True,
        verbose_name=ModelsMessages.COUNTRY_CODE,
    )
    continent = CharField(
        max_length=2,
        choices=CONTINENTS.choices,
        verbose_name=FieldsMessages.CONTINENT,
    )
    capital = OneToOneField(
        to="Address.City",
        on_delete=CASCADE,
        blank=True,
        null=True,
        related_name="Capital To +",
        verbose_name=FieldsMessages.CAPITAL,
    )
    flag_emoji = CharField(
        max_length=5,
        blank=True,
        null=True,
        verbose_name=FieldsMessages.FLAG,
    )
    currency = ForeignKey(
        Currency,
        on_delete=CASCADE,
        related_name="Countries",
        verbose_name=ModelsMessages.CURRENCY,
    )
    language = ForeignKey(
        Language,
        on_delete=CASCADE,
        related_name="Countries",
        verbose_name=ModelsMessages.LANGUAGE,
    )
    tel_code = CharField(
        max_length=5,
        null=True,
        blank=True,
        validators=[RegexValidators.telephone_country_code_pattern_validator],
        verbose_name=FieldsMessages.TELPHONE_CODE,
    )
    time_zone = CharField(
        max_length=32,
        null=True,
        blank=True,
        choices=ALL_TIMEZONES,
        verbose_name=FieldsMessages.TIME_ZONE,
    )

    #############################################################
    ######################### Image Filed  ######################
    #############################################################
    @property
    def flag(self):
        if self.image:
            return self.image.url
        if self.firebase_image_url:
            return self.firebase_image_url
        return f"https://flagsapi.com/{self.country_code.upper()}/shiny/64.png"

    @flag.setter
    def flag(self, value):
        return self.image.url

    @flag.setter
    def flag(self, value):
        self.image = value

    #############################################################

    class Meta:
        verbose_name = ModelsMessages.COUNTRY
        verbose_name_plural = ModelsMessages.COUNTRIES


# # TODO API FOR COUNTRIES
# https://restcountries.com/#api-endpoints-v3
# https://gitlab.com/restcountries/restcountries

## pip install python-restcountries
# https://github.com/SteinRobert/python-restcountries
""" 
    {
        "name": {
            "common": "Egypt",
            "official": "Arab Republic of Egypt",
            "nativeName": {
                "ara": {
                    "official": "جمهورية مصر العربية",
                    "common": "مصر"
                }
            }
        },
        "tld": [
            ".eg",
            ".مصر"
        ],
        "cca2": "EG",
        "ccn3": "818",
        "cca3": "EGY",
        "cioc": "EGY",
        "independent": true,
        "status": "officially-assigned",
        "unMember": true,
        "currencies": {
            "EGP": {
                "name": "Egyptian pound",
                "symbol": "£"
            }
        },
        "idd": {
            "root": "+2",
            "suffixes": [
                "0"
            ]
        },
        "capital": [
            "Cairo"
        ],
        "altSpellings": [
            "EG",
            "Arab Republic of Egypt"
        ],
        "region": "Africa",
        "subregion": "Northern Africa",
        "languages": {
            "ara": "Arabic"
        },
        "translations": {
            "ara": {
                "official": "جمهورية مصر العربية",
                "common": "مصر"
            },
            "ces": {
                "official": "Egyptská arabská republika",
                "common": "Egypt"
            },
            "cym": {
                "official": "Gweriniaeth Arabaidd yr Aifft",
                "common": "Yr Aifft"
            },
            "deu": {
                "official": "Arabische Republik Ägypten",
                "common": "Ägypten"
            },
            "est": {
                "official": "Egiptuse Araabia Vabariik",
                "common": "Egiptus"
            },
            "fin": {
                "official": "Egyptin arabitasavalta",
                "common": "Egypti"
            },
            "fra": {
                "official": "République arabe d'Égypte",
                "common": "Égypte"
            },
            "hrv": {
                "official": "Arapska Republika Egipat",
                "common": "Egipat"
            },
            "hun": {
                "official": "Egyiptomi Arab Köztársaság",
                "common": "Egyiptom"
            },
            "ita": {
                "official": "Repubblica araba d'Egitto",
                "common": "Egitto"
            },
            "jpn": {
                "official": "エジプト·アラブ共和国",
                "common": "エジプト"
            },
            "kor": {
                "official": "이집트 아랍 공화국",
                "common": "이집트"
            },
            "nld": {
                "official": "Arabische Republiek Egypte",
                "common": "Egypte"
            },
            "per": {
                "official": "جمهوری عربی مصر",
                "common": "مصر"
            },
            "pol": {
                "official": "Arabska Republika Egiptu",
                "common": "Egipt"
            },
            "por": {
                "official": "República Árabe do Egipto",
                "common": "Egito"
            },
            "rus": {
                "official": "Арабская Республика Египет",
                "common": "Египет"
            },
            "slk": {
                "official": "Egyptská arabská republika",
                "common": "Egypt"
            },
            "spa": {
                "official": "República Árabe de Egipto",
                "common": "Egipto"
            },
            "swe": {
                "official": "Arabrepubliken Egypten",
                "common": "Egypten"
            },
            "urd": {
                "official": "مصری عرب جمہوریہ",
                "common": "مصر"
            },
            "zho": {
                "official": "阿拉伯埃及共和国",
                "common": "埃及"
            }
        },
        "latlng": [
            27,
            30
        ],
        "landlocked": false,
        "borders": [
            "ISR",
            "LBY",
            "PSE",
            "SDN"
        ],
        "area": 1002450,
        "demonyms": {
            "eng": {
                "f": "Egyptian",
                "m": "Egyptian"
            },
            "fra": {
                "f": "Égyptienne",
                "m": "Égyptien"
            }
        },
        "flag": "🇪🇬",
        "maps": {
            "googleMaps": "https://goo.gl/maps/uoDRhXbsqjG6L7VG7",
            "openStreetMaps": "https://www.openstreetmap.org/relation/1473947"
        },
        "population": 102334403,
        "gini": {
            "2017": 31.5
        },
        "fifa": "EGY",
        "car": {
            "signs": [
                "ET"
            ],
            "side": "right"
        },
        "timezones": [
            "UTC+02:00"
        ],
        "continents": [
            "Africa"
        ],
        "flags": {
            "png": "https://flagcdn.com/w320/eg.png",
            "svg": "https://flagcdn.com/eg.svg"
        },
        "coatOfArms": {
            "png": "https://mainfacts.com/media/images/coats_of_arms/eg.png",
            "svg": "https://mainfacts.com/media/images/coats_of_arms/eg.svg"
        },
        "startOfWeek": "sunday",
        "capitalInfo": {
            "latlng": [
                30.05,
                31.25
            ]
        },
        "postalCode": {
            "format": "#####",
            "regex": "^(\\d{5})$"
        }
    }
"""
