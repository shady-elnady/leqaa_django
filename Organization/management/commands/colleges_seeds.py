from django.core.management.base import BaseCommand
from django.conf import settings
from os.path import join, exists
from os import makedirs

from Organization.models import College, University


class Command(BaseCommand):
    data = "Colleges"
    help = f"Creates initial {data} model"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        IMAGES_ROOT = join(settings.MEDIA_ROOT, "images")

        colleges_images_directory = join(IMAGES_ROOT, "Colleges")
        if not exists(colleges_images_directory):
            makedirs(colleges_images_directory)

        colleges = [
            {
                "name": "College of Commerce",
                "university": 1,
                "translations": {
                    "ar-AS": "كليه تجاره",
                    "ar-EG": "كليه تجاره",
                    "en-US": "College of Commerce",
                    "fr-FR": "Collège de Commerce",
                    "tr-TR": "Ticaret Koleji",
                },
            },
        ]
        college_id = 1
        for college in colleges:
            try:
                College.objects.create(
                    name=college["name"],
                    logo=join(colleges_images_directory, f"{college_id}.png"),
                    university=University.objects.get(pk=college["university"]),
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
