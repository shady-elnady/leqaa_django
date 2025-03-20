from django.core.management.base import BaseCommand
from django.conf import settings
from os.path import join, exists
from os import makedirs

from User.models import User, UserAlbum, Profile
from User.utils.enums import TITLES, GENDERS
from Currency.models import Currency
from Locale.models import Language


class Command(BaseCommand):
    help = "Create Initial Staff Load Data"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        IMAGES_ROOT = join(settings.MEDIA_ROOT, "images")

        staffs_albums_images_directory = join(IMAGES_ROOT, "Users Albums", "Staff")
        if not exists(staffs_albums_images_directory):
            makedirs(staffs_albums_images_directory)

        staffs_profile_images_directory = join(IMAGES_ROOT, "Avatars", "Staff")
        if not exists(staffs_profile_images_directory):
            makedirs(staffs_profile_images_directory)

        staff_list = [
            {
                "username": "Staff",
                "email": "staff@g.com",
                "password": "12345678",
                "Profile": {
                    "full_name": "شادى رافت سعد",
                    "national_id": "01232222222222",
                    "birth_date": None,
                    "title": TITLES.Doctor,
                    "gender": GENDERS.MALE,
                    "university_number": "01223222222222",
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
        for staff in staff_list:
            try:
                staff_instance: User = User.objects.create_staff(
                    username=staff["username"],
                    email=staff["email"],
                    password=staff["password"],
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully  Create Staff with Name > {staff['username']}"
                    )
                )
                try:
                    Profile.objects.update_or_create(
                        user=staff_instance,
                        defaults={
                            "avatar": join(
                                staffs_profile_images_directory,
                                f"{staff_instance.id}.png",
                            ),
                            "full_name": staff["Profile"]["full_name"],
                            "national_id": staff["Profile"]["national_id"],
                            "birth_date": staff["Profile"]["birth_date"],
                            "title": staff["Profile"]["title"],
                            "gender": staff["Profile"]["gender"],
                            "university_number": staff["Profile"]["university_number"],
                            "is_graduate": staff["Profile"]["is_graduate"],
                            "currency": Currency.objects.get(
                                pk=staff["Profile"]["currency"]
                            ),
                            "language": Language.objects.get(
                                pk=staff["Profile"]["language"]
                            ),
                            "contact_info": staff["Profile"]["contact_info"],
                        },
                    )
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Successfully  Create Staff Profile with Name > {staff['username']}"
                        )
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(
                            f"Failed Create Staff Profile with Name > {staff['username']} , \n \t Error is: \t \t{e}"
                        )
                    )
                for id in range(1, 3):
                    try:
                        UserAlbum.objects.create(
                            user=staff_instance,
                            photo=join(
                                staffs_albums_images_directory,
                                f"{staff_instance.id}",
                                f"{id}.png",
                            ),
                        )
                        self.stdout.write(
                            self.style.SUCCESS(
                                f"Successfully  Create Photo for Staff with Name > {staff_instance.username}"
                            )
                        )
                    except Exception as e:
                        self.stdout.write(
                            self.style.ERROR(
                                f"Failed Create Photo for Staff with Name > {staff_instance.username} , \n \t Error is: \t \t{e}"
                            )
                        )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed Create Staff with Name > {staff['username']} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING("Finish Initial Staff Load Data"))
