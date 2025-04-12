from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (
    TokenAuthentication,
    SessionAuthentication,
    BasicAuthentication,
)
from rest_framework import filters
import django_filters.rest_framework

from Advertisement.models import Advertisement
from Api.permissions import IsAdminOrReadOnlyForUser
from .serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnlyForUser]
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
    search_fields = ["title"]
    # This will be used as the default ordering
    ordering = "-last_updated"
