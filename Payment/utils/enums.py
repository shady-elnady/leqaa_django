from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class PAYMENT_METHOD_TYPES(TextChoices):
    Monetary = "M", _("Monetary")
    CreditCard = "Cr", _("Credit Card")
    BankTransfer = "BT", _("Bank Transfer")
    Check = "Ch", _("Check")
    MoneyTransfer = "MT", _("Money Transfer")
    MobileCach = "MC", _("Mobile Cach")


class PAYMENT_STATUS_TYPES(TextChoices):
    Paid = "P", _("Paid")
    PayLater = "L", _("Pay later")
    PartiallyPaid = "PP", _("Partially Paid")


class FINANCIAL_TRANSACTIONS_TYPES(TextChoices):  # أنواع المعاملات المالية
    REVENUES = "R", _("Revenues")  # الإيرادات
    EXPENSES = "E", _("Expenses")  # المصروفات \ نفقات
    # DEBTS = "D", _("Debts")  # مديونيات
    # DUES = "U", _("Dues")  # مستحقات
