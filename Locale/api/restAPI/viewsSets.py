from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)  # noqa: F401
from Api.restAPI.permissions import IsAdminOrReadOnly
from rest_framework.authentication import (
    TokenAuthentication,
    SessionAuthentication,
    BasicAuthentication,
)
from rest_framework import filters
import django_filters.rest_framework

from Locale.models import Locale, Language
from .serializers import LocaleSerializer, LanguageSerializer, AppLocaleSerializer


class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAdminOrReadOnly]
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]
    filter_backends = (
        filters.OrderingFilter,  # http://example.com/api/users?ordering=account,username
        filters.SearchFilter,  # http://example.com/api/users?search=russell
        django_filters.rest_framework.DjangoFilterBackend,
    )
    ordering_fields = ("id", "created_at", "last_updated")
    filterset_fields = ["id", "created_at", "last_updated"]
    search_fields = [
        "name",
        "native_name",
        "language_iso_code",
        "is_bidirectional",
    ]
    # This will be used as the default ordering
    ordering = "-last_updated"


class LocaleViewSet(ModelViewSet):
    queryset = Locale.objects.all()
    serializer_class = LocaleSerializer
    permission_classes = [IsAdminOrReadOnly]
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]
    filter_backends = (
        filters.OrderingFilter,  # http://example.com/api/users?ordering=account,username
        filters.SearchFilter,  # http://example.com/api/users?search=russell
        django_filters.rest_framework.DjangoFilterBackend,
    )
    ordering_fields = ("id", "created_at", "last_updated")
    filterset_fields = ["id", "created_at", "last_updated"]
    search_fields = [
        "language",
        "country",
        "locale_code",
    ]
    # This will be used as the default ordering
    ordering = "-last_updated"


class AppLocaleViewSet(ModelViewSet):
    queryset = Locale.objects.all()
    serializer_class = AppLocaleSerializer
    permission_classes = [IsAdminOrReadOnly]
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]
