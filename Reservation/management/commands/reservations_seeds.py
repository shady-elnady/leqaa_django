from django.core.management.base import BaseCommand

from Reservation.models import Reservation
from Reservation.utils.enums import RESERVATION_STATUS
from User.models import User
from Event.models import Event


class Command(BaseCommand):
    data = "Reservations"
    help = f"Creates initial {data} model"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        reservations = [
            {
                "user": 1,
                "event": 1,
                "reservation_status": RESERVATION_STATUS.InitializationReservation,
                "rating": 4.5,
                "canceled_reason": None,
                "comment": "comment",
            },
        ]

        for reservation in reservations:
            try:
                Reservation.objects.create(
                    user=User.objects.get(pk=reservation["user"]),
                    event=Event.objects.get(pk=reservation["event"]),
                    reservation_status=reservation["reservation_status"],
                    rating=reservation["rating"],
                    canceled_reason=reservation["canceled_reason"],
                    comment=reservation["comment"],
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully insert {self.data} > {reservation}"
                    )
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed insert {self.data} > {reservation} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING(f"Finish Created initial {self.data}"))
