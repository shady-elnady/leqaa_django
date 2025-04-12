from django.db.models import CharField, ForeignKey, CASCADE

from App.messages import ModelsMessages, FieldsMessages
from Language.models.BaseTranslationModel import BaseTranslationModel
from Address.utils.enums import StateTypes
from Address.models import City

# Create your models here.


class State(BaseTranslationModel):
    city = ForeignKey(
        City,
        on_delete=CASCADE,
        related_name="Areas",
        verbose_name=ModelsMessages.CITY,
    )
    postal_code = CharField(
        max_length=5,
        null=True,
        blank=True,
        verbose_name=FieldsMessages.POSTAL_CODE,
    )
    state_type = CharField(
        max_length=2,
        choices=StateTypes.choices,
        default=StateTypes.VILLAGE,
        verbose_name=FieldsMessages.STATE_TYPE,
    )

    class Meta:
        verbose_name = ModelsMessages.STATE
        verbose_name_plural = ModelsMessages.STATES


"""

https://stackoverflow.com/questions/51159241/how-to-generate-shapefiles-for-h3-hexagons-in-a-particular-area

"""
