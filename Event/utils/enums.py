from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class LecturerFinancialSystem(TextChoices):
    All = "A", _("All Event")
    Each = "E", _("Each Student")
    Enlist = "N", _("Enlist")  # تطوع


class EventPaidStatus(TextChoices):
    Free = "F", _("Completely ")
    Partially = "P", _("Partially Paid")
    Paid = "C", _("Completely Paid")


class OnOrOffLineStatus(TextChoices):
    OnLine = "N", _("On Line ")
    OffLine = "F", _("Off Line")
    Any = "A", _("Any")
