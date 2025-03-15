from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
from os.path import join, exists
from os import makedirs


class Command(BaseCommand):
    help = "Creates initial Users Load Data"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        IMAGES_ROOT = join(settings.MEDIA_ROOT, "images")

        users_images_directory = join(IMAGES_ROOT, "Users")
        if not exists(users_images_directory):
            makedirs(users_images_directory)

        commands = [
            "lecturers_seeds",
            "students_seeds",
        ]

        for command in commands:
            try:
                call_command(command)
                self.stdout.write(self.style.SUCCESS(f"Successfully {command}"))
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"{command} Failed  \n \t \t Error is: {e}")
                )
        self.stdout.write(self.style.SUCCESS("Successfully Created Users Initial Data"))
