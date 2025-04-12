from django.db.models import CharField

from Language.models import BaseTranslationModel
from App.messages import ModelsMessages, FieldsMessages
from Payment.utils.enums import PAYMENT_METHOD_TYPES

# Create your mofrom django.utils.text import slugify


class PaymentMethod(BaseTranslationModel):

    payment_Method_type = CharField(
        max_length=2,
        choices=PAYMENT_METHOD_TYPES.choices,
        default=PAYMENT_METHOD_TYPES.Monetary,
        verbose_name=FieldsMessages.PAYMENY_METHOD_TYPE,
    )

    class Meta:
        verbose_name = ModelsMessages.PAYMENY_METHOD
        verbose_name_plural = ModelsMessages.PAYMENY_METHODS
