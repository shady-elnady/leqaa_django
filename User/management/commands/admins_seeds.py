from django.core.management.base import BaseCommand
from datetime import datetime
from os.path import join

from App.tools import get_model_name_from_class
from User.models import User, UserAlbum, Profile
from User.utils.enums import TITLES, GENDERS
from Currency.models import Currency
from Language.models import Language


class Command(BaseCommand):
    help = "Create Initial Admins Load Data"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        admins = [
            {
                "username": "الأدمن",
                "email": "admin@g.com",
                "password": "password",
                "Profile": {
                    "full_name": "الأدمن الأول",
                    "national_id": "01222222222222",
                    "birth_date": datetime(1982, 5, 11),
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
                    profile, _ = Profile.objects.update_or_create(
                        user=admin_instance,
                        defaults={
                            "full_name": admin["Profile"]["full_name"],
                            "national_id": admin["Profile"]["national_id"],
                            "title": admin["Profile"]["title"],
                            "gender": admin["Profile"]["gender"],
                            "university_number": admin["Profile"]["university_number"],
                            "is_graduate": admin["Profile"]["is_graduate"],
                            "image": join(
                                "images",
                                get_model_name_from_class(Profile),
                                f"{admin_instance.id}.png",
                            ),
                            "currency": Currency.objects.get(
                                pk=admin["Profile"]["currency"]
                            ),
                            "language": Language.objects.get(
                                pk=admin["Profile"]["language"]
                            ),
                            "contact_info": admin["Profile"]["contact_info"],
                        },
                    )

                    profile.birth_date_property = admin["Profile"]["birth_date"]
                    profile.save()
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
                            image=join(
                                "images",
                                get_model_name_from_class(UserAlbum),
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
