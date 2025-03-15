from django.db.models import CharField, ForeignKey, CASCADE
from django.utils.translation import gettext_lazy as _

from Address.utils.enums import STATES_TYPES
from Locale.models.BaseTranslationModel import BaseTranslationModel
from .City import City

# Create your models here.


class State(BaseTranslationModel):
    city = ForeignKey(
        City,
        on_delete=CASCADE,
        related_name=_("Areas"),
        verbose_name=_("City"),
    )
    postal_code = CharField(
        max_length=5,
        null=True,
        blank=True,
        verbose_name=_("Postal Code"),
    )
    state_type = CharField(
        max_length=2,
        choices=STATES_TYPES.choices,
        default=STATES_TYPES.VILLAGE,
        verbose_name=_("State Type"),
    )

    class Meta:
        verbose_name = _("State")
        verbose_name_plural = _("States")


"""

https://stackoverflow.com/questions/51159241/how-to-generate-shapefiles-for-h3-hexagons-in-a-particular-area

"""
