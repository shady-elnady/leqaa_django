from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class STATES_TYPES(TextChoices):
    TALUK = "T", _("Taluk")
    VILLAGE = "V", _("Village")  # القرية
    DISTRICT = "D", _("District")  # المنطقة
    MANOR = "M", _("Manor")  # عزبه
    RESIDENTIAL_QUARTER = "RQ", _("Residential Quarter")  # حى سكنى
    HOUSING = "H", _("Housing")  # مساكن
    FEUDALISM = "F", _("Feudalism")  # اقطاعيه
    REGION = "R", _("Region")  # منطقه


class CONTINENTS(TextChoices):
    AFRICA = "AF", _("Africa")
    ASIA = "AS", _("Asia")
    EUROPE = "EU", _("Europe")
    NORTH_AMERICA = "NA", _("North America")
    OCEANIA = "OC", _("Oceania")
    SOUTH_AMERICA = "SA", _("South America")
    ANTARCTICA = "AN", _("Antarctica")
