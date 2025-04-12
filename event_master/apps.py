from django.apps import AppConfig

from App.messages import ModelsMessages, FieldsMessages


class AdminBerryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "event_master"
    verbose_name = ModelsMessages.EVENT_MASTER
    verbose_name_plural = ModelsMessages.EVENT_MASTERS
