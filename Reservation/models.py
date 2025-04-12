from django.db.models import (
    CharField,
    FloatField,
    TextField,
    ForeignKey,
    CASCADE,
)

from App.models import BaseModel
from App.messages import ModelsMessages, FieldsMessages
from Reservation.utils.enums import RESERVATION_STATUS
from User.models import User
from Event.models import Event

# Create your model


class Reservation(BaseModel):
    user = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name="Reservations",
        verbose_name=ModelsMessages.USER,
    )
    event = ForeignKey(
        Event,
        on_delete=CASCADE,
        related_name="Reservations",
        verbose_name=ModelsMessages.EVENT,
    )
    reservation_status = CharField(
        max_length=2,
        choices=RESERVATION_STATUS.choices,
        default=RESERVATION_STATUS.InitializationReservation,
        verbose_name=ModelsMessages.RESERVATION_STATUS,
    )
    rating = FloatField(
        default=0,
        verbose_name=FieldsMessages.RATING,
    )
    canceled_reason = TextField(
        null=True,
        blank=True,
        verbose_name=FieldsMessages.CANCELED_REASON,
    )
    comment = TextField(
        null=True,
        blank=True,
        verbose_name=FieldsMessages.COMMENT,
    )

    def __str__(self) -> str:
        return f"{self.pk}-{self.user.username}({self.event.title})"

    def __decode__(self) -> str:
        return f"{self.pk}- {self.user.username}({self.event.title})"

    class Meta:
        verbose_name = ModelsMessages.RESERVATION
        verbose_name_plural = ModelsMessages.RESERVATIONS
