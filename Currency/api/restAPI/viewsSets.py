from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from Api.permissions import IsAdminOrReadOnlyForUser
from rest_framework.authentication import (
    TokenAuthentication,
    SessionAuthentication,
    BasicAuthentication,
)
import django_filters.rest_framework

from Currency.models import Currency
from .serializers import CurrencySerializer


class CurrencyViewSet(ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [IsAdminOrReadOnlyForUser]
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
        # "native",
        "code",
        "symbol",
    ]
    # This will be used as the default ordering
    ordering = "-last_updated"
