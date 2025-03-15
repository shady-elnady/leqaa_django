from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    data = "Payments"
    help = "Creates Payment initial Data"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        commands = [
            "payment_methods_seeds",
            "payment_statuses_seeds",
        ]
        for command in commands:
            try:
                call_command(command)
                self.stdout.write(self.style.SUCCESS(f"Payment Successfully {command}"))
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Payment Initial {command} Failed  \n \t \t Error is: {e}"
                    )
                )

        self.stdout.write(self.style.WARNING(f"Finish Created initial {self.data}"))
