from django.db.models import TextChoices
import calendar

from App.messages import ChoicesMessages

# Create your TextChoices here.


class WeekDays(TextChoices):
    SATURDAY = f"{calendar.SATURDAY}", ChoicesMessages.SATURDAY
    SUNDAY = f"{calendar.SUNDAY}", ChoicesMessages.SUNDAY
    MONDAY = f"{calendar.MONDAY}", ChoicesMessages.MONDAY
    TUESDAY = f"{calendar.TUESDAY}", ChoicesMessages.TUESDAY
    WEDNESDAY = f"{calendar.WEDNESDAY}", ChoicesMessages.WEDNESDAY
    THURSDAY = f"{calendar.THURSDAY}", ChoicesMessages.THURSDAY
    FRIDAY = f"{calendar.FRIDAY}", ChoicesMessages.FRIDAY


class FacilityTypes(TextChoices):
    LABORATORY = "L", ChoicesMessages.LABORATORY
    MAIN_LABORATORY = "ML", ChoicesMessages.MAIN_LABORATORY
    ASSOCIATIONS = "A", ChoicesMessages.ASSOCIATIONS
    DISPENSARY = "D", ChoicesMessages.DISPENSARY
    SCIENTIFIC_COMPANY = "SC", ChoicesMessages.SCIENTIFIC_COMPANY
    PHARMACEUTICAL_COMPANY = "Ph", ChoicesMessages.PHARMACEUTICAL_COMPANY
    SUPPLIER = "S", ChoicesMessages.SUPPLIER
    DENTAL_CLINIC = "DC", ChoicesMessages.DENTAL_CLINIC
    PRIVATE_CLINIC = "PC", ChoicesMessages.PRIVATE_CLINIC
    GROCERY_STORE = "G", ChoicesMessages.GROCERY_STORE
    BOOKSTORE = "BS", ChoicesMessages.BOOKSTORE
    COFFEE_SHOP = "CO", ChoicesMessages.COFFEE
    BAKERY = "BA", ChoicesMessages.BAKERY
    DELICATESSEN = "DE", ChoicesMessages.DELICATESSEN
    SCHOOL = "Sc", ChoicesMessages.SCHOOL
    CAFE = "CA", ChoicesMessages.CAFE
    LAUNDROMAT = "LA", ChoicesMessages.LAUNDROMAT
    HOTEL = "H", ChoicesMessages.HOTEL
    BUTCHER = "BU", ChoicesMessages.BUTCHER
    SUPERMARKET = "SM", ChoicesMessages.SUPERMARKET
    GIFT_SHOP = "GS", ChoicesMessages.GIFT_SHOP
    FLOWER_SHOP = "FS", ChoicesMessages.FLOWER_SHOP
    SPORTING_GOODS_STORE = "SG", ChoicesMessages.SPORTING_GOODS_STORE
    ELECTRONICS_STORE = "ES", ChoicesMessages.ELECTRONICS_STORE
    BARBER = "B", ChoicesMessages.BARBER
    PHARMACY = "P", ChoicesMessages.PHARMACY
    MEDICAL_FACILITY = "MF", ChoicesMessages.MEDICAL_FACILITY
    MOBILE_NETWORK = "MN", ChoicesMessages.MOBILE_NETWORK


class SCORES(TextChoices):
    ONE = "1", ChoicesMessages.ONE
    TWO = "2", ChoicesMessages.TWO
    THREE = "3", ChoicesMessages.THREE


class RUNS(TextChoices):
    SAME_DAY = "SD", ChoicesMessages.SAME_DAY
    NEXT_DAY = "ND", ChoicesMessages.NEXT_DAY
    AFTER_2_DAYS = "2D", ChoicesMessages.AFTER_2_DAYS
    AFTER_4_DAYS = "4D", ChoicesMessages.AFTER_4_DAYS
    AFTER_10_DAYS = "10", ChoicesMessages.AFTER_10_DAYS
    AFTER_WEEK = "AW", ChoicesMessages.AFTER_WEEK
    AFTER_2_WEEK = "2W", ChoicesMessages.AFTER_2_WEEK
    AFTER_MONTH = "AM", ChoicesMessages.AFTER_MONTH
    SATURDAY = f"{calendar.SATURDAY}", ChoicesMessages.SATURDAY
    SUNDAY = f"{calendar.SUNDAY}", ChoicesMessages.SUNDAY
    MONDAY = f"{calendar.MONDAY}", ChoicesMessages.MONDAY
    TUESDAY = f"{calendar.TUESDAY}", ChoicesMessages.TUESDAY
    WEDNESDAY = f"{calendar.WEDNESDAY}", ChoicesMessages.WEDNESDAY
    THURSDAY = f"{calendar.THURSDAY}", ChoicesMessages.THURSDAY
    FRIDAY = f"{calendar.FRIDAY}", ChoicesMessages.FRIDAY


class ProductTransactionTypes(TextChoices):
    IMPORTED = "I", ChoicesMessages.IMPORTED_PRODUCTS
    EXPORTED = "E", ChoicesMessages.EXPORTED_PRODUCTS


class PLATFORMS(TextChoices):
    ANDROID = "A", ChoicesMessages.ANDROID
    IOS = "i", ChoicesMessages.IOS
    WINDOWS = "W", ChoicesMessages.WINDOWS
    LINUX = "L", ChoicesMessages.LINUX
    BROWSER = "B", ChoicesMessages.BROWSER


class DeviceTypes(TextChoices):
    MOBILE = "M", ChoicesMessages.MOBILE
    TABLET = "T", ChoicesMessages.TABLET
    LAPTOP = "L", ChoicesMessages.LAPTOP
    MAC = "P", ChoicesMessages.MAC
