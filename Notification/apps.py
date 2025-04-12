from django.apps import AppConfig

from App.messages import ModelsMessages


class NotificationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Notification"
    verbose_name = ModelsMessages.NOTIFICATION
    verbose_name_plural = ModelsMessages.NOTIFICATIONS

    def ready(self):
        import Notification.utils.signals  # noqa: F401  # Import your signals here
