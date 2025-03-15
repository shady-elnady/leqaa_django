from django.core.management.base import BaseCommand

from Address.models.Country import Country
from Address.models.City import City


class Command(BaseCommand):
    help = "Creates initial Capitals Load Data"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        my_countries = [
            {
                "name": "Egypt",
                "capital": 1,
            },
            {
                "name": "United Arab Emirates",
                "capital": 6,
            },
            {
                "name": "France",
                "capital": 7,
            },
        ]
        for my_country in my_countries:
            try:
                country = Country.objects.get(
                    name=my_country["name"],
                )
                country.capital = City.objects.get(id=my_country["capital"])
                country.save()
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully Update Capital of {my_country['name']}"
                    )
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed Update Capital of {my_country['name']} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING("Finish Initial Capitals Load Data"))
