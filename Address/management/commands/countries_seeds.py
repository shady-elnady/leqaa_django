from django.core.management.base import BaseCommand
from django.conf import settings
from os.path import join, exists
from os import makedirs

from Address.models import Country
from Currency.models import Currency
from Locale.models import Language


class Command(BaseCommand):
    help = "Creates initial Countries Load Data"

    def handle(self, *args, **options):

        IMAGES_ROOT = join(settings.MEDIA_ROOT, "images")

        countries_images_directory = join(IMAGES_ROOT, "Countries")
        if not exists(countries_images_directory):
            makedirs(countries_images_directory)

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
                    "en-US": "United State of America",
                    "ar-AS": "الولايات المتحدة الامريكية",
                    "ar-EG": "الولايات المتحدة الامريكية",
                    "fr-FR": "États-Unis d'Amérique",
                    "tr-TR": "Amerika Birleşik Devletleri",
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
                    "en-US": "Kingdom of Saudi Arabia",
                    "ar-AS": "المملكه العربيه السعوديه",
                    "ar-EG": "المملكه العربيه السعوديه",
                    "fr-FR": "Royaume d'Arabie Saoudite",
                    "tr-TR": "Suudi Arabistan Krallığı",
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
                    "en-US": "Egypt",
                    "ar-AS": "مصر",
                    "ar-EG": "مصر",
                    "fr-FR": "Egypte",
                    "tr-TR": "Mısır",
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
                    "en-US": "France",
                    "ar-AS": "فرنسا",
                    "ar-EG": "فرنسا",
                    "fr-FR": "République française",
                    "tr-TR": "Fransa",
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
                    "en-US": "Turkia",
                    "ar-AS": "تركيا",
                    "ar-EG": "تركيا",
                    "fr-FR": "Turquie",
                    "tr-TR": "Türkiye",
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
                    "en-US": "United Arab Emirates",
                    "ar-AS": "دولة الإمارات العربية المتحدة",
                    "ar-EG": "دولة الإمارات العربية المتحدة",
                    "fr-FR": "Emirats Arabes Unis",
                    "tr-TR": "Birleşik Arap Emirlikleri",
                },
            },
        ]

        id = 1
        for country in countries:
            try:
                Country.objects.create(
                    name=country["name"],
                    country_code=country["country_code"],
                    continent=country["continent"],
                    flag_emoji=country["flag_emoji"],
                    flag=join(countries_images_directory, f"{id}.png"),
                    currency=Currency.objects.get(pk=country["currency"]),
                    language=Language.objects.get(pk=country["language"]),
                    tel_code=country["tel_code"],
                    time_zone=country["time_zone"],
                    translations=country["translations"],
                )
                id = id + 1
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
