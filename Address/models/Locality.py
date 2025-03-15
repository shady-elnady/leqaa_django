from django.db.models import ForeignKey, CASCADE
from django.utils.translation import gettext_lazy as _

from Locale.models.BaseTranslationModel import BaseTranslationModel
from .State import State

# Create your models here.


class Locality(BaseTranslationModel):
    state = ForeignKey(
        State,
        on_delete=CASCADE,
        related_name=_("Areas"),
        verbose_name=_("State"),
    )

    class Meta:
        verbose_name = _("Locality")
        verbose_name_plural = _("Localities")
