from django.core.management.base import BaseCommand
from django.conf import settings
from os.path import join, exists
from os import makedirs

from User.models import User, UserAlbum, Profile
from User.utils.enums import TITLES, GENDERS
from Currency.models import Currency
from Locale.models import Language


class Command(BaseCommand):
    help = "Create Initial Super Users Load Data"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        IMAGES_ROOT = join(settings.MEDIA_ROOT, "images")

        superusers_albums_images_directory = join(
            IMAGES_ROOT, "Users Albums", "Super Users"
        )
        if not exists(superusers_albums_images_directory):
            makedirs(superusers_albums_images_directory)

        superusers_profile_images_directory = join(
            IMAGES_ROOT, "Avatars", "Super Users"
        )
        if not exists(superusers_profile_images_directory):
            makedirs(superusers_profile_images_directory)

        superusers = [
            {
                "username": "Shady",
                "email": "shady@g.com",
                "password": "12345678",
                "Profile": {
                    "full_name": "شادى رافت سعد",
                    "national_id": "02222222222222",
                    "birth_date": None,
                    "title": TITLES.Doctor,
                    "gender": GENDERS.MALE,
                    "university_number": "02222222222222",
                    "is_graduate": True,
                    "currency": 1,
                    "language": 1,
                    "contact_info": {
                        "Telephone": "+2 050 5060570",
                        "lat": 4.33333,
                        "lng": 4.33333,
                    },
                },
            },
        ]
        for superuser in superusers:
            try:
                superuser_instance: User = User.objects.create_superuser(
                    username=superuser["username"],
                    email=superuser["email"],
                    password=superuser["password"],
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully  CreateSuper User with Name > {superuser['username']}"
                    )
                )
                try:
                    Profile.objects.update_or_create(
                        user=superuser_instance,
                        defaults={
                            "avatar": join(
                                superusers_profile_images_directory,
                                f"{superuser_instance.id}.png",
                            ),
                            "full_name": superuser["Profile"]["full_name"],
                            "national_id": superuser["Profile"]["national_id"],
                            "birth_date": superuser["Profile"]["birth_date"],
                            "title": superuser["Profile"]["title"],
                            "gender": superuser["Profile"]["gender"],
                            "university_number": superuser["Profile"][
                                "university_number"
                            ],
                            "is_graduate": superuser["Profile"]["is_graduate"],
                            "currency": Currency.objects.get(
                                pk=superuser["Profile"]["currency"]
                            ),
                            "language": Language.objects.get(
                                pk=superuser["Profile"]["language"]
                            ),
                            "contact_info": superuser["Profile"]["contact_info"],
                        },
                    )
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Successfully  Create Super User Profile with Name > {superuser['username']}"
                        )
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(
                            f"Failed Create Super User Profile with Name > {superuser['username']} , \n \t Error is: \t \t{e}"
                        )
                    )
                for id in range(1, 3):
                    try:
                        UserAlbum.objects.create(
                            user=superuser_instance,
                            photo=join(
                                superusers_albums_images_directory,
                                f"{superuser_instance.id}",
                                f"{id}.png",
                            ),
                        )
                        self.stdout.write(
                            self.style.SUCCESS(
                                f"Successfully  Create Photo for Super User with Name > {superuser_instance.username}"
                            )
                        )
                    except Exception as e:
                        self.stdout.write(
                            self.style.ERROR(
                                f"Failed Create Photo forSuper User with Name > {superuser_instance.username} , \n \t Error is: \t \t{e}"
                            )
                        )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed Create Super User with Name > {superuser['username']} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING("Finish Initial Super Users Load Data"))
