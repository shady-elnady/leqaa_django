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
from django.utils.translation import gettext_lazy as _

from Currency.models import Currency
from Payment.models import PaymentMethod, PaymentStatus
from Reservation.models import Reservation
from User.models import User
from Utils.models.BaseModel import BaseModel

# Create your mofrom django.utils.text import slugify


class Transaction(BaseModel):
    transactor = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name="Transactions",
        verbose_name=_("Transactor"),
    )
    reservation = ForeignKey(
        Reservation,
        null=True,
        blank=True,
        on_delete=PROTECT,
        related_name="Transactions",
        verbose_name=_("Reservation"),
    )
    payment_status = ForeignKey(
        PaymentStatus,
        null=True,
        blank=True,
        on_delete=PROTECT,
        related_name="Transactions",
        verbose_name=_("Payment Status"),
    )
    payment_method = ForeignKey(
        PaymentMethod,
        null=True,
        blank=True,
        on_delete=PROTECT,
        related_name="Transactions",
        verbose_name=_("Payment Method"),
    )
    currency = ForeignKey(
        Currency,
        on_delete=PROTECT,
        related_name="Transactions",
        verbose_name=_("Currency"),
    )
    due_date = DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Due Date"),
    )  # تاريخ الاستحقاق
    notified_days = SmallIntegerField(
        null=True,
        blank=True,
        verbose_name=_("Notified Days"),
    )  # يخطر قبل ايام
    reference_number = CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name=_("Reference Number"),
    )
    bank_deposit_date = DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Bank Deposit Date"),
    )  # تاريخ الإيداع البنكي
    bank_name = CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Bank Name"),
    )
    comment = TextField(
        null=True,
        blank=True,
        verbose_name=_("Comment"),
    )
    total_required_amount = FloatField(
        verbose_name=_("Total Required Amount"),
    )
    amount = FloatField(
        verbose_name=_("Amount"),
    )

    @property
    def remaining_amount(self):
        return self.total_required_amount - self.amount

    def __str__(self) -> str:
        return f"{self.pk} >{self.transactor.username}"

    def __decode__(self) -> str:
        return f"{self.pk} >{self.transactor.username}"

    class Meta:
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")
