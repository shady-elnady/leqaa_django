from django.apps import AppConfig

from App.messages import ModelsMessages


class LogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Log"
    verbose_name = ModelsMessages.LOG
    verbose_name_plural = ModelsMessages.LOGS
