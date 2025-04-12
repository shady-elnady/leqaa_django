from django.core.management.base import BaseCommand
from django.conf import settings
from os.path import join, exists
from os import makedirs

from App.tools.get_model_name import get_model_name_from_class
from Organization.models import University


class Command(BaseCommand):
    data = "Universities"
    help = f"Creates initial {data} model"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        if not exists(
            join(settings.MEDIA_ROOT, "images", get_model_name_from_class(University))
        ):
            makedirs(
                join(
                    settings.MEDIA_ROOT, "images", get_model_name_from_class(University)
                )
            )
        universities = [
            {
                "name": "Mansoura University",
                "email": 1,
                "translations": {
                    "ar_AS": "جامعه المنصوره",
                    "ar_EG": "جامعه المنصوره",
                    "en_US": "Mansoura University",
                    "fr_FR": "Université de Mansourah",
                    "tr_TR": "Mansoura Üniversitesi",
                },
            },
        ]
        university_id = 1
        for university in universities:
            try:
                University.objects.create(
                    name=university["name"],
                    image=join(
                        "images",
                        get_model_name_from_class(University),
                        f"{university_id}.png",
                    ),
                    email=university["email"],
                    translations=university["translations"],
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully insert {self.data} > {university}"
                    )
                )
                university_id = university_id + 1
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed insert {self.data} > {university} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING(f"Finish Created initial {self.data}"))
