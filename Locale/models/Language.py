from django.db.models import CharField, BooleanField
from django.utils.translation import gettext_lazy as _

from Utils.models.BaseModel import BaseNativeModel

# Create your model


class Language(BaseNativeModel):
    language_iso_code = CharField(
        max_length=2,
        unique=True,
        verbose_name=_("Language ISO Code"),
    )
    is_bidirectional = BooleanField(
        default=False,
        verbose_name=_("is Bidirectional"),
    )

    class Meta:
        verbose_name = _("Language")
        verbose_name_plural = _("Languages")
