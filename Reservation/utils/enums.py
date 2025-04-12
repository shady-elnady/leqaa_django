from django.db.models import TextChoices
from App.messages import ChoicesMessages


class RESERVATION_STATUS(TextChoices):
    InitializationReservation = "I", ChoicesMessages.INITIALIZATION_RESERVATION
    CanceledReservation = "C", ChoicesMessages.CANCELED_RESERVATION
    ConfirmedReservation = "R", ChoicesMessages.CONFIRMED_RESERVATION
    HoldReservation = "H", ChoicesMessages.HOLD_RESERVATION
