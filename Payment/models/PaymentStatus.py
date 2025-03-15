from django.db.models import CharField
from django.utils.translation import gettext_lazy as _

from Locale.models.BaseTranslationModel import BaseTranslationModel
from Payment.utils.enums import PAYMENT_STATUS_TYPES

# Create your mofrom django.utils.text import slugify


class PaymentStatus(BaseTranslationModel):
    payment_status_type = CharField(
        max_length=2,
        choices=PAYMENT_STATUS_TYPES.choices,
        default=PAYMENT_STATUS_TYPES.Paid,
        verbose_name=_("Payment Status Type"),
    )

    class Meta:
        verbose_name = _("PaymentStatus")
        verbose_name_plural = _("Payment Statuses")
