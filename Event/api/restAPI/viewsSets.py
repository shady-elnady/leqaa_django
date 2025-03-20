from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (
    TokenAuthentication,
    SessionAuthentication,
    BasicAuthentication,
)
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters import rest_framework as filters

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from Api.restAPI.permissions import IsAdminOrReadOnlyForUser
from Category.api.restAPI.serializers import CategorySerializer
from Category.models import Category
from Event.models import Event, EventType, EventAlbum
from .serializers import (
    EventSerializer,
    EventTypeSerializer,
    EventAlbumSerializer,
    MultipleImageEventAlbumSerializer,
)


class EventTypeViewSet(ModelViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer
    permission_classes = [IsAdminOrReadOnlyForUser]
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]
    filter_backends = (
        OrderingFilter,  # http://example.com/api/users?ordering=account,username
        SearchFilter,  # http://example.com/api/users?search=russell
        filters.DjangoFilterBackend,
    )
    ordering_fields = ("id", "created_at", "last_updated")
    filterset_fields = ["id", "created_at", "last_updated"]
    search_fields = ["name"]
    # This will be used as the default ordering
    ordering = "-last_updated"


class EventFilter(filters.FilterSet):
    category__in = filters.ModelMultipleChoiceFilter(
        field_name="category",
        queryset=Category.objects.all(),
        lookup_expr="in",
        method="filter_category",
    )

    def filter_category(self, queryset, name, value):
        if value:
            return queryset.filter(category__in=value)
        return queryset

    class Meta:
        model = Event
        fields = ["category__in", "category__id"]


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdminOrReadOnlyForUser]
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]
    filter_backends = (
        OrderingFilter,  # http://example.com/api/users?ordering=account,username
        SearchFilter,  # http://example.com/api/users?search=russell
        filters.DjangoFilterBackend,
    )
    filterset_class = EventFilter
    ordering_fields = ("id", "created_at", "last_updated")
    search_fields = ["title"]
    # This will be used as the default ordering
    ordering = "-last_updated"

    # def list(self, request, *args, **kwargs):
    #     print(request.query_params)  # Add this line
    #     return super().list(request, *args, **kwargs)


class EventAlbumViewSet(ModelViewSet):
    queryset = EventAlbum.objects.all()
    serializer_class = EventAlbumSerializer
    permission_classes = [IsAdminOrReadOnlyForUser]
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]
    filter_backends = (
        OrderingFilter,  # http://example.com/api/users?ordering=account,username
        SearchFilter,  # http://example.com/api/users?search=russell
        filters.DjangoFilterBackend,
    )
    ordering_fields = ("id", "created_at", "last_updated")
    filterset_fields = ["id", "created_at", "last_updated"]
    search_fields = [
        "event.title",
        "order",
    ]
    # This will be used as the default ordering
    ordering = "-last_updated"

    @action(detail=False, methods=["POST"])
    def multiple_upload(self, request, *args, **kwargs):
        """Upload multiple Photos and create objects."""
        serializer = MultipleImageEventAlbumSerializer(data=request.data or None)
        serializer.is_valid(raise_exception=True)
        photos = serializer.validated_data.get("photos")

        photos_list = []
        for photo in photos:
            photos_list.append(EventAlbum(photo=photo))
        if photos_list:
            EventAlbum.objects.bulk_create(photos_list)

        return Response("Success")
