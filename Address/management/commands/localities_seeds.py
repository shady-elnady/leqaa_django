from django.core.management.base import BaseCommand

from Address.models import Locality, State


class Command(BaseCommand):
    help = "Creates initial Localities Load Data"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        localities = [
            {
                "name": "Locality 1",
                "state": 1,
                "translations": {
                    "en_US": "Locality 1",
                    "ar_EG": "محليه 1",
                    "ar_AS": "محليه 1",
                    "fr_FR": "Localité 1",
                    "tr_TR": "Yerellik 1",
                },
            },
        ]

        for locality in localities:
            try:
                Locality.objects.create(
                    name=locality["name"],
                    state=State.objects.get(pk=locality["state"]),
                    translations=locality["translations"],
                )

                self.stdout.write(
                    self.style.SUCCESS(f"Successfully Create {locality['name']}")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed Create {locality['name']} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING("Finish Initial Localities Load Data"))
