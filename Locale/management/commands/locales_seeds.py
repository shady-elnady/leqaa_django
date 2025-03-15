from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Creates initial Locales Load Data"
    data = "Locales"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        load_data = [
            "locales.json",
        ]
        for data in load_data:
            try:
                call_command("loaddata", data)
                self.stdout.write(self.style.SUCCESS(f"Successfully {data} Load Data"))
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Load Data Failed from {data} , \n \t Error is: \t \t{e}"
                    )
                )

        self.stdout.write(self.style.WARNING(f"Finish Created initial {self.data}"))
