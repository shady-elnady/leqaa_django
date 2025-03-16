from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Creates initial models"

    def handle(self, *args, **options):
        commands = [
            ## Base Commands
            "cleanproject_seeds",
            "makemigrations",
            "migrate",
            "collectstatic",
            ## Create Supaer User
            "createsuperuser",
            ## Load Data Commands
            "languages_seeds",
            "currencies_seeds",
            "address_seeds",
            "locales_seeds",
            "categories_seeds",
            "organizations_seeds",
            "users_seeds",
            "events_seeds",
            "reservations_seeds",
            "payments_seeds",
            "advertisements_seeds",
            # "notifications_seeds",
            # "chats_seeds",
            ## End and Run Server
            "runserver",
        ]
        for command in commands:
            try:
                call_command(command)
                if command == "runserver":
                    self.stdout.write(
                        self.style.WARNING("Finish Created All Initial Data")
                    )
                    break
                else:
                    self.stdout.write(self.style.SUCCESS(f"Successfully {command}"))
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"{command} Failed  \n \t \t Error is: {e}")
                )
