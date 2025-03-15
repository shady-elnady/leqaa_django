from django.db.models import JSONField, ForeignKey, CASCADE
from django.utils.translation import gettext_lazy as _

from Locale.models.BaseTranslationModel import BaseTranslationModel
from .Street import Street
from .Locality import Locality

# Create your models here.


class Address(BaseTranslationModel):
    locality = ForeignKey(
        Locality,
        on_delete=CASCADE,
        related_name=_("Address"),
        verbose_name=_("Locality"),
    )
    street = ForeignKey(
        Street,
        null=True,
        blank=True,
        on_delete=CASCADE,
        related_name=_("Address"),
        verbose_name=_("Street"),
    )
    details = JSONField(
        null=True,
        blank=True,
        verbose_name=_("Details"),
    )

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Address")
