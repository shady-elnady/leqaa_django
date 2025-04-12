from django.core.management.base import BaseCommand
from datetime import datetime
from os.path import join

from App.tools.get_model_name import get_model_name_from_class
from Currency.models import Currency
from Language.models import Language
from User.models import User, UserAlbum, Profile
from User.utils.enums import USERS_TYPES, TITLES, GENDERS


class Command(BaseCommand):
    help = "Create Initial Lecturers Load Data"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        users = [
            {
                "username": "المحاضر",
                "user_type": USERS_TYPES.Lecturer,
                "email": "lecturer@g.com",
                "mobile": "+201011111111",
                "password": "password",
                "Profile": {
                    "full_name": "المحاضر الأول",
                    "national_id": "11116111511111",
                    "birth_date": datetime(1981, 5, 11),
                    "title": TITLES.Doctor,
                    "gender": GENDERS.MALE,
                    "university_number": "11116111511111",
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
                    email=user["email"],
                    password=user["password"],
                    user_type=user["user_type"],
                    mobile=user["mobile"],
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully  Create Lecturer with Name > {user['username']}"
                    )
                )
                try:
                    profile, _ = Profile.objects.update_or_create(
                        user=user_instance,
                        defaults={
                            "national_id": user["Profile"]["national_id"],
                            "full_name": user["Profile"]["full_name"],
                            "birth_date": user["Profile"]["birth_date"],
                            "title": user["Profile"]["title"],
                            "gender": user["Profile"]["gender"],
                            "university_number": user["Profile"]["university_number"],
                            "is_graduate": user["Profile"]["is_graduate"],
                            "image": join(
                                "images",
                                get_model_name_from_class(Profile),
                                f"{user_instance.id}.png",
                            ),
                            "currency": Currency.objects.get(
                                pk=user["Profile"]["currency"]
                            ),
                            "language": Language.objects.get(
                                pk=user["Profile"]["language"]
                            ),
                            "contact_info": user["Profile"]["contact_info"],
                        },
                    )
                    profile.birth_date_property = user["Profile"]["birth_date"]
                    profile.save()
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
                            image=join(
                                "images",
                                get_model_name_from_class(UserAlbum),
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
