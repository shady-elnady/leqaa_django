from django.db.models import (
    CharField,
    FloatField,
    TextField,
    ForeignKey,
    CASCADE,
)
from django.utils.translation import gettext_lazy as _

from Utils.models.BaseModel import BaseModel
from Reservation.utils.enums import RESERVATION_STATUS
from User.models import Student
from Event.models import Event

# Create your model


class Reservation(BaseModel):
    student = ForeignKey(
        Student,
        on_delete=CASCADE,
        related_name=_("Reservations"),
        verbose_name=_("Student"),
    )
    event = ForeignKey(
        Event,
        on_delete=CASCADE,
        related_name=_("Reservations"),
        verbose_name=_("Event"),
    )
    reservation_status = CharField(
        max_length=2,
        choices=RESERVATION_STATUS.choices,
        default=RESERVATION_STATUS.InitialzationReservation,
        verbose_name=_("Reservation Status"),
    )
    rating = FloatField(
        default=0,
        verbose_name=_("Rating"),
    )
    canceled_reason = TextField(
        null=True,
        blank=True,
        verbose_name=_("Canceled Reason"),
    )
    comment = TextField(
        null=True,
        blank=True,
        verbose_name=_("Comment"),
    )

    def __str__(self) -> str:
        return f"{self.pk}-{self.student.user.username}({self.event.title})"

    def __decode__(self) -> str:
        return f"{self.pk}- {self.student.user.username}({self.event.title})"

    class Meta:
        verbose_name = _("Reservation")
        verbose_name_plural = _("Reservations")
