from django.db.models import ForeignKey, CASCADE
from django.utils.translation import gettext_lazy as _

from Locale.models.BaseTranslationModel import BaseTranslationModel
from .University import University
from Utils.models.BaseModel import BaseLogoModel

# Create your models here.


class College(BaseTranslationModel, BaseLogoModel):
    university = ForeignKey(
        University,
        on_delete=CASCADE,
        related_name=_("Colleges"),
        verbose_name=_("University"),
    )

    class Meta:
        verbose_name = _("College")
        verbose_name_plural = _("Colleges")
