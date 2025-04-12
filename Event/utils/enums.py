from django.db.models import TextChoices
from App.messages import ChoicesMessages


class LecturerFinancialSystem(TextChoices):
    All = "A", ChoicesMessages.ALL_EVENT
    Each = "E", ChoicesMessages.EACH_STUDENT
    Enlist = "N", ChoicesMessages.ENLIST


class EventPaidStatus(TextChoices):
    Free = "F", ChoicesMessages.COMPLETELY_FREE
    Partially = "P", ChoicesMessages.PARTIALLY_PAID
    Paid = "C", ChoicesMessages.COMPLETELY_PAID


class OnOrOffLineStatus(TextChoices):
    OnLine = "N", ChoicesMessages.ON_LINE
    OffLine = "F", ChoicesMessages.OFF_LINE
    Any = "A", ChoicesMessages.ANY
