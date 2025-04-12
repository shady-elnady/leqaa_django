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
                    "en_US": "Cairo",
                    "ar_EG": "القاهره",
                    "ar_AS": "القاهره",
                    "fr_FR": "Caire",
                    "tr_TR": "Kahire",
                },
            },
            {
                "name": "Mansoura",
                "country": 1,
                "governorate": 3,
                "translations": {
                    "en_US": "Mansoura",
                    "ar_EG": "المنصوره",
                    "ar_AS": "المنصوره",
                    "fr_FR": "Mansourah",
                    "tr_TR": "Mansoura",
                },
            },
            {
                "name": "Sherbin",
                "country": 1,
                "governorate": 3,
                "translations": {
                    "en_US": "Sherbin",
                    "ar_EG": "شربين",
                    "ar_AS": "شربين",
                    "fr_FR": "Sherbine",
                    "tr_TR": "Sherbin",
                },
            },
            {
                "name": "Belqas",
                "country": 1,
                "governorate": 3,
                "translations": {
                    "en_US": "Belqas",
                    "ar_EG": "بلقاس",
                    "ar_AS": "بلقاس",
                    "fr_FR": "Belqase",
                    "tr_TR": "Belqas",
                },
            },
            {
                "name": "Talkha",
                "country": 1,
                "governorate": 3,
                "translations": {
                    "en_US": "Talkha",
                    "ar_EG": "طلخا",
                    "ar_AS": "طلخا",
                    "fr_FR": "Talkhae",
                    "tr_TR": "Talkha",
                },
            },
            {
                "name": "Abu Dhabi",
                "country": 2,
                "governorate": 27,
                "translations": {
                    "en_US": "Abu Dhabi",
                    "ar_EG": "أبوظبى",
                    "ar_AS": "أبوظبى",
                    "fr_FR": "Abou Dhabi",
                    "tr_TR": "Abu Dhabi",
                },
            },
            {
                "name": "Paris",
                "country": 3,
                "governorate": 26,
                "translations": {
                    "en_US": "Paris",
                    "ar_EG": "باريس",
                    "ar_AS": "باريس",
                    "fr_FR": "Paris",
                    "tr_TR": "Paris",
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
