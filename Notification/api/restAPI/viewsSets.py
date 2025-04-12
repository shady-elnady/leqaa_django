from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import (
    TokenAuthentication,
    SessionAuthentication,
    BasicAuthentication,
)
from App.messages import AuthMessages
from rest_framework import filters
import django_filters.rest_framework
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status

from Notification.models import Notification
from .serializers import NotificationSerializer


class NotificationViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAdminUser]
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
        "user",
        "category",
    ]
    # This will be used as the default ordering
    ordering = "-last_updated"


class UserNotificationsViewSet(ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        if serializer.validated_data.get("user") is None:
            serializer.save(user=self.request.user)
        else:
            serializer.save()

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_queryset().get(pk=kwargs["pk"])
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Notification.DoesNotExist:
            raise NotFound(AuthMessages.NOT_FOUND)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_queryset().get(pk=kwargs["pk"])
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        except Notification.DoesNotExist:
            raise NotFound(AuthMessages.NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_queryset().get(pk=kwargs["pk"])
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Notification.DoesNotExist:
            raise NotFound(AuthMessages.NOT_FOUND)
