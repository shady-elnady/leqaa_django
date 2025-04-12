from django.core.management.base import BaseCommand
from django.conf import settings
from os.path import join, exists
from os import makedirs

from Advertisement.models import Advertisement
from App.tools import get_model_name_from_class


class Command(BaseCommand):
    data = "Advertisements"
    help = f"Creates initial {data} model"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        if not exists(
            join(
                settings.MEDIA_ROOT, "images", get_model_name_from_class(Advertisement)
            )
        ):
            makedirs(
                join(
                    settings.MEDIA_ROOT,
                    "images",
                    get_model_name_from_class(Advertisement),
                )
            )

        advertisements = [
            {
                "title": "First",
                "advertisement_url": "http://127.0.0.1:8000/admin/Advertisement/advertisement/1",
                "description": "First Advertisement Description",
            },
            {
                "title": "Second",
                "advertisement_url": "http://127.0.0.1:8000/admin/Advertisement/advertisement/2",
                "description": "Second Advertisement Description",
            },
            {
                "title": "Third",
                "advertisement_url": "http://127.0.0.1:8000/admin/Advertisement/advertisement/3",
                "description": "Third Advertisement Description",
            },
        ]
        advertisement_id = 1
        for advertisement in advertisements:
            try:
                Advertisement.objects.create(
                    title=advertisement["title"],
                    advertisement_url=advertisement["advertisement_url"],
                    description=advertisement["description"],
                    image=join(
                        "images",
                        get_model_name_from_class(Advertisement),
                        f"{advertisement_id}.png",
                    ),
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully insert {self.data} > {advertisement}"
                    )
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed insert {self.data} > {advertisement} , \n \t Error is: \t \t{e}"
                    )
                )

            advertisement_id = advertisement_id + 1

        self.stdout.write(self.style.WARNING(f"Finish Created initial {self.data}"))
