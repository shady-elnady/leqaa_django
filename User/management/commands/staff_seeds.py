from django.core.management.base import BaseCommand
from datetime import datetime
from os.path import join

from App.tools import get_model_name_from_class
from User.models import User, UserAlbum, Profile
from User.utils.enums import TITLES, GENDERS
from Currency.models import Currency
from Language.models import Language


class Command(BaseCommand):
    help = "Create Initial Staff Load Data"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        staff_list = [
            {
                "username": "موظف",
                "email": "staff@g.com",
                "password": "password",
                "Profile": {
                    "full_name": "الموظف الأول",
                    "national_id": "01232222222222",
                    "birth_date": datetime(1982, 5, 11),
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
                    profile, _ = Profile.objects.update_or_create(
                        user=staff_instance,
                        defaults={
                            "full_name": staff["Profile"]["full_name"],
                            "national_id": staff["Profile"]["national_id"],
                            "title": staff["Profile"]["title"],
                            "gender": staff["Profile"]["gender"],
                            "university_number": staff["Profile"]["university_number"],
                            "is_graduate": staff["Profile"]["is_graduate"],
                            "image": join(
                                "images",
                                get_model_name_from_class(Profile),
                                f"{staff_instance.id}.png",
                            ),
                            "currency": Currency.objects.get(
                                pk=staff["Profile"]["currency"]
                            ),
                            "language": Language.objects.get(
                                pk=staff["Profile"]["language"]
                            ),
                            "contact_info": staff["Profile"]["contact_info"],
                        },
                    )

                    profile.birth_date_property = staff["Profile"]["birth_date"]
                    profile.save()
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
                            image=join(
                                "images",
                                get_model_name_from_class(UserAlbum),
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
