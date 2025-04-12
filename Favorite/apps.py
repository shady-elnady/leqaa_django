from django.apps import AppConfig

from App.messages import ModelsMessages


class FavoriteConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Favorite"
    verbose_name = ModelsMessages.FAVORITE
    verbose_name_plural = ModelsMessages.FAVORITES
