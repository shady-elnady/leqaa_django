from django.core.management.base import BaseCommand
from django.conf import settings
from os.path import join, exists
from os import makedirs

from Organization.models import University


class Command(BaseCommand):
    data = "Universities"
    help = f"Creates initial {data} model"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        IMAGES_ROOT = join(settings.MEDIA_ROOT, "images")

        universities_images_directory = join(IMAGES_ROOT, "Universities")
        if not exists(universities_images_directory):
            makedirs(universities_images_directory)

        universities = [
            {
                "name": "Mansoura University",
                # "logo": "images/Universities/1.png",
                "email": 1,
                "translations": {
                    "ar-AS": "جامعه المنصوره",
                    "ar-EG": "جامعه المنصوره",
                    "en-US": "Mansoura University",
                    "fr-FR": "Université de Mansourah",
                    "tr-TR": "Mansoura Üniversitesi",
                },
            },
        ]
        id = 1
        for university in universities:
            try:
                University.objects.create(
                    name=university["name"],
                    logo=join(universities_images_directory, f"{id}.png"),
                    email=university["email"],
                    translations=university["translations"],
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully insert {self.data} > {university}"
                    )
                )
                id = id + 1
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed insert {self.data} > {university} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING(f"Finish Created initial {self.data}"))
