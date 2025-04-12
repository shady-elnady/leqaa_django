from django.apps import AppConfig
from django.conf import settings
from django.core.cache import cache
from django.db.utils import OperationalError, ProgrammingError

from App.messages import ModelsMessages


class LanguageConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Language"
    verbose_name = ModelsMessages.LANGUAGE
    verbose_name_plural = ModelsMessages.LANGUAGES

    def ready(self):
        import Language.utils.signals  # noqa: F401

        # Use Django's autoreloader to run after apps are loaded
        if not getattr(settings, "TESTING", False) and not getattr(
            settings, "LOCALES_LOADED", False
        ):
            from django.utils.autoreload import autoreload_started
            from Language.utils.locales_loader import fetch_supported_locales

            def load_locales_when_ready(**kwargs):
                try:
                    from Language.models import Locale

                    if Locale.objects.exists():
                        fetch_supported_locales()
                except (OperationalError, ProgrammingError):
                    pass

            autoreload_started.connect(load_locales_when_ready)
