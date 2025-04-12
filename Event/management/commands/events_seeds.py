from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.utils import timezone
from django.conf import settings
from os.path import join, exists
from os import makedirs
from datetime import datetime

from Address.models import Location
from App.tools import get_model_name_from_class
from Category.models import Category
from Event.models import Event, EventAlbum, EventType
from Event.utils.enums import EventPaidStatus, LecturerFinancialSystem
from Organization.models import College, University, Organization
from User.models import Lecturer


class Command(BaseCommand):
    data = "Events"
    help = f"Creates initial {data} model"

    def handle(self, *args, **options):
        COUNT_EVENTS_HAS_ALBUM: int = 3

        if not exists(
            join(settings.MEDIA_ROOT, "images", get_model_name_from_class(Event))
        ):
            makedirs(
                join(settings.MEDIA_ROOT, "images", get_model_name_from_class(Event))
            )

        if not exists(
            join(settings.MEDIA_ROOT, "images", get_model_name_from_class(EventType))
        ):
            makedirs(
                join(
                    settings.MEDIA_ROOT, "images", get_model_name_from_class(EventType)
                )
            )

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

        DESCRIPTTION = "تنظم جامعة المنصورة ملتقى التوظيف السنوي، وهو فعالية تهدف إلى تعزيز فرص العمل للخريجين وتهيئتهم لسوق العمل. يقام الملتقى تحت رعاية رئيس الجامعة د. شريف يوسف خاطر، ويشمل مشاركة العديد من الشركات والمؤسسات من مختلف القطاعات.الملتقى يوفر منصة للخريجين للتفاعل مع أصحاب العمل، والاستفادة من ورش العمل والجلسات النقاشية التي تركز على تنمية المهارات المهنية والشخصية، مما يعزز من فرص التوظيف الفعلية للخريجين.كما يتضمن الملتقى جلسات حول استراتيجيات التوظيف ورؤية مصر 2030، حيث يتم تناول موضوعات مثل المشروعات القومية ومدن الجيل الرابع، وريادة الأعمال، والدور المجتمعي لمؤسسات العمل  ويشمل مشاركة العديد من الشركات والمؤسسات من مختلف القطاعات"

        OTHER_DESCRIPTTION = "ملتقى البحث العلمي هو حدث يعرض فيه الطلاب والباحثون أبحاثهم، ويهدف إلى تعزيز التفاعل الأكاديمي وتطوير المهارات البحثية."

        events = [
            {
                "title": "الثقافه و الفنون",
                "hall": "Occasions",
                "event_type": 1,
                "category": 1,
                "lecturer": 1,
                "university": 1,
                "college": 1,
                "organizer": 1,
                "location": 1,
                "lecturer_financial_dues": None,
                "lecturer_financial_system": LecturerFinancialSystem.Enlist,
                "event_paid_status": EventPaidStatus.Free,
                "description": DESCRIPTTION,
                "start_date_time": datetime(2022, 4, 17, 10, 5, 0),
                "end_date_time": datetime(2022, 5, 17, 10, 5, 0),
            },
            {
                "title": "ملتقى التوظيف",
                "hall": "Occasions",
                "event_type": 1,
                "category": 1,
                "lecturer": 1,
                "university": 1,
                "college": 1,
                "organizer": 1,
                "location": 3,
                "lecturer_financial_dues": None,
                "lecturer_financial_system": LecturerFinancialSystem.Enlist,
                "event_paid_status": EventPaidStatus.Free,
                "description": DESCRIPTTION,
                "start_date_time": datetime(2024, 4, 17, 10, 5, 0),
                "end_date_time": datetime(2024, 5, 17, 10, 5, 0),
            },
            {
                "title": "لغه انجليزيه",
                "hall": "Occasions",
                "event_type": 2,
                "category": 1,
                "lecturer": 1,
                "university": 1,
                "college": 1,
                "organizer": 1,
                "location": 1,
                "lecturer_financial_dues": None,
                "lecturer_financial_system": LecturerFinancialSystem.Enlist,
                "event_paid_status": EventPaidStatus.Free,
                "description": DESCRIPTTION,
                "start_date_time": datetime(2025, 4, 17, 10, 5, 0),
                "end_date_time": datetime(2025, 5, 17, 10, 5, 0),
            },
            {
                "title": "إداره موارد بشريه",
                "hall": "Occasions",
                "event_type": 2,
                "category": 1,
                "lecturer": 1,
                "university": 1,
                "college": 1,
                "organizer": 1,
                "location": 1,
                "lecturer_financial_dues": None,
                "lecturer_financial_system": LecturerFinancialSystem.Enlist,
                "event_paid_status": EventPaidStatus.Free,
                "description": DESCRIPTTION,
                "start_date_time": datetime(2026, 4, 17, 10, 5, 0),
                "end_date_time": datetime(2026, 5, 17, 10, 5, 0),
            },
            {
                "title": "ملتقي البحث العلمي",
                "hall": "Occasions",
                "event_type": 2,
                "category": 1,
                "lecturer": 1,
                "university": 1,
                "college": 1,
                "organizer": 3,
                "location": 2,
                "lecturer_financial_dues": None,
                "lecturer_financial_system": LecturerFinancialSystem.Enlist,
                "event_paid_status": EventPaidStatus.Free,
                "description": OTHER_DESCRIPTTION,
                "start_date_time": datetime(2027, 4, 17, 10, 5, 0),
                "end_date_time": datetime(2027, 5, 17, 10, 5, 0),
            },
        ]
        event_id = 1
        for event in events:
            try:
                event_instance: Event = Event.objects.create(
                    image=join(
                        "images",
                        get_model_name_from_class(Event),
                        f"{event_id}.png",
                    ),
                    title=event["title"],
                    hall=event["hall"],
                    event_type=EventType.objects.get(pk=event["event_type"]),
                    category=Category.objects.get(pk=event["category"]),
                    lecturer=Lecturer.objects.get(pk=event["lecturer"]),
                    university=University.objects.get(pk=event["university"]),
                    college=College.objects.get(pk=event["college"]),
                    organizer=Organization.objects.get(pk=event["organizer"]),
                    location=Location.objects.get(pk=event["organizer"]),
                    lecturer_financial_dues=event["lecturer_financial_dues"],
                    lecturer_financial_system=event["lecturer_financial_system"],
                    event_paid_status=event["event_paid_status"],
                    complete_description=event["description"],
                    short_description=event["description"],
                    registration_link="https://www.google.com/",
                    start_date_time=timezone.make_aware(
                        event["start_date_time"]
                    ),  # Convert to timezone-aware,
                    end_date_time=timezone.make_aware(
                        event["end_date_time"]
                    ),  # Convert to timezone-aware
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully insert {self.data} > {event_instance.title}"
                    )
                )
                if event_id <= COUNT_EVENTS_HAS_ALBUM:
                    for uuid in [
                        "9HrBC1jMQ3KlZw4CssPUeQ",
                        "VQ6EAOKbQdSnFkRmVUQAAA",
                        "Ej5FZOi5EtOkVkJmFBdAAA",
                        "a6e4EAna0R2AtADAT9QwyA",
                        "G51rzbv9Sy2bXavY-9tL7Q",
                        "oO68mZwLTvi7bWu2m704oQ",
                        "Kg4Obp4bHrqLMgJCrBMA",
                        "Tp5bXp4bHrqLMgJCrBMA",
                        "f16efp4bHrqLMgJCrBMA",
                        "n2qenp4bHrqLMgJCrBMA",
                        "n3qenp4bHrqLMgJCrBMA",
                        "n4qenp4bHrqLMgJCrBMA",
                    ]:
                        try:
                            EventAlbum.objects.create(
                                event=event_instance,
                                image=join(
                                    "images",
                                    get_model_name_from_class(EventAlbum),
                                    f"{event_id}",
                                    f"{uuid}.png",
                                ),
                            )
                            self.stdout.write(
                                self.style.SUCCESS(
                                    f"Successfully insert Event Photo > {event_instance.title}"
                                )
                            )
                        except Exception as ee:
                            self.stdout.write(
                                self.style.ERROR(
                                    f"Failed insert Event Photo > {event_instance.title} , \n \t Error is: \t \t{ee}"
                                )
                            )

            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed insert {self.data} > {event} , \n \t Error is: \t \t{e}"
                    )
                )

            event_id = event_id + 1

        self.stdout.write(self.style.WARNING(f"Finish Created initial {self.data}"))
