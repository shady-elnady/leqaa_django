from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Creates initial Address Load Data"

    def handle(self, *args, **options):

        address_seeds = [
            "countries_seeds",
            "governorates_seeds",
            "cities_seeds",
            "states_seeds",
            "localities_seeds",
            "streets_seeds",
            "locations_seeds",
        ]
        for address_seed in address_seeds:
            try:
                call_command(address_seed)
                self.stdout.write(self.style.SUCCESS(f"Successfully {address_seed}"))
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"{address_seed} Failed  \n \t \t Error is: {e}")
                )

        self.stdout.write(self.style.WARNING("Finish Created Address Initial Data"))
