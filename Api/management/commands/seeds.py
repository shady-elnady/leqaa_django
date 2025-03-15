from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
from os.path import join, exists
from os import makedirs


class Command(BaseCommand):
    help = "Creates initial models"

    def handle(self, *args, **options):

        ## Create Database Folder
        database_dir = join(settings.BASE_DIR, "Database")
        if not exists(database_dir):
            makedirs(database_dir)

        ## Create Media Folders
        files = [
            "images",
            "sounds",
            "videos",
            "svg",
        ]
        for file in files:
            file_dir = join(settings.MEDIA_ROOT, file)
            if not exists(file_dir):
                makedirs(file_dir)

        ##
        commands = [
            ## Base Commands
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
            # "notifications_seeds",
            # "chats_seeds",
            ## End and Run Server
            "runserver",
        ]
        for command in commands:

            try:
                if command == "runserver":
                    self.stdout.write(
                        self.style.WARNING("Finish Created All Initial Data")
                    )
                    call_command(command)
                    break
                else:
                    call_command(command)
                    self.stdout.write(self.style.SUCCESS(f"Successfully {command}"))
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"{command} Failed  \n \t \t Error is: {e}")
                )

        # self.stdout.write(self.style.WARNING("Finish Created All Initial Data"))
