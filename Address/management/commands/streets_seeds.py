from django.core.management.base import BaseCommand

from Address.models import State, Street


class Command(BaseCommand):
    help = "Creates initial Streets Load Data"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        streets = [
            {
                "name": "Street 1",
                "state": 1,
                "translations": {
                    "en-us": "Street 1",
                    "ar-eg": "شارع 1",
                    "ar-as": "شارع 1",
                    "fr-fr": "Rue 1",
                    "tr-tr": "Sokak 1",
                },
            },
        ]

        for street in streets:
            try:
                Street.objects.create(
                    name=street["name"],
                    state=State.objects.get(pk=street["state"]),
                    translations=street["translations"],
                )

                self.stdout.write(
                    self.style.SUCCESS(f"Successfully Create {street['name']}")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed Create {street['name']} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING("Finish Initial Streets Load Data"))
