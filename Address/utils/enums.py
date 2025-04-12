from django.db.models import TextChoices

from App.messages import ChoicesMessages


class StateTypes(TextChoices):
    TALUK = "T", ChoicesMessages.TALUK
    VILLAGE = "V", ChoicesMessages.VILLAGE  # القرية
    DISTRICT = "D", ChoicesMessages.DISTRICT  # المنطقة
    MANOR = "M", ChoicesMessages.MANOR  # عزبه
    RESIDENTIAL_QUARTER = "RQ", ChoicesMessages.RESIDENTIAL_QUARTER  # حى سكنى
    HOUSING = "H", ChoicesMessages.HOUSING  # مساكن
    FEUDALISM = "F", ChoicesMessages.FEUDALISM  # اقطاعيه
    REGION = "R", ChoicesMessages.REGION  # منطقه


class CONTINENTS(TextChoices):
    AFRICA = "AF", ChoicesMessages.AFRICA
    ASIA = "AS", ChoicesMessages.ASIA
    EUROPE = "EU", ChoicesMessages.EUROPE
    NORTH_AMERICA = "NA", ChoicesMessages.NORTH_AMERICA
    OCEANIA = "OC", ChoicesMessages.OCEANIA
    SOUTH_AMERICA = "SA", ChoicesMessages.SOUTH_AMERICA
    ANTARCTICA = "AN", ChoicesMessages.ANTARCTICA
