from django.db.models import TextChoices
from App.messages import ChoicesMessages


class PAYMENT_METHOD_TYPES(TextChoices):
    Monetary = "M", ChoicesMessages.MONETARY
    CreditCard = "Cr", ChoicesMessages.CREDIT_CARD
    BankTransfer = "BT", ChoicesMessages.BANK_TRANSFER
    Check = "Ch", ChoicesMessages.CHECK
    MoneyTransfer = "MT", ChoicesMessages.MONEY_TRANSFER
    MobileCash = (
        "MC",
        ChoicesMessages.MOBILE_CASH,
    )  # Fixed attribute name from "MobileCach"


class PAYMENT_STATUS_TYPES(TextChoices):
    Paid = "P", ChoicesMessages.PAID
    PayLater = "L", ChoicesMessages.PAY_LATER
    PartiallyPaid = "PP", ChoicesMessages.PARTIALLY_PAID


class FINANCIAL_TRANSACTIONS_TYPES(TextChoices):
    REVENUES = "R", ChoicesMessages.REVENUES  # الإيرادات
    EXPENSES = "E", ChoicesMessages.EXPENSES  # المصروفات \ نفقات
    # DEBTS = "D", ChoicesMessages.DEBTS  # مديونيات
    # DUES = "U", ChoicesMessages.DUES  # مستحقات
