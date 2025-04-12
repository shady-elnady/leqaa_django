from django.core.management.base import BaseCommand

from Address.models import City, State
from Address.utils.enums import StateTypes


class Command(BaseCommand):
    help = "Creates initial States Load Data"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        states = [
            {
                "name": "State 1",
                "city": 1,
                "postal_code": "12333",
                "state_type": StateTypes.VILLAGE,
                "translations": {
                    "en_US": "State 1",
                    "ar_EG": "ولاية 1",
                    "ar_AS": "ولاية 1",
                    "fr_FR": "État 1",
                    "tr_TR": "Durum 1",
                },
            },
        ]

        for state in states:
            try:
                State.objects.create(
                    name=state["name"],
                    city=City.objects.get(pk=state["city"]),
                    postal_code=state["postal_code"],
                    state_type=state["state_type"],
                    translations=state["translations"],
                )

                self.stdout.write(
                    self.style.SUCCESS(f"Successfully Create {state['name']}")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed Create {state['name']} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING("Finish Initial States Load Data"))
