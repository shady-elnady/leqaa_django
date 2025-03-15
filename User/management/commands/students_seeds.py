from django.core.management.base import BaseCommand
from os.path import join

from User.models import User, UserAlbum, Profile
from User.utils.enums import USERS_TYPES, TITLES, GENDERS
from Currency.models import Currency
from Locale.models import Language


class Command(BaseCommand):
    help = "Create Initial Students Load Data"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        users = [
            {
                "username": "شادى رأفت",
                "user_type": USERS_TYPES.Student,
                "email": "shadyelnady1@gmail.com",
                "mobile": "+01022222222",
                "password": "password",
                "Profile": {
                    # "avatar": "Images/Users/3/Avatar_3.png",
                    "full_name": "شادى رافت سعد النادى",
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
                # "UserPhotosAlbum": [
                #     {
                #         "photo": "Images/Users/3/3_3.png",
                #     },
                #     {
                #         "photo": "Images/Users/3/3_4.png",
                #     },
                # ],
            },
        ]
        for user in users:
            try:
                userInstance: User = User.objects.create_user(
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
                        user=userInstance,
                        defaults={
                            "avatar": join(
                                "images",
                                "Users",
                                f"{userInstance.id}",
                                f"Avatar_{userInstance.id}.png",
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
                for id in range(2):
                    try:
                        UserAlbum.objects.create(
                            user=userInstance,
                            photo=join(
                                "images",
                                "Users",
                                f"{userInstance.id}",
                                f"{userInstance.id}_{id}.png",
                            ),
                        )
                        self.stdout.write(
                            self.style.SUCCESS(
                                f"Successfully  Create Photo for Student with Name > {userInstance.username}"
                            )
                        )
                    except Exception as e:
                        self.stdout.write(
                            self.style.ERROR(
                                f"Failed Create Photo for Student with Name > {userInstance.username} , \n \t Error is: \t \t{e}"
                            )
                        )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed Create Student with Name > {user['username']} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING("Finish Initial Students Load Data"))
