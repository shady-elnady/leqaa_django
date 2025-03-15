from django.db.models import CharField, ForeignKey, CASCADE
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from Locale.models.BaseTranslationModel import BaseTranslationModel
from .Country import Country

# Create your models here.


class Governorate(BaseTranslationModel):  # المحافظه
    ## https://en.wikipedia.org/wiki/ISO_3166-2:EG

    governorate_tel_code_regex = RegexValidator(
        regex=r"^\d{1,3}$",
        message=_(
            "Rest Phone number must be entered in the format: '999'. Up to 3 digits allowed."
        ),
    )
    country = ForeignKey(
        Country,
        on_delete=CASCADE,
        related_name=_("Governorates"),
        verbose_name=_("Country"),
    )
    governorate_tel_code = CharField(
        max_length=3,
        blank=True,
        null=True,
        unique=True,
        validators=[governorate_tel_code_regex],
        verbose_name=_("Telephone Code"),
    )

    class Meta:
        verbose_name = _("Governorate")
        verbose_name_plural = _("Governorates")
