from django.db.models import ForeignKey, CASCADE

from Language.models.BaseTranslationModel import BaseTranslationModel
from App.messages import ModelsMessages
from .governorate_model import Governorate
from Address.models import Country

# Create your models here.


class City(BaseTranslationModel):
    country = ForeignKey(
        Country,
        on_delete=CASCADE,
        related_name="Cities",
        verbose_name=ModelsMessages.COUNTRY,
    )
    governorate = ForeignKey(
        Governorate,
        null=True,
        blank=True,
        on_delete=CASCADE,
        related_name="Cities",
        verbose_name=ModelsMessages.GOVERNORATE,
    )

    class Meta:
        verbose_name = ModelsMessages.CITY
        verbose_name_plural = ModelsMessages.CITIES
