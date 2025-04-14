from django.core.management.base import BaseCommand
from django.conf import settings
from os.path import join, exists
from os import makedirs

from App.tools import get_model_name_from_class
from Event.models import EventType


class Command(BaseCommand):
    data = "Event Types"
    help = f"Creates initial {data} model"

    def handle(self, *args, **options):

        if not exists(
            join(settings.MEDIA_ROOT, "images", get_model_name_from_class(EventType))
        ):
            makedirs(
                join(
                    settings.MEDIA_ROOT, "images", get_model_name_from_class(EventType)
                )
            )

        event_types = [
            {
                "name": "Occasions",
                # "image": "images/Event_Types/1.png",
                "translations": {
                    "ar-as": "مناسبات",
                    "ar-eg": "مناسبات",
                    "en-us": "Occasions",
                    "fr-fr": "Occasions",
                    "tr-tr": "Fırsatlar",
                },
            },
            {
                "name": "Courses",
                # "image": "images/Event_Types/2.png",
                "translations": {
                    "ar-as": "كورسات",
                    "ar-eg": "كورسات",
                    "en-us": "Courses",
                    "fr-fr": "Cours",
                    "tr-tr": "Kurslar",
                },
            },
            {
                "name": "Traning",
                # "image": "images/Event_Types/3.png",
                "translations": {
                    "ar-as": "تدريب",
                    "ar-eg": "تدريب",
                    "en-us": "Traning",
                    "fr-fr": "Formation",
                    "tr-tr": "Eğitim",
                },
            },
        ]
        event_type_id = 1
        for event_type in event_types:
            try:
                EventType.objects.create(
                    name=event_type["name"],
                    image=join(
                        "images",
                        get_model_name_from_class(EventType),
                        f"{event_type_id}.png",
                    ),
                    translations=event_type["translations"],
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully insert {self.data} > {event_type}"
                    )
                )
                event_type_id = event_type_id + 1
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed insert {self.data} > {event_type} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING(f"Finish Created initial {self.data}"))
