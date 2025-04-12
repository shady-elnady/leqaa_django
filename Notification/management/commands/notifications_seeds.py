from django.core.management.base import BaseCommand

from User.models import User
from Category.models import Category
from Notification.models import Notification


class Command(BaseCommand):
    data = "Notifications"
    help = f"Creates initial {data} model"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        notifications = [
            {
                "user": 1,
                "category": 1,
            },
            {
                "user": 1,
                "category": 2,
            },
            {
                "user": 1,
                "category": 3,
            },
            {
                "user": 2,
                "category": 1,
            },
            {
                "user": 2,
                "category": 2,
            },
            {
                "user": 2,
                "category": 3,
            },
        ]

        for notification in notifications:
            try:
                Notification.objects.create(
                    user=User.objects.get(pk=notification["user"]),
                    category=Category.objects.get(pk=notification["category"]),
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully insert {self.data} > {notification}"
                    )
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed insert {self.data} > {notification} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING(f"Finish Created initial {self.data}"))
