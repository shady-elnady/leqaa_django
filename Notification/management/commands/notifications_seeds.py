from django.core.management.base import BaseCommand

from Notification.models import Notification
from User.models import User
from Event.models import Event


class Command(BaseCommand):
    data = "Notifications"
    help = f"Creates initial {data} model"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        notifications = [
            {
                "user": 1,
                "event": 1,
            },
            {
                "user": 1,
                "event": 2,
            },
            {
                "user": 1,
                "event": 3,
            },
            {
                "user": 2,
                "event": 1,
            },
            {
                "user": 2,
                "event": 2,
            },
            {
                "user": 2,
                "event": 3,
            },
        ]

        for notification in notifications:
            try:
                Notification.objects.create(
                    user=User.objects.get(pk=notification["user"]),
                    event=Event.objects.get(pk=notification["event"]),
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
