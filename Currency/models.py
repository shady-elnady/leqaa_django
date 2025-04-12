from django.db.models import CharField, FloatField, ManyToManyField, ForeignKey, CASCADE
from django.utils.translation import get_language, to_locale

from App.messages import ModelsMessages, FieldsMessages
from App.models import BaseModel
from Language.models.BaseTranslationModel import BaseTranslationModel

# Create your models here.


class Currency(BaseTranslationModel):
    iso_code = CharField(
        max_length=5,
        unique=True,
        verbose_name=FieldsMessages.ISO_CODE,
    )
    symbol = CharField(
        max_length=5,
        blank=True,
        null=True,
        verbose_name=FieldsMessages.SYMBOL,
    )
    exchange_rates = ManyToManyField(
        to="self",
        through="CurrencyExchangeRate",
        verbose_name=FieldsMessages.EXCHANGE_RATES,
    )

    @property
    def translated_name(self) -> str:
        trans = self.translations[to_locale(get_language())]
        return trans if trans else self.name

    class Meta:
        verbose_name = ModelsMessages.CURRENCY
        verbose_name_plural = ModelsMessages.CURRENCIES


class CurrencyExchangeRate(BaseModel):
    currency = ForeignKey(
        Currency,
        on_delete=CASCADE,
        related_name="%(class)s+",
        verbose_name=ModelsMessages.CURRENCY,
    )
    exchange_2_currency = ForeignKey(
        Currency,
        on_delete=CASCADE,
        related_name="%(class)s+",
        verbose_name=FieldsMessages.EXCHANGE_TO_CURRENCY,
    )
    rate = FloatField(
        verbose_name=FieldsMessages.RATE,
    )

    class Meta:
        unique_together = (
            "currency",
            "exchange_2_currency",
        )
        verbose_name = ModelsMessages.CURRENCY_EXCHANGE_RATE
        verbose_name_plural = ModelsMessages.CURRENCY_EXCHANGE_RATES


##  https://openexchangerates.org/account/app-ids
# api ID = "02b179d00a8948e68d0ba908a61fb93f"
