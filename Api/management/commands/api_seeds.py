from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Creates initial models"
    commands = [
        ## Base Commands
        "cleanproject_seeds",
        "makemigrations",
        "migrate",
        "collectstatic",
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
        "notifications_seeds",
        # "chats_seeds",
        ## End
        "end",
    ]

    def handle(self, *args, **options):
        return self.run_commands()

    def run_commands(self):
        for command in self.commands:
            if command == "end":
                break
            else:
                try:
                    call_command(command)
                    self.stdout.write(self.style.SUCCESS(f"Successfully {command}"))
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f"{command} Failed  \n \t \t Error is: {e}")
                    )
                    if command == "cleanproject_seeds":
                        return call_command("runserver")
        return self.create_superuser_and_run_server()

    def create_superuser_and_run_server(self):
        try:
            call_command("createsuperuser")
            return call_command("runserver")
        except Exception:
            return None
