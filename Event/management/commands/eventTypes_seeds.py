from django.core.management.base import BaseCommand
from django.conf import settings
from os.path import join, exists
from os import makedirs

from Event.models import EventType


class Command(BaseCommand):
    data = "Event Types"
    help = f"Creates initial {data} model"

    def handle(self, *args, **options):

        IMAGES_ROOT = join(settings.MEDIA_ROOT, "images")

        event_types_images_directory = join(IMAGES_ROOT, "Event_Types")
        if not exists(event_types_images_directory):
            makedirs(event_types_images_directory)

        eventTypes = [
            {
                "name": "Occasions",
                # "image": "images/Event_Types/1.png",
                "translations": {
                    "ar-AS": "مناسبات",
                    "ar-EG": "مناسبات",
                    "en-US": "Occasions",
                    "fr-FR": "Occasions",
                    "tr-TR": "Fırsatlar",
                },
            },
            {
                "name": "Courses",
                # "image": "images/Event_Types/2.png",
                "translations": {
                    "ar-AS": "كورسات",
                    "ar-EG": "كورسات",
                    "en-US": "Courses",
                    "fr-FR": "Cours",
                    "tr-TR": "Kurslar",
                },
            },
            {
                "name": "Traning",
                # "image": "images/Event_Types/3.png",
                "translations": {
                    "ar-AS": "تدريب",
                    "ar-EG": "تدريب",
                    "en-US": "Traning",
                    "fr-FR": "Formation",
                    "tr-TR": "Eğitim",
                },
            },
        ]
        id = 1
        for eventType in eventTypes:
            try:
                EventType.objects.create(
                    name=eventType["name"],
                    image=join(event_types_images_directory, f"{id}.png"),
                    translations=eventType["translations"],
                )
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully insert {self.data} > {eventType}")
                )
                id = id + 1
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed insert {self.data} > {eventType} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING(f"Finish Created initial {self.data}"))
