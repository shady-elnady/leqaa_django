from django.db.models import CharField
from django.utils.translation import gettext_lazy as _

from Locale.models.BaseTranslationModel import BaseTranslationModel
from Payment.utils.enums import PAYMENT_METHOD_TYPES

# Create your mofrom django.utils.text import slugify


class PaymentMethod(BaseTranslationModel):

    payment_Method_type = CharField(
        max_length=2,
        choices=PAYMENT_METHOD_TYPES.choices,
        default=PAYMENT_METHOD_TYPES.Monetary,
        verbose_name=_("Payment Method Type"),
    )

    class Meta:
        verbose_name = _("Payment Method")
        verbose_name_plural = _("Payment Methods")
