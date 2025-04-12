from django.apps import AppConfig

from App.messages import ModelsMessages


class AddressConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Address"
    verbose_name = ModelsMessages.ADDRESS
    verbose_name_plural = ModelsMessages.ADDRESSES
