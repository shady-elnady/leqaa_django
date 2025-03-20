from django.core.management.base import BaseCommand
from django.conf import settings
from os.path import join, exists
from os import makedirs

from User.models import User, UserAlbum, Profile
from User.utils.enums import TITLES, GENDERS
from Currency.models import Currency
from Locale.models import Language


class Command(BaseCommand):
    help = "Create Initial Admins Load Data"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        IMAGES_ROOT = join(settings.MEDIA_ROOT, "images")

        admins_albums_images_directory = join(IMAGES_ROOT, "Users Albums", "Admins")
        if not exists(admins_albums_images_directory):
            makedirs(admins_albums_images_directory)

        admins_profile_images_directory = join(IMAGES_ROOT, "Avatars", "Admins")
        if not exists(admins_profile_images_directory):
            makedirs(admins_profile_images_directory)

        admins = [
            {
                "username": "Admin",
                "email": "admin@g.com",
                "password": "12345678",
                "Profile": {
                    "full_name": "شادى رافت سعد",
                    "national_id": "01222222222222",
                    "birth_date": None,
                    "title": TITLES.Doctor,
                    "gender": GENDERS.MALE,
                    "university_number": "01222222222222",
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
        for admin in admins:
            try:
                admin_instance: User = User.objects.create_admin(
                    username=admin["username"],
                    email=admin["email"],
                    password=admin["password"],
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully  Create Admin with Name > {admin['username']}"
                    )
                )
                try:
                    Profile.objects.update_or_create(
                        user=admin_instance,
                        defaults={
                            "avatar": join(
                                admins_profile_images_directory,
                                f"{admin_instance.id}.png",
                            ),
                            "full_name": admin["Profile"]["full_name"],
                            "national_id": admin["Profile"]["national_id"],
                            "birth_date": admin["Profile"]["birth_date"],
                            "title": admin["Profile"]["title"],
                            "gender": admin["Profile"]["gender"],
                            "university_number": admin["Profile"]["university_number"],
                            "is_graduate": admin["Profile"]["is_graduate"],
                            "currency": Currency.objects.get(
                                pk=admin["Profile"]["currency"]
                            ),
                            "language": Language.objects.get(
                                pk=admin["Profile"]["language"]
                            ),
                            "contact_info": admin["Profile"]["contact_info"],
                        },
                    )
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Successfully  Create AdminProfile with Name > {admin['username']}"
                        )
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(
                            f"Failed Create Admin Profile with Name > {admin['username']} , \n \t Error is: \t \t{e}"
                        )
                    )
                for id in range(1, 3):
                    try:
                        UserAlbum.objects.create(
                            user=admin_instance,
                            photo=join(
                                admins_albums_images_directory,
                                f"{admin_instance.id}",
                                f"{id}.png",
                            ),
                        )
                        self.stdout.write(
                            self.style.SUCCESS(
                                f"Successfully  Create Photo for Admin with Name > {admin_instance.username}"
                            )
                        )
                    except Exception as e:
                        self.stdout.write(
                            self.style.ERROR(
                                f"Failed Create Photo for Admin with Name > {admin_instance.username} , \n \t Error is: \t \t{e}"
                            )
                        )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed Create Admin with Name > {admin['username']} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING("Finish Initial Admins Load Data"))
