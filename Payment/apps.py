from django.apps import AppConfig

from App.messages import ModelsMessages


class PaymentConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Payment"
    verbose_name = ModelsMessages.PAYMENT
    verbose_name_plural = ModelsMessages.PAYMENTS
