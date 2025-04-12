from django.apps import AppConfig

from App.messages import ModelsMessages


class AdvertisementConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Advertisement"
    verbose_name = ModelsMessages.ADVERTISEMENT
    verbose_name_plural = ModelsMessages.ADVERTISEMENTS
