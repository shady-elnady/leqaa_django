# from django.db import models
from django.db.models import CharField, FloatField, ManyToManyField, ForeignKey, CASCADE
from django.utils.translation import get_language, to_locale
from django.utils.translation import gettext_lazy as _

# from django.utils.translation import get_language

from Utils.models.BaseModel import BaseTimeStampModel
from Locale.models.BaseTranslationModel import BaseTranslationModel

# Create your models here.


class Currency(BaseTranslationModel):
    iso_code = CharField(
        max_length=5,
        unique=True,
        verbose_name=_("ISO Code"),
    )
    symbol = CharField(
        max_length=5,
        blank=True,
        null=True,
        verbose_name=_("Symbol"),
    )
    exchange_rates = ManyToManyField(
        to="self",
        through="CurrencyExchangeRate",
        verbose_name=_("Exchange Rates"),
    )

    @property
    def translated_name(self) -> str:
        trans = self.translations[to_locale(get_language())]
        return trans if trans else self.name

    class Meta:
        verbose_name = _("Currency")
        verbose_name_plural = _("Currencies")


class CurrencyExchangeRate(BaseTimeStampModel):
    currency = ForeignKey(
        Currency,
        on_delete=CASCADE,
        related_name="%(class)s+",
        verbose_name=_("Currency"),
    )
    exchange_2_currency = ForeignKey(
        Currency,
        on_delete=CASCADE,
        related_name="%(class)s+",
        verbose_name=_("Exchange to Currency"),
    )
    rate = FloatField(
        verbose_name=_("Rate"),
    )

    class Meta:
        unique_together = (
            "currency",
            "exchange_2_currency",
        )
        verbose_name = _("Currency Exchange Rate")
        verbose_name_plural = _("Currencies Exchange Rates")


##  https://openexchangerates.org/account/app-ids
# api ID = "02b179d00a8948e68d0ba908a61fb93f"
