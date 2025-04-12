from django.core.management.base import BaseCommand
from datetime import datetime
from os.path import join

from App.tools import get_model_name_from_class
from Category.models import Category
from User.models import User, UserAlbum, Profile, Interest
from User.utils.enums import USERS_TYPES, TITLES, GENDERS
from Currency.models import Currency
from Language.models import Language


class Command(BaseCommand):
    help = "Create Initial Students Load Data"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        users = [
            {
                "username": "طالب",
                "user_type": USERS_TYPES.Student,
                "email": "student@g.com",
                "mobile": "+201022222222",
                "password": "password12345678",
                "Profile": {
                    "full_name": "الطالب الأول",
                    "national_id": "22222222422222",
                    "birth_date": datetime(1982, 5, 11),
                    "title": TITLES.Student,
                    "gender": GENDERS.MALE,
                    "university_number": "22222222422222",
                    "is_graduate": True,
                    "currency": 1,
                    "language": 1,
                    "contact_info": {
                        "Telephone": "+2 050 5060570",
                        "lat": 4.33333,
                        "lng": 4.33333,
                    },
                },
                "interesting_notifiable_categories": [
                    1,
                    2,
                ],
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
                        f"Successfully  Create User with Name > {user['username']}"
                    )
                )

                ##################################### User Profile ########################################
                try:
                    profile, _ = Profile.objects.update_or_create(
                        user=user_instance,
                        defaults={
                            "full_name": user["Profile"]["full_name"],
                            "national_id": user["Profile"]["national_id"],
                            "birth_date": user["Profile"]["birth_date"],
                            "title": user["Profile"]["title"],
                            "gender": user["Profile"]["gender"],
                            "university_number": user["Profile"]["university_number"],
                            "is_graduate": user["Profile"]["is_graduate"],
                            "image": join(
                                "images",
                                get_model_name_from_class(Profile),
                                f"{str(user_instance.uid)}.png",
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
                            f"Successfully  Create Student Profile with Name > {user['username']}"
                        )
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(
                            f"Failed Create Student Profile with Name > {user['username']} , \n \t Error is: \t \t{e}"
                        )
                    )
                ##################################### interesting_notifiable_categories ########################################
                for category_id in user["interesting_notifiable_categories"]:
                    try:
                        Interest.objects.update_or_create(
                            user=user_instance,
                            defaults={
                                "category": Category.objects.get(pk=category_id),
                                "is_notifiable": True,
                            },
                        )
                        self.stdout.write(
                            self.style.SUCCESS(
                                f"Successfully  Create Student Interest with Name > {user['username']}"
                            )
                        )
                    except Exception as e:
                        self.stdout.write(
                            self.style.ERROR(
                                f"Failed Create Student Interest with Name > {user['username']} , \n \t Error is: \t \t{e}"
                            )
                        )

                ##################################### User Album ########################################
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
