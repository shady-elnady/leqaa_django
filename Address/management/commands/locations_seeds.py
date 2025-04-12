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
                    "en_US": "Cairo",
                    "ar_EG": "القاهره",
                    "ar_AS": "القاهره",
                    "fr_FR": "Caire",
                    "tr_TR": "Kahire",
                },
            },
            {
                "name": "Address 2",
                "locality": 1,
                "street": 1,
                "lat": 22.4343434,
                "lng": 22.4343434,
                "translations": {
                    "en_US": "Mansoura",
                    "ar_EG": "المنصوره",
                    "ar_AS": "المنصوره",
                    "fr_FR": "Mansourah",
                    "tr_TR": "Mansoura",
                },
            },
            {
                "name": "Address 3",
                "locality": 1,
                "street": 1,
                "lat": 22.4343434,
                "lng": 22.4343434,
                "translations": {
                    "en_US": "Sherbin",
                    "ar_EG": "شربين",
                    "ar_AS": "شربين",
                    "fr_FR": "Sherbine",
                    "tr_TR": "Sherbin",
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
