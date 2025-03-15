from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Creates initial Address Load Data"

    def handle(self, *args, **options):

        address_seeds = [
            "countries_seeds",
            "governorates_seeds",
            "cities_seeds",
            "capitals_seeds",
        ]
        for addressSeed in address_seeds:
            try:
                call_command(addressSeed)
                self.stdout.write(self.style.SUCCESS(f"Successfully {addressSeed}"))
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"{addressSeed} Failed  \n \t \t Error is: {e}")
                )

        # load_data = [
        #     "countries.json",
        #     "governorates.json",
        #     "cities.json",
        # ]
        # for data in load_data:
        #     try:
        #         call_command("loaddata", data)
        #         self.stdout.write(self.style.SUCCESS(f"Successfully {data} Load Data"))
        #     except Exception as e:
        #         self.stdout.write(
        #             self.style.ERROR(
        #                 f"Load Data Failed from {data} , \n \t Error is: \t \t{e}"
        #             )
        #         )

        self.stdout.write(self.style.WARNING("Finish Created Address Initial Data"))
