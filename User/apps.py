from django.apps import AppConfig

from App.messages import ModelsMessages


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "User"
    verbose_name = ModelsMessages.USER
    verbose_name_plural = ModelsMessages.USERS

    def ready(self):
        import User.utils.signals  # noqa: F401
