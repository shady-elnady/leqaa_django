from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class GENDERS(TextChoices):
    MALE = "M", _("Male")
    FEMALE = "F", _("FeMale")


class USERS_TYPES(TextChoices):
    SuperUser = "SU", _("Super User")
    Admin = "A", _("Admin")
    Lecturer = "L", _("Lecturer")
    Staff = "St", _("Staff")
    Student = "S", _("Student")
    User = "U", _("User")


class TITLES(TextChoices):
    Doctor = "D", _("Doctor")
    Engineer = "E", _("Engineer")
    Professor = "P", _("Professor")
    Student = "S", _("Student")


class MARITAL_STATUS(TextChoices):
    VIRGIN = "V", _("Virgin")  # اعزب
    BACHELOR = "B", _("Bachelor")  # اعزب
    MARRIED = "M", _("Married")  # متزوج
    WIDOWER = "W", _("Widower")  # ارمل
    DIVORCDE = "D", _("Divorced")  # مطلقه
