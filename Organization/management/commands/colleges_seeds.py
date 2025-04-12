from django.core.management.base import BaseCommand
from django.conf import settings
from os.path import join, exists
from os import makedirs

from App.tools import get_model_name_from_class
from Organization.models import College, University


class Command(BaseCommand):
    data = "Colleges"
    help = f"Creates initial {data} model"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        if not exists(
            join(settings.MEDIA_ROOT, "images", get_model_name_from_class(College))
        ):
            makedirs(
                join(settings.MEDIA_ROOT, "images", get_model_name_from_class(College))
            )

        colleges = [
            {
                "name": "College of Commerce",
                "university": 1,
                "translations": {
                    "ar_AS": "كليه تجاره",
                    "ar_EG": "كليه تجاره",
                    "en_US": "College of Commerce",
                    "fr_FR": "Collège de Commerce",
                    "tr_TR": "Ticaret Koleji",
                },
            },
        ]
        college_id = 1
        for college in colleges:
            try:
                college: "College" = College.objects.create(
                    name=college["name"],
                    university=University.objects.get(pk=college["university"]),
                    image=join(
                        "images",
                        get_model_name_from_class(College),
                        f"{college_id}.png",
                    ),
                    translations=college["translations"],
                )

                self.stdout.write(
                    self.style.SUCCESS(f"Successfully insert {self.data} > {college}")
                )
                college_id = college_id + 1
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed insert {self.data} > {college} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING(f"Finish Created initial {self.data}"))
