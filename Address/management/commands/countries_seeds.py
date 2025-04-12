from django.core.management.base import BaseCommand
from django.conf import settings
from os.path import join, exists
from os import makedirs

from Address.models import Country
from App.tools import get_model_name_from_class
from Currency.models import Currency
from Language.models import Language


class Command(BaseCommand):
    help = "Creates initial Countries Load Data"

    def handle(self, *args, **options):

        if not exists(
            join(settings.MEDIA_ROOT, "images", get_model_name_from_class(Country))
        ):
            makedirs(
                join(
                    settings.MEDIA_ROOT,
                    "images",
                    get_model_name_from_class(Country),
                )
            )

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        countries = [
            {
                "name": "United State of America",
                "country_code": "US",
                "continent": "AS",
                "flag_emoji": "🇦🇪",
                "currency": 16,
                "language": 3,
                "tel_code": "+1",
                "time_zone": "UTC+02:00",
                "translations": {
                    "en_US": "United State of America",
                    "ar_AS": "الولايات المتحدة الامريكية",
                    "ar_EG": "الولايات المتحدة الامريكية",
                    "fr_FR": "États-Unis d'Amérique",
                    "tr_TR": "Amerika Birleşik Devletleri",
                },
            },
            {
                "name": "Kingdom of Saudi Arabia",
                "country_code": "AS",
                "continent": "AS",
                "flag_emoji": "🇦🇪",
                "currency": 16,
                "language": 3,
                "tel_code": "+966",
                "time_zone": "UTC+02:00",
                "translations": {
                    "en_US": "Kingdom of Saudi Arabia",
                    "ar_AS": "المملكه العربيه السعوديه",
                    "ar_EG": "المملكه العربيه السعوديه",
                    "fr_FR": "Royaume d'Arabie Saoudite",
                    "tr_TR": "Suudi Arabistan Krallığı",
                },
            },
            {
                "name": "Egypt",
                "country_code": "EG",
                "continent": "AF",
                "flag_emoji": "🇪🇬",
                "currency": 7,
                "language": 3,
                "tel_code": "+02",
                "time_zone": "UTC+02:00",
                "translations": {
                    "en_US": "Egypt",
                    "ar_AS": "مصر",
                    "ar_EG": "مصر",
                    "fr_FR": "Egypte",
                    "tr_TR": "Mısır",
                },
            },
            {
                "name": "France",
                "country_code": "FR",
                "continent": "EU",
                "flag_emoji": "🇫🇷",
                "currency": 4,
                "language": 2,
                "tel_code": "33",
                "time_zone": "UTC+02:00",
                "translations": {
                    "en_US": "France",
                    "ar_AS": "فرنسا",
                    "ar_EG": "فرنسا",
                    "fr_FR": "République française",
                    "tr_TR": "Fransa",
                },
            },
            {
                "name": "Turkia",
                "country_code": "TR",
                "continent": "EU",
                "flag_emoji": "🇫🇷",
                "currency": 4,
                "language": 2,
                "tel_code": "33",
                "time_zone": "UTC+02:00",
                "translations": {
                    "en_US": "Turkia",
                    "ar_AS": "تركيا",
                    "ar_EG": "تركيا",
                    "fr_FR": "Turquie",
                    "tr_TR": "Türkiye",
                },
            },
            {
                "name": "United Arab Emirates",
                "country_code": "UA",
                "continent": "AS",
                "flag_emoji": "🇦🇪",
                "currency": 16,
                "language": 3,
                "tel_code": "+971",
                "time_zone": "UTC+02:00",
                "translations": {
                    "en_US": "United Arab Emirates",
                    "ar_AS": "دولة الإمارات العربية المتحدة",
                    "ar_EG": "دولة الإمارات العربية المتحدة",
                    "fr_FR": "Emirats Arabes Unis",
                    "tr_TR": "Birleşik Arap Emirlikleri",
                },
            },
        ]

        country_id = 1
        for country in countries:
            try:
                Country.objects.create(
                    name=country["name"],
                    country_code=country["country_code"],
                    continent=country["continent"],
                    flag_emoji=country["flag_emoji"],
                    image=join(
                        "images",
                        get_model_name_from_class(Country),
                        f"{country_id}.png",
                    ),
                    currency=Currency.objects.get(pk=country["currency"]),
                    language=Language.objects.get(pk=country["language"]),
                    tel_code=country["tel_code"],
                    time_zone=country["time_zone"],
                    translations=country["translations"],
                )
                country_id = country_id + 1
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully Create {country['name']}")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed Create {country['name']} , \n \t Error is: \t \t{e}"
                    )
                )

        self.stdout.write(self.style.WARNING("Finish Initial Countries Load Data"))
