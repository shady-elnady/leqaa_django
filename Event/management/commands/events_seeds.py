from datetime import datetime
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
from os.path import join, exists
from os import makedirs

from Category.models import Category
from Event.models import Event, EventAlbum, EventType
from Event.utils.enums import EventPaidStatus, LecturerFinancialSystem
from Organization.models import College, University, Organization
from User.models import Lecturer


class Command(BaseCommand):
    data = "Events"
    help = f"Creates initial {data} model"

    def handle(self, *args, **options):

        IMAGES_ROOT = join(settings.MEDIA_ROOT, "images")

        events_images_directory = join(IMAGES_ROOT, "Events")
        if not exists(events_images_directory):
            makedirs(events_images_directory)

        events_album_images_directory = join(IMAGES_ROOT, "Events_Albums")
        if not exists(events_album_images_directory):
            makedirs(events_album_images_directory)

        commands = [
            "eventTypes_seeds",
        ]
        for command in commands:
            try:
                call_command(command)
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully {command} Load Data")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Load Data Failed from {command} , \n \t Error is: \t \t{e}"
                    )
                )

        #########################

        events = [
            {
                # "image": "images/Events/1.png",
                "title": "الثقافه و الفنون",
                "hall": "Occasions",
                "event_type": 1,
                "category": 1,
                "lecturer": 1,
                "university": 1,
                "college": 1,
                "organizer": 1,
                "lecturer_financial_dues": None,
                "lecturer_financial_system": LecturerFinancialSystem.Enlist,
                "event_paid_status": EventPaidStatus.Free,
                "description": "تنظم جامعة المنصورة ملتقى التوظيف السنوي، وهو فعالية تهدف إلى تعزيز فرص العمل للخريجين وتهيئتهم لسوق العمل. يقام الملتقى تحت رعاية رئيس الجامعة د. شريف يوسف خاطر، ويشمل مشاركة العديد من الشركات والمؤسسات من مختلف القطاعات.الملتقى يوفر منصة للخريجين للتفاعل مع أصحاب العمل، والاستفادة من ورش العمل والجلسات النقاشية التي تركز على تنمية المهارات المهنية والشخصية، مما يعزز من فرص التوظيف الفعلية للخريجين.كما يتضمن الملتقى جلسات حول استراتيجيات التوظيف ورؤية مصر 2030، حيث يتم تناول موضوعات مثل المشروعات القومية ومدن الجيل الرابع، وريادة الأعمال، والدور المجتمعي لمؤسسات العمل  ويشمل مشاركة العديد من الشركات والمؤسسات من مختلف القطاعات",
                "start_date_time": datetime.strptime(
                    "2020-09-17T10:05",
                    "%Y-%m-%dT%H:%M",
                ),
                # "EventPhotosAlbum": [
                #     {
                #         "photo": "images/Events_Albums/1_0.png",
                #     },
                # ],
            },
            {
                # "image": "images/Events/2.png",
                "title": "ملتقى التوظيف",
                "hall": "Occasions",
                "event_type": 1,
                "category": 1,
                "lecturer": 1,
                "university": 1,
                "college": 1,
                "organizer": 1,
                "lecturer_financial_dues": None,
                "lecturer_financial_system": LecturerFinancialSystem.Enlist,
                "event_paid_status": EventPaidStatus.Free,
                "description": "تنظم جامعة المنصورة ملتقى التوظيف السنوي، وهو فعالية تهدف إلى تعزيز فرص العمل للخريجين وتهيئتهم لسوق العمل. يقام الملتقى تحت رعاية رئيس الجامعة د. شريف يوسف خاطر، ويشمل مشاركة العديد من الشركات والمؤسسات من مختلف القطاعات.الملتقى يوفر منصة للخريجين للتفاعل مع أصحاب العمل، والاستفادة من ورش العمل والجلسات النقاشية التي تركز على تنمية المهارات المهنية والشخصية، مما يعزز من فرص التوظيف الفعلية للخريجين.كما يتضمن الملتقى جلسات حول استراتيجيات التوظيف ورؤية مصر 2030، حيث يتم تناول موضوعات مثل المشروعات القومية ومدن الجيل الرابع، وريادة الأعمال، والدور المجتمعي لمؤسسات العمل  ويشمل مشاركة العديد من الشركات والمؤسسات من مختلف القطاعات",
                "start_date_time": datetime.strptime(
                    "2020-09-17T10:05",
                    "%Y-%m-%dT%H:%M",
                ),
                # "EventPhotosAlbum": [
                #     {
                #         "photo": "images/Events_Albums/2_0.png",
                #     },
                # ],
            },
            {
                # "image": "images/Events/3.png",
                "title": "لغه انجليزيه",
                "hall": "Occasions",
                "event_type": 2,
                "category": 1,
                "lecturer": 1,
                "university": 1,
                "college": 1,
                "organizer": 1,
                "lecturer_financial_dues": None,
                "lecturer_financial_system": LecturerFinancialSystem.Enlist,
                "event_paid_status": EventPaidStatus.Free,
                "description": "تنظم جامعة المنصورة ملتقى التوظيف السنوي، وهو فعالية تهدف إلى تعزيز فرص العمل للخريجين وتهيئتهم لسوق العمل. يقام الملتقى تحت رعاية رئيس الجامعة د. شريف يوسف خاطر، ويشمل مشاركة العديد من الشركات والمؤسسات من مختلف القطاعات.الملتقى يوفر منصة للخريجين للتفاعل مع أصحاب العمل، والاستفادة من ورش العمل والجلسات النقاشية التي تركز على تنمية المهارات المهنية والشخصية، مما يعزز من فرص التوظيف الفعلية للخريجين.كما يتضمن الملتقى جلسات حول استراتيجيات التوظيف ورؤية مصر 2030، حيث يتم تناول موضوعات مثل المشروعات القومية ومدن الجيل الرابع، وريادة الأعمال، والدور المجتمعي لمؤسسات العمل  ويشمل مشاركة العديد من الشركات والمؤسسات من مختلف القطاعات",
                "start_date_time": datetime.strptime(
                    "2020-09-17T10:05",
                    "%Y-%m-%dT%H:%M",
                ),
                # "EventPhotosAlbum": [
                #     {
                #         "photo": "images/Events_Albums/3_0.png",
                #     },
                # ],
            },
            {
                # "image": "images/Events/4.png",
                "title": "إداره موارد بشريه",
                "hall": "Occasions",
                "event_type": 2,
                "category": 1,
                "lecturer": 1,
                "university": 1,
                "college": 1,
                "organizer": 1,
                "lecturer_financial_dues": None,
                "lecturer_financial_system": LecturerFinancialSystem.Enlist,
                "event_paid_status": EventPaidStatus.Free,
                "description": "تنظم جامعة المنصورة ملتقى التوظيف السنوي، وهو فعالية تهدف إلى تعزيز فرص العمل للخريجين وتهيئتهم لسوق العمل. يقام الملتقى تحت رعاية رئيس الجامعة د. شريف يوسف خاطر، ويشمل مشاركة العديد من الشركات والمؤسسات من مختلف القطاعات.الملتقى يوفر منصة للخريجين للتفاعل مع أصحاب العمل، والاستفادة من ورش العمل والجلسات النقاشية التي تركز على تنمية المهارات المهنية والشخصية، مما يعزز من فرص التوظيف الفعلية للخريجين.كما يتضمن الملتقى جلسات حول استراتيجيات التوظيف ورؤية مصر 2030، حيث يتم تناول موضوعات مثل المشروعات القومية ومدن الجيل الرابع، وريادة الأعمال، والدور المجتمعي لمؤسسات العمل  ويشمل مشاركة العديد من الشركات والمؤسسات من مختلف القطاعات",
                "start_date_time": datetime.strptime(
                    "2020-09-17T10:05",
                    "%Y-%m-%dT%H:%M",
                ),
                # "EventPhotosAlbum": [
                #     {
                #         "photo": "images/Events_Albums/4_0.png",
                #     },
                # ],
            },
        ]
        id = 1
        for event in events:
            try:
                eventInstance: Event = Event.objects.create(
                    image=join(events_images_directory, f"{id}.png"),
                    title=event["title"],
                    hall=event["hall"],
                    event_type=EventType.objects.get(pk=event["event_type"]),
                    category=Category.objects.get(pk=event["category"]),
                    lecturer=Lecturer.objects.get(pk=event["lecturer"]),
                    university=University.objects.get(pk=event["university"]),
                    college=College.objects.get(pk=event["college"]),
                    organizer=Organization.objects.get(pk=event["organizer"]),
                    lecturer_financial_dues=event["lecturer_financial_dues"],
                    lecturer_financial_system=event["lecturer_financial_system"],
                    event_paid_status=event["event_paid_status"],
                    description=event["description"],
                    start_date_time=event["start_date_time"],
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully insert {self.data} > {eventInstance.title}"
                    )
                )
                for albumId in range(13):
                    try:
                        EventAlbum.objects.create(
                            event=eventInstance,
                            photo=join(
                                events_images_directory,
                                f"{eventInstance.id}_{albumId}.png",
                            ),
                        )
                        self.stdout.write(
                            self.style.SUCCESS(
                                f"Successfully insert Event Photo > {eventInstance.title}"
                            )
                        )
                    except Exception as ee:
                        self.stdout.write(
                            self.style.ERROR(
                                f"Failed insert Event Photo > {eventInstance.title} , \n \t Error is: \t \t{ee}"
                            )
                        )
                id = id + 1

            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed insert {self.data} > {event} , \n \t Error is: \t \t{e}"
                    )
                )

        self.stdout.write(self.style.WARNING(f"Finish Created initial {self.data}"))
