from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
from os.path import join, exists
from os import makedirs

from App.tools.get_model_name import get_model_name_from_class
from User.models import UserAlbum, Profile


class Command(BaseCommand):
    help = "Creates initial Users Load Data"

    def handle(self, *args, **options):

        if not exists(
            join(settings.MEDIA_ROOT, "images", get_model_name_from_class(Profile))
        ):
            makedirs(
                join(settings.MEDIA_ROOT, "images", get_model_name_from_class(Profile))
            )
        if not exists(
            join(settings.MEDIA_ROOT, "images", get_model_name_from_class(UserAlbum))
        ):
            makedirs(
                join(
                    settings.MEDIA_ROOT, "images", get_model_name_from_class(UserAlbum)
                )
            )

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        commands = [
            "superusers_seeds",
            "admins_seeds",
            "staff_seeds",
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
