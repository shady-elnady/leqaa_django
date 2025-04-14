from django.core.management.base import BaseCommand

from Address.models import Location, Locality, Street


class Command(BaseCommand):
    help = "Creates initial Locations Load Data"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        addresses = [
            {
                "name": "Address 1",
                "locality": 1,
                "street": 1,
                "lat": 22.4343434,
                "lng": 22.4343434,
                "translations": {
                    "en-us": "Cairo",
                    "ar-eg": "القاهره",
                    "ar-as": "القاهره",
                    "fr-fr": "Caire",
                    "tr-tr": "Kahire",
                },
            },
            {
                "name": "Address 2",
                "locality": 1,
                "street": 1,
                "lat": 22.4343434,
                "lng": 22.4343434,
                "translations": {
                    "en-us": "Mansoura",
                    "ar-eg": "المنصوره",
                    "ar-as": "المنصوره",
                    "fr-fr": "Mansourah",
                    "tr-tr": "Mansoura",
                },
            },
            {
                "name": "Address 3",
                "locality": 1,
                "street": 1,
                "lat": 22.4343434,
                "lng": 22.4343434,
                "translations": {
                    "en-us": "Sherbin",
                    "ar-eg": "شربين",
                    "ar-as": "شربين",
                    "fr-fr": "Sherbine",
                    "tr-tr": "Sherbin",
                },
            },
        ]

        for address in addresses:
            try:
                Location.objects.create(
                    name=address["name"],
                    locality=Locality.objects.get(pk=address["locality"]),
                    street=Street.objects.get(pk=address["street"]),
                    lat=address["lat"],
                    lng=address["lng"],
                    translations=address["translations"],
                )

                self.stdout.write(
                    self.style.SUCCESS(f"Successfully Create {address['name']}")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed Create {address['name']} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING("Finish Initial Locations Load Data"))
