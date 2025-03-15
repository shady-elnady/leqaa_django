from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _
import calendar

# Create your TextChoices here.


class WEEK_DAYS(TextChoices):
    SATURDAY = f"{calendar.SATURDAY}", _("Saturday")
    SUNDAY = f"{calendar.SUNDAY}", _("Sunday")
    MONDAY = f"{calendar.MONDAY}", _("Monday")
    TUESDAY = f"{calendar.TUESDAY}", _("Tuesday")
    WEDNESDAY = f"{calendar.WEDNESDAY}", _("Wednesday")
    THURSDAY = f"{calendar.THURSDAY}", _("Thursday")
    FRIDAY = f"{calendar.FRIDAY}", _("Friday")


class FACILITY_TYPES(TextChoices):
    LABORATORY = "L", _("Laboratory")
    MainLaboratory = "ML", _("MainLaboratory")
    ASSOCIATIONS = "A", _("Association")
    DISPENSARY = "D", _("Dispensary")
    SCIENTIFIC_COMPANY = "SC", _("Scientific Company")
    PHARMACEUTICAL_COMPANY = "Ph", _("Pharmaceutical Company")
    SUPPLYER = "S", _("Supplyer")
    DENTAL_CLINIC = "DC", _("Dental Clinic")
    PRIVATE_CLINIC = "PC", _("Private Clinic")
    GEROCERY = "G", _("Grocery Store")  # بقالة
    BOOK_STORE = "BS", _("Bookstore")  # مكتبة
    COFFEE = "CO", _("Coffee")  # المقهى
    BAKERY = "BA", _("Bakery")  # مخبز
    DELICATESSEN = "DE", _("Delicatessen")  # محل بيع لحوم
    SCHOOL = "Sc", _("School")  # مدرسة
    CAFE = "CA", _("café")  # كافيه
    LAUNDROMAT = "LA", _("Laundromat")  # مغسلة
    HOTAL = "H", _("Hotel")  # الفندق
    BUTCHER = "BU", _("Butcher")  # لجزار
    SUPER_MARKET = "SM", _("SuperMarket ")  # سوبر ماركت
    GIFT_SHOP = "GS", _("Gift Shop")  # محل الهدايا
    FLOWER_SHOP = "FS", _("Flower Shop")  # محل الزهور
    SPORTING_GOODS_STORE = "SG", _("Sporting Goods Store	")  # محل ادوات رياضية
    ELECTRONICS_STORE = "ES", _("Electronics Store")  # محل الكترونيات
    BARBER = "B", _("Barber")
    PHARMACY = "P", _("Pharmacy")
    MEDICAL_FACILITY = "MF", _("Medical Facility")
    MOBILE_NETWORK = "MN", _("Mobile Network Compnay")


class SCORES(TextChoices):
    ONE = "1", _("1")
    TWO = "2", _("2")
    THREE = "3", _("3")


class RUNS(TextChoices):
    SAME_DAY = "SD", _("Same Day")
    NEXT_DAY = "ND", _("Next Day")
    AFTER_2_DAYS = "2D", _("After 2Days")
    AFTER_4_DAYS = "4D", _("After 4Days")
    AFTER_10_DAYS = "10", _("After 10Days")
    AFTER_WEEK = "AW", _("After Week")
    AFTER_2_WEEK = "2W", _("After Two Week")
    AFTER_MONTH = "AM", _("After Month")
    SATURDAY = f"{calendar.SATURDAY}", _("Saturday")
    SUNDAY = f"{calendar.SUNDAY}", _("Sunday")
    MONDAY = f"{calendar.MONDAY}", _("Monday")
    TUESDAY = f"{calendar.TUESDAY}", _("Tuesday")
    WEDNESDAY = f"{calendar.WEDNESDAY}", _("Wednesday")
    THURSDAY = f"{calendar.THURSDAY}", _("Thursday")
    FRIDAY = f"{calendar.FRIDAY}", _("Friday")
    # Saturday = "Sat", _(calendar.day_name[0])
    # Sunday = "Sun", _(calendar.day_name[1])
    # Monday = "Mon", _(calendar.day_name[2])
    # Tuesday = "Tue", _(calendar.day_name[3])
    # Wednesday = "Wed", _(calendar.day_name[4])
    # Thursday = "Thu", _(calendar.day_name[5])
    # Friday = "Fri", _(calendar.day_name[6])


class PRODUCT_TRANSACTIONS_TYPES(TextChoices):
    IMPORTED_PRODUCTS = "I", _("Imported Products")
    EXPORTED_PRODUCTS = "E", _("Exported Products")


class PLATFORMS(TextChoices):
    ANDROID = "A", _("Android")
    IOS = "i", _("ios")
    WINDOWS = "W", _("Windows")
    LINUX = "L", _("Linux")
    BROWSER = "B", _("Web Browser")


class DEVICES_TYPES(TextChoices):
    MOBILE = "M", _("Mobile")
    TABLITE = "T", _("Tablete")
    TAB_TOP = "L", _("Lab Top")
    MAC = "P", _("Mac")
