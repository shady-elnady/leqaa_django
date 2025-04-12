from django.db.models import JSONField, ForeignKey, CASCADE, FloatField

from Language.models.BaseTranslationModel import BaseTranslationModel
from App.messages import ModelsMessages, FieldsMessages
from Address.models import Locality, Street

# Create your models here.


class Location(BaseTranslationModel):
    locality = ForeignKey(
        Locality,
        on_delete=CASCADE,
        related_name="Addresses",
        verbose_name=ModelsMessages.LOCALITY,
    )
    street = ForeignKey(
        Street,
        null=True,
        blank=True,
        on_delete=CASCADE,
        related_name="Addresses",
        verbose_name=ModelsMessages.STREET,
    )
    lat = FloatField(
        null=True,
        blank=True,
        verbose_name=FieldsMessages.LATITUDE,
    )
    lng = FloatField(
        null=True,
        blank=True,
        verbose_name=FieldsMessages.LONGITUDE,
    )
    address = JSONField(
        null=True,
        blank=True,
        verbose_name=FieldsMessages.ADDRESS,
    )

    class Meta:
        verbose_name = ModelsMessages.LOCATION
        verbose_name_plural = ModelsMessages.LOCATIONS
