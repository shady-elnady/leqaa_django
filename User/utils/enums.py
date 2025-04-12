from django.db.models import TextChoices
from App.messages import ChoicesMessages, ModelsMessages


class GENDERS(TextChoices):
    MALE = "M", ChoicesMessages.MALE
    FEMALE = "F", ChoicesMessages.FEMALE


class USERS_TYPES(TextChoices):
    Developer = "D", ModelsMessages.USER
    SuperUser = "SU", ChoicesMessages.SUPER_USER
    Admin = "A", ChoicesMessages.ADMIN
    Lecturer = "L", ChoicesMessages.LECTURER
    Staff = "St", ChoicesMessages.STAFF
    Student = "S", ChoicesMessages.STUDENT
    User = "U", ModelsMessages.USER


class TITLES(TextChoices):
    Doctor = "D", ChoicesMessages.DOCTOR
    Engineer = "E", ChoicesMessages.ENGINEER
    Professor = "P", ChoicesMessages.PROFESSOR
    Student = "S", ChoicesMessages.STUDENT


class MARITAL_STATUS(TextChoices):
    VIRGIN = "V", ChoicesMessages.VIRGIN  # اعزب
    BACHELOR = "B", ChoicesMessages.BACHELOR  # اعزب
    MARRIED = "M", ChoicesMessages.MARRIED  # متزوج
    WIDOWER = "W", ChoicesMessages.WIDOWER  # ارمل
    DIVORCDE = "D", ChoicesMessages.DIVORCDE  # مطلقه
