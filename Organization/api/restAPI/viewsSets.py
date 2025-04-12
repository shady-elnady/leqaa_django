from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (
    TokenAuthentication,
    SessionAuthentication,
    BasicAuthentication,
)
from rest_framework import filters
import django_filters.rest_framework
from Api.permissions import IsAdminOrReadOnlyForUser

from Organization.models import Organization, OrganizationType, College, University
from .serializers import (
    OrganizationSerializer,
    OrganizationTypeSerializer,
    CollegeSerializer,
    UniversitySerializer,
)


class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
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
    search_fields = ["name"]
    # This will be used as the default ordering
    ordering = "-last_updated"


class OrganizationTypeViewSet(ModelViewSet):
    queryset = OrganizationType.objects.all()
    serializer_class = OrganizationTypeSerializer
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
    search_fields = ["name"]
    # This will be used as the default ordering
    ordering = "-last_updated"


class CollegeViewSet(ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
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
    search_fields = ["name"]
    # This will be used as the default ordering
    ordering = "-last_updated"


class UniversityViewSet(ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
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
    search_fields = ["name"]
    # This will be used as the default ordering
    ordering = "-last_updated"
