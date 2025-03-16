from django.core.management.base import BaseCommand
from django.conf import settings
from os.path import join, exists
from os import makedirs

from Advertisement.models import Advertisement


class Command(BaseCommand):
    data = "Advertisements"
    help = f"Creates initial {data} model"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        IMAGES_ROOT = join(settings.MEDIA_ROOT, "images")

        categories_images_directory = join(IMAGES_ROOT, "Advertisements")
        if not exists(categories_images_directory):
            makedirs(categories_images_directory)

        advertisements = [
            {
                "title": "First",
                "url": "http://127.0.0.1:8000/en-us/admin/Advertisement/advertisement/1",
                "description": "First Advertisement Description",
            },
            {
                "title": "Second",
                "url": "http://127.0.0.1:8000/en-us/admin/Advertisement/advertisement/2",
                "description": "Second Advertisement Description",
            },
            {
                "title": "Third",
                "url": "http://127.0.0.1:8000/en-us/admin/Advertisement/advertisement/3",
                "description": "Third Advertisement Description",
            },
        ]
        advertisement_id = 1
        for advertisement in advertisements:
            try:
                Advertisement.objects.create(
                    title=advertisement["title"],
                    url=advertisement["url"],
                    description=advertisement["description"],
                    image=join(categories_images_directory, f"{advertisement_id}.png"),
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully insert {self.data} > {advertisement}"
                    )
                )
                advertisement_id = advertisement_id + 1
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed insert {self.data} > {advertisement} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING(f"Finish Created initial {self.data}"))
