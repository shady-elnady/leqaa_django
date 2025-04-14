from django.core.management.base import BaseCommand

from Address.models import City, Country, Governorate


class Command(BaseCommand):
    help = "Creates initial Cities Load Data"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        cities = [
            {
                "name": "Cairo",
                "country": 1,
                "governorate": 1,
                "translations": {
                    "en-us": "Cairo",
                    "ar-eg": "القاهره",
                    "ar-as": "القاهره",
                    "fr-fr": "Caire",
                    "tr-tr": "Kahire",
                },
            },
            {
                "name": "Mansoura",
                "country": 1,
                "governorate": 3,
                "translations": {
                    "en-us": "Mansoura",
                    "ar-eg": "المنصوره",
                    "ar-as": "المنصوره",
                    "fr-fr": "Mansourah",
                    "tr-tr": "Mansoura",
                },
            },
            {
                "name": "Sherbin",
                "country": 1,
                "governorate": 3,
                "translations": {
                    "en-us": "Sherbin",
                    "ar-eg": "شربين",
                    "ar-as": "شربين",
                    "fr-fr": "Sherbine",
                    "tr-tr": "Sherbin",
                },
            },
            {
                "name": "Belqas",
                "country": 1,
                "governorate": 3,
                "translations": {
                    "en-us": "Belqas",
                    "ar-eg": "بلقاس",
                    "ar-as": "بلقاس",
                    "fr-fr": "Belqase",
                    "tr-tr": "Belqas",
                },
            },
            {
                "name": "Talkha",
                "country": 1,
                "governorate": 3,
                "translations": {
                    "en-us": "Talkha",
                    "ar-eg": "طلخا",
                    "ar-as": "طلخا",
                    "fr-fr": "Talkhae",
                    "tr-tr": "Talkha",
                },
            },
            {
                "name": "Abu Dhabi",
                "country": 2,
                "governorate": 27,
                "translations": {
                    "en-us": "Abu Dhabi",
                    "ar-eg": "أبوظبى",
                    "ar-as": "أبوظبى",
                    "fr-fr": "Abou Dhabi",
                    "tr-tr": "Abu Dhabi",
                },
            },
            {
                "name": "Paris",
                "country": 3,
                "governorate": 26,
                "translations": {
                    "en-us": "Paris",
                    "ar-eg": "باريس",
                    "ar-as": "باريس",
                    "fr-fr": "Paris",
                    "tr-tr": "Paris",
                },
            },
        ]

        for city in cities:
            try:
                City.objects.create(
                    name=city["name"],
                    country=Country.objects.get(pk=city["country"]),
                    governorate=Governorate.objects.get(pk=city["governorate"]),
                    translations=city["translations"],
                )

                self.stdout.write(
                    self.style.SUCCESS(f"Successfully Create {city['name']}")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed Create {city['name']} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING("Finish Initial Cities Load Data"))
