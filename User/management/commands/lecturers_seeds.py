from django.core.management.base import BaseCommand
from django.conf import settings
from os.path import join, exists
from os import makedirs

from Currency.models import Currency
from Locale.models import Language
from User.models import User, UserAlbum, Profile
from User.utils.enums import USERS_TYPES, TITLES, GENDERS


class Command(BaseCommand):
    help = "Create Initial Lecturers Load Data"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        IMAGES_ROOT = join(settings.MEDIA_ROOT, "images")

        lecturers_albums_images_directory = join(
            IMAGES_ROOT, "Users Albums", "Lecturers"
        )
        if not exists(lecturers_albums_images_directory):
            makedirs(lecturers_albums_images_directory)

        lecturers_profile_images_directory = join(IMAGES_ROOT, "Avatars", "Lecturers")
        if not exists(lecturers_profile_images_directory):
            makedirs(lecturers_profile_images_directory)

        users = [
            {
                "username": "أحمد محمود",
                "user_type": USERS_TYPES.Lecturer,
                "email": "shadyelnady0@g.com",
                "mobile": "+201011111111",
                "password": "password",
                "Profile": {
                    "full_name": "أحمد محمود محمد أحمد",
                    "national_id": "11111111111111",
                    "birth_date": None,
                    "title": TITLES.Doctor,
                    "gender": GENDERS.MALE,
                    "university_number": "11111111111111",
                    "is_graduate": False,
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
        for user in users:
            try:
                user_instance: User = User.objects.create_user(
                    username=user["username"],
                    user_type=user["user_type"],
                    email=user["email"],
                    mobile=user["mobile"],
                    password=user["password"],
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully  Create Lecturer with Name > {user['username']}"
                    )
                )
                try:
                    Profile.objects.update_or_create(
                        user=user_instance,
                        defaults={
                            "avatar": join(
                                lecturers_profile_images_directory,
                                f"{user_instance.id}.png",
                            ),
                            "national_id": user["Profile"]["national_id"],
                            "full_name": user["Profile"]["full_name"],
                            "birth_date": user["Profile"]["birth_date"],
                            "title": user["Profile"]["title"],
                            "gender": user["Profile"]["gender"],
                            "university_number": user["Profile"]["university_number"],
                            "is_graduate": user["Profile"]["is_graduate"],
                            "currency": Currency.objects.get(
                                pk=user["Profile"]["currency"]
                            ),
                            "language": Language.objects.get(
                                pk=user["Profile"]["language"]
                            ),
                            "contact_info": user["Profile"]["contact_info"],
                        },
                    )
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Successfully  Create Lecturer Profile with Name > {user['username']}"
                        )
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(
                            f"Failed Create Lecturer Profile with Name > {user['username']} , \n \t Error is: \t \t{e}"
                        )
                    )
                for id in range(1, 3):
                    try:
                        UserAlbum.objects.create(
                            user=user_instance,
                            photo=join(
                                lecturers_albums_images_directory,
                                f"{user_instance.id}",
                                f"{id}.png",
                            ),
                        )
                        self.stdout.write(
                            self.style.SUCCESS(
                                f"Successfully  Create Photo for Lecturer with Name > {user_instance.username}"
                            )
                        )
                    except Exception as e:
                        self.stdout.write(
                            self.style.ERROR(
                                f"Failed Create Photo for Lecturer with Name > {user_instance.username} , \n \t Error is: \t \t{e}"
                            )
                        )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed Create User with Name > {user['username']} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING("Finish Initial Lecturers Load Data"))
