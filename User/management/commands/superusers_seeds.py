from django.core.management.base import BaseCommand
from datetime import datetime
from os.path import join

from App.tools.get_model_name import get_model_name_from_class
from User.models import User, UserAlbum, Profile
from User.utils.enums import TITLES, GENDERS
from Currency.models import Currency
from Language.models import Language


class Command(BaseCommand):
    help = "Create Initial Super Users Load Data"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        superusers = [
            {
                "username": "سوبريوزر",
                "email": "superuser@g.com",
                "password": "password",
                "Profile": {
                    "full_name": "سوبريوزر الأول",
                    "national_id": "02222222222222",
                    "birth_date": datetime(1981, 5, 11),
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
                        f"Successfully  Create Super User with Name > {superuser['username']}"
                    )
                )
                try:
                    profile, _ = Profile.objects.update_or_create(
                        user=superuser_instance,
                        defaults={
                            "full_name": superuser["Profile"]["full_name"],
                            "national_id": superuser["Profile"]["national_id"],
                            "title": superuser["Profile"]["title"],
                            "gender": superuser["Profile"]["gender"],
                            "university_number": superuser["Profile"][
                                "university_number"
                            ],
                            "image": join(
                                "images",
                                get_model_name_from_class(Profile),
                                f"{str(superuser_instance.id)}.png",
                            ),
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
                    profile.birth_date_property = superuser["Profile"]["birth_date"]
                    profile.save()
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
                            image=join(
                                "images",
                                get_model_name_from_class(UserAlbum),
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
                raise
        self.stdout.write(self.style.WARNING("Finish Initial Super Users Load Data"))
