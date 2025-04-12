from django.db.models import CharField

from Language.models import BaseTranslationModel
from App.messages import ModelsMessages, FieldsMessages
from Payment.utils.enums import PAYMENT_STATUS_TYPES

# Create your mofrom django.utils.text import slugify


class PaymentStatus(BaseTranslationModel):
    payment_status_type = CharField(
        max_length=2,
        choices=PAYMENT_STATUS_TYPES.choices,
        default=PAYMENT_STATUS_TYPES.Paid,
        verbose_name=FieldsMessages.PAYMENY_STATUS_TYPE,
    )

    class Meta:
        verbose_name = ModelsMessages.PAYMENY_STATUS
        verbose_name_plural = ModelsMessages.PAYMENY_STATUSES
