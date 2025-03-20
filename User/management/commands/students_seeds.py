from django.core.management.base import BaseCommand
from django.conf import settings
from os.path import join, exists
from os import makedirs

from User.models import User, UserAlbum, Profile
from User.utils.enums import USERS_TYPES, TITLES, GENDERS
from Currency.models import Currency
from Locale.models import Language


class Command(BaseCommand):
    help = "Create Initial Students Load Data"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        IMAGES_ROOT = join(settings.MEDIA_ROOT, "images")

        students_albums_images_directory = join(IMAGES_ROOT, "Users Albums", "Students")
        if not exists(students_albums_images_directory):
            makedirs(students_albums_images_directory)

        students_profile_images_directory = join(IMAGES_ROOT, "Avatars", "Students")
        if not exists(students_profile_images_directory):
            makedirs(students_profile_images_directory)

        users = [
            {
                "username": "طارق الجيد",
                "user_type": USERS_TYPES.Student,
                "email": "shadyelnady1@g.com",
                "mobile": "+201022222222",
                "password": "password",
                "Profile": {
                    "full_name": "طارق أحمد محمود الجيد",
                    "national_id": "22222222222222",
                    "birth_date": None,
                    "title": TITLES.Student,
                    "gender": GENDERS.MALE,
                    "university_number": "22222222222222",
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
                        f"Successfully  Create User with Name > {user['username']}"
                    )
                )
                try:
                    Profile.objects.update_or_create(
                        user=user_instance,
                        defaults={
                            "avatar": join(
                                students_profile_images_directory,
                                f"{user_instance.id}.png",
                            ),
                            "full_name": user["Profile"]["full_name"],
                            "national_id": user["Profile"]["national_id"],
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
                            f"Successfully  Create Student Profile with Name > {user['username']}"
                        )
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(
                            f"Failed Create Student Profile with Name > {user['username']} , \n \t Error is: \t \t{e}"
                        )
                    )
                for id in range(1, 3):
                    try:
                        UserAlbum.objects.create(
                            user=user_instance,
                            photo=join(
                                students_albums_images_directory,
                                f"{user_instance.id}",
                                f"{id}.png",
                            ),
                        )
                        self.stdout.write(
                            self.style.SUCCESS(
                                f"Successfully  Create Photo for Student with Name > {user_instance.username}"
                            )
                        )
                    except Exception as e:
                        self.stdout.write(
                            self.style.ERROR(
                                f"Failed Create Photo for Student with Name > {user_instance.username} , \n \t Error is: \t \t{e}"
                            )
                        )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed Create Student with Name > {user['username']} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING("Finish Initial Students Load Data"))
