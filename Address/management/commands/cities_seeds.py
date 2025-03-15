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
                    "en-US": "Cairo",
                    "ar-EG": "القاهره",
                    "ar-AS": "القاهره",
                    "fr-FR": "Caire",
                    "tr-TR": "Kahire",
                },
            },
            {
                "name": "Mansoura",
                "country": 1,
                "governorate": 3,
                "translations": {
                    "en-US": "Mansoura",
                    "ar-EG": "المنصوره",
                    "ar-AS": "المنصوره",
                    "fr-FR": "Mansourah",
                    "tr-TR": "Mansoura",
                },
            },
            {
                "name": "Sherbin",
                "country": 1,
                "governorate": 3,
                "translations": {
                    "en-US": "Sherbin",
                    "ar-EG": "شربين",
                    "ar-AS": "شربين",
                    "fr-FR": "Sherbine",
                    "tr-TR": "Sherbin",
                },
            },
            {
                "name": "Belqas",
                "country": 1,
                "governorate": 3,
                "translations": {
                    "en-US": "Belqas",
                    "ar-EG": "بلقاس",
                    "ar-AS": "بلقاس",
                    "fr-FR": "Belqase",
                    "tr-TR": "Belqas",
                },
            },
            {
                "name": "Talkha",
                "country": 1,
                "governorate": 3,
                "translations": {
                    "en-US": "Talkha",
                    "ar-EG": "طلخا",
                    "ar-AS": "طلخا",
                    "fr-FR": "Talkhae",
                    "tr-TR": "Talkha",
                },
            },
            {
                "name": "Abu Dhabi",
                "country": 2,
                "governorate": 27,
                "translations": {
                    "en-US": "Abu Dhabi",
                    "ar-EG": "أبوظبى",
                    "ar-AS": "أبوظبى",
                    "fr-FR": "Abou Dhabi",
                    "tr-TR": "Abu Dhabi",
                },
            },
            {
                "name": "Paris",
                "country": 3,
                "governorate": 26,
                "translations": {
                    "en-US": "Paris",
                    "ar-EG": "باريس",
                    "ar-AS": "باريس",
                    "fr-FR": "Paris",
                    "tr-TR": "Paris",
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
