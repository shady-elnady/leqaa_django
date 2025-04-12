from django.apps import AppConfig

from App.messages import ModelsMessages


class ReservationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Reservation"
    verbose_name = ModelsMessages.RESERVATION
    verbose_name_plural = ModelsMessages.RESERVATIONS
