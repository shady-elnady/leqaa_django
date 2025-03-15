from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class RESERVATION_STATUS(TextChoices):
    InitialzationReservation = "I", _("Initialzation Reservation")
    CanceledReservation = "C", _("Canceled Reservation")
    ConfirmedReservation = "R", _("Confirmed Reservation")
    HoldReservation = "H", _("Hold Reservation")
