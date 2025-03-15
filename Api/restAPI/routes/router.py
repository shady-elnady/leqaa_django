from rest_framework import routers
from Advertisement.api import AdvertisementViewSet
from Event.api import EventAlbumViewSet, EventTypeViewSet, EventViewSet
from Locale.api import LocaleViewSet, LanguageViewSet, AppLocaleViewSet
from Category.api import CategoryViewSet
from Currency.api import CurrencyViewSet
from Address.api import (
    AddressViewSet,
    CityViewSet,
    CountryViewSet,
    GovernorateViewSet,
    LocalityViewSet,
    StateViewSet,
    StreetViewSet,
)
from Organization.api import (
    CollegeViewSet,
    OrganizationTypeViewSet,
    OrganizationViewSet,
    UniversityViewSet,
)
from Payment.api import (
    PaymentMethodViewSet,
    PaymentStatusViewSet,
    TransactionViewSet,
)
from Reservation.api import ReservationViewSet
from User.api import (
    ProfileViewSet,
    UserViewSet,
    StudentViewSet,
    LecturerViewSet,
    UserAlbumViewSet,
    InterestViewSet,
)
from Api.restAPI import RegisterViewSet

router = routers.DefaultRouter()

# Api
router.register("register", RegisterViewSet, basename="register")
# Locale
router.register("languages", LanguageViewSet, basename="language")
router.register("app-locales", AppLocaleViewSet, basename="app-locale")
router.register("locales", LocaleViewSet, basename="locale")
# Currency
router.register("currencies", CurrencyViewSet, basename="currency")
# Category
router.register("categories", CategoryViewSet, basename="category")
# Advertisement
router.register("advertisements", AdvertisementViewSet, basename="advertisement")
# Address
router.register("countries", CountryViewSet, basename="country")
router.register("governorates", GovernorateViewSet, basename="governorate")
router.register("cities", CityViewSet, basename="city")
router.register("localities", LocalityViewSet, basename="locality")
router.register("states", StateViewSet, basename="state")
router.register("streets", StreetViewSet, basename="street")
router.register("address", AddressViewSet, basename="address")
# User
router.register("users", UserViewSet, basename="user")
router.register("students", StudentViewSet, basename="student")
router.register("lecturers", LecturerViewSet, basename="lecturer")
router.register("Users-Albums", UserAlbumViewSet)
router.register("profiles", ProfileViewSet, basename="profile")
router.register("interests", InterestViewSet, basename="interest")
# Organization
router.register("organizations", OrganizationViewSet, basename="organization")
router.register("organizations-types", OrganizationTypeViewSet)
router.register("colleges", CollegeViewSet, basename="college")
router.register("universities", UniversityViewSet, basename="university")
# Event
router.register("events", EventViewSet, basename="event")
router.register("events-types", EventTypeViewSet)
router.register("events-Albums", EventAlbumViewSet)
# Reservation
router.register("reservations", ReservationViewSet, basename="reservation")
# Payment
router.register("payment-methods", PaymentMethodViewSet)
router.register("payment-statuses", PaymentStatusViewSet)
router.register("transactions", TransactionViewSet, basename="transaction")

# Notification
