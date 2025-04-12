from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
import django_filters.rest_framework

from Address.models import (
    Location,
    Locality,
    Street,
    State,
    City,
    Governorate,
    Country,
)
from .serializers import (
    LocationSerializer,
    StateSerializer,
    LocalitySerializer,
    CitySerializer,
    CountrySerializer,
    GovernorateSerializer,
    StreetSerializer,
)


class LocationViewSet(ModelViewSet):
    """
    API endpoint that allows Locations to be viewed or edited.
    """

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (
        filters.OrderingFilter,  # http://example.com/api/users?ordering=account,username
        filters.SearchFilter,  # http://example.com/api/users?search=russell
        django_filters.rest_framework.DjangoFilterBackend,
    )
    ordering_fields = ("id", "created_at", "last_updated")
    filterset_fields = ["id", "created_at", "last_updated"]
    search_fields = ["name"]
    # This will be used as the default ordering
    ordering = "-last_updated"


"""
    ?page=1&size=15&sorters[0]

    http://example.com/api/users?ordering=account,username

"""


class StreetViewSet(ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.OrderingFilter,)


# https://github.com/openwisp/django-rest-framework-gis#using-geometryserializermethodfield-as-geo_field
# https://docs.djangoproject.com/en/2.0/ref/contrib/gis/functions/


class LocalityViewSet(ModelViewSet):
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.OrderingFilter,)
    # Explicitly specify which fields the API may be ordered against
    ordering_fields = ("id", "created_at", "name")
    # This will be used as the default ordering
    ordering = "last_updated"


class StateViewSet(ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.OrderingFilter,)
    # Explicitly specify which fields the API may be ordered against
    ordering_fields = ("id", "created_at", "name")
    # This will be used as the default ordering
    ordering = "last_updated"


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.OrderingFilter,)
    # Explicitly specify which fields the API may be ordered against
    ordering_fields = ("id", "created_at", "name")
    # This will be used as the default ordering
    ordering = "last_updated"


class GovernorateViewSet(ModelViewSet):
    queryset = Governorate.objects.all()
    serializer_class = GovernorateSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (
        filters.OrderingFilter,
        # DjangoFilterBackend,
    )
    # Explicitly specify which fields the API may be ordered against
    ordering_fields = ("id", "created_at", "name")
    # This will be used as the default ordering
    ordering = "last_updated"


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (
        filters.OrderingFilter,  # http://example.com/api/users?ordering=account,username
        filters.SearchFilter,  # http://example.com/api/users?search=russell
        django_filters.rest_framework.DjangoFilterBackend,
    )
    ordering_fields = ("id", "created_at", "last_updated")
    filterset_fields = ["id", "created_at", "last_updated"]
    search_fields = [
        "name",
        "country_code",
        "continent",
        "capital",
        "flag_emoji",
        "currency",
        "language",
        "tel_code",
        "time_zone",
        "translations",
    ]
    # This will be used as the default ordering
