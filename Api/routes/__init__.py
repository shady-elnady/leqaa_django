from rest_framework import routers
from Advertisement.api import AdvertisementViewSet
from Event.api import EventAlbumViewSet, EventTypeViewSet, EventViewSet
from Language.api import LocaleViewSet, LanguageViewSet, AppLocaleViewSet
from Category.api import CategoryViewSet
from Currency.api import CurrencyViewSet
from Address.api import (
    LocationViewSet,
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
from Reservation.api import ReservationViewSet, UserReservationsViewSet
from Notification.api import NotificationViewSet, UserNotificationsViewSet
from Favorite.api import FavoriteViewSet, UserFavoritesViewSet
from User.api import (
    ProfileViewSet,
    UserViewSet,
    StudentViewSet,
    LecturerViewSet,
    UserAlbumViewSet,
    InterestViewSet,
    UserInterestsViewSet,
    UserMyProfileViewSet,
    MyAccountViewSet,
)
from Api.views import RegisterViewSet

router = routers.DefaultRouter()

# Api
router.register(r"register", RegisterViewSet, basename="register")
# Locale
router.register(r"languages", LanguageViewSet, basename="language")
router.register(r"app-locales", AppLocaleViewSet, basename="app-locale")
router.register(r"locales", LocaleViewSet, basename="locale")
# Currency
router.register(r"currencies", CurrencyViewSet, basename="currency")
# Category
router.register(r"categories", CategoryViewSet, basename="category")
# Advertisement
router.register(r"advertisements", AdvertisementViewSet, basename="advertisement")
# Address
router.register(r"countries", CountryViewSet, basename="country")
router.register(r"governorates", GovernorateViewSet, basename="governorate")
router.register(r"cities", CityViewSet, basename="city")
router.register(r"localities", LocalityViewSet, basename="locality")
router.register(r"states", StateViewSet, basename="state")
router.register(r"streets", StreetViewSet, basename="street")
router.register(r"locations", LocationViewSet, basename="locations")
# User
router.register(r"users", UserViewSet, basename="user")
router.register(r"students", StudentViewSet, basename="student")
router.register(r"lecturers", LecturerViewSet, basename="lecturer")
router.register(r"Users-Albums", UserAlbumViewSet)
router.register(r"profiles", ProfileViewSet, basename="profile")
router.register(r"interests", InterestViewSet, basename="interest")
router.register(r"my-account", MyAccountViewSet, basename="myAccount")
# router.register(
#     r"users/(?P<user_id>\d+)/interests", UserInterestsViewSet, basename="user-interests"
# )
router.register(r"user/my-interests", UserInterestsViewSet, basename="user-interests")
router.register(r"user/my-profile", UserMyProfileViewSet, basename="user-profile")

# Organization
router.register(r"organizations", OrganizationViewSet, basename="organization")
router.register(r"organizations-types", OrganizationTypeViewSet)
router.register(r"colleges", CollegeViewSet, basename="college")
router.register(r"universities", UniversityViewSet, basename="university")
# Event
router.register(r"events", EventViewSet, basename="event")
router.register(r"events-types", EventTypeViewSet)
router.register(r"events-Albums", EventAlbumViewSet)
# Reservation
router.register(r"reservations", ReservationViewSet, basename="reservation")
router.register(
    r"user/my-reservations", UserReservationsViewSet, basename="user-reservations"
)
# Payment
router.register(r"payment-methods", PaymentMethodViewSet)
router.register(r"payment-statuses", PaymentStatusViewSet)
router.register(r"transactions", TransactionViewSet, basename="transaction")
# Notification
router.register(r"notifications", NotificationViewSet, basename="notification")
router.register(
    r"user/my-notifications", UserNotificationsViewSet, basename="user-notifications"
)
# Favorite
router.register(r"favorites", FavoriteViewSet, basename="favorite")
router.register(r"user/my-favorites", UserFavoritesViewSet, basename="user-favorites")
