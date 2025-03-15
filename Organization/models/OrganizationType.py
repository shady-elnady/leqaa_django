# from django.db.models import CharField, ForeignKey, OneToOneField, CASCADE, TextChoices
from django.utils.translation import gettext_lazy as _

from Locale.models.BaseTranslationModel import BaseTranslationModel

# Create your models here.


class OrganizationType(BaseTranslationModel):

    class Meta:
        verbose_name = _("Organization Type")
        verbose_name_plural = _("Organizations Types")
