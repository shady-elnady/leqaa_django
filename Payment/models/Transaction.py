from django.db.models import (
    CharField,
    SmallIntegerField,
    ForeignKey,
    CASCADE,
    FloatField,
    TextField,
    PROTECT,
    DateTimeField,
)
from App.messages import ModelsMessages, FieldsMessages

from Currency.models import Currency
from Payment.models import PaymentMethod, PaymentStatus
from Reservation.models import Reservation
from User.models import User
from App.models.base_models import BaseModel

# Create your mofrom django.utils.text import slugify


class Transaction(BaseModel):
    transactor = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name="Transactions",
        verbose_name=FieldsMessages.TRANSACTOR,
    )
    reservation = ForeignKey(
        Reservation,
        null=True,
        blank=True,
        on_delete=PROTECT,
        related_name="Transactions",
        verbose_name=ModelsMessages.RESERVATION,
    )
    payment_status = ForeignKey(
        PaymentStatus,
        null=True,
        blank=True,
        on_delete=PROTECT,
        related_name="Transactions",
        verbose_name=ModelsMessages.PAYMENY_STATUS,
    )
    payment_method = ForeignKey(
        PaymentMethod,
        null=True,
        blank=True,
        on_delete=PROTECT,
        related_name="Transactions",
        verbose_name=ModelsMessages.PAYMENY_METHOD,
    )
    currency = ForeignKey(
        Currency,
        on_delete=PROTECT,
        related_name="Transactions",
        verbose_name=ModelsMessages.CURRENCY,
    )
    due_date = DateTimeField(
        null=True,
        blank=True,
        verbose_name=FieldsMessages.DUE_DATE,
    )  # تاريخ الاستحقاق
    notified_days = SmallIntegerField(
        null=True,
        blank=True,
        verbose_name=FieldsMessages.NOTIFIED_DAYS,
    )  # يخطر قبل ايام
    reference_number = CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name=FieldsMessages.REFERENCE_NUMBER,
    )
    bank_deposit_date = DateTimeField(
        null=True,
        blank=True,
        verbose_name=FieldsMessages.BANK_DEPOSIT_DATE,
    )  # تاريخ الإيداع البنكي
    bank_name = CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=FieldsMessages.BANK_NAME,
    )
    comment = TextField(
        null=True,
        blank=True,
        verbose_name=FieldsMessages.COMMENT,
    )
    total_required_amount = FloatField(
        verbose_name=FieldsMessages.TOTAL_REQUIRED_AMOUNT,
    )
    amount = FloatField(
        verbose_name=FieldsMessages.AMOUNT,
    )

    @property
    def remaining_amount(self):
        return self.total_required_amount - self.amount

    def __str__(self) -> str:
        return f"{self.pk} >{self.transactor.username}"

    def __decode__(self) -> str:
        return f"{self.pk} >{self.transactor.username}"

    class Meta:
        verbose_name = ModelsMessages.TRANSACTION
        verbose_name_plural = ModelsMessages.TRANSACTIONS
