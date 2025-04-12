from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import (
    TokenAuthentication,
    SessionAuthentication,
    BasicAuthentication,
)
from rest_framework import filters
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

import django_filters.rest_framework

from Api.permissions import IsAdminOrReadOnlyForUser
from Category.models import Category
from .serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnlyForUser]

    # # Define custom permission classes for each action
    # permission_classes_by_action = {
    #     "create": [IsAuthenticated],
    #     "list": [AllowAny],
    #     "retrieve": [AllowAny],
    #     "destroy": [
    #         IsAdmin,
    #         # IsOwner | IsAdmin,
    #     ],
    # }

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

    # # You might also want to restrict creation to admins only
    # def perform_create(self, serializer):
    #     if not self.request.user.is_admin:
    #         raise PermissionDenied("Only Admins can create this resource.")
    #     serializer.save(
    #         user=self.request.user
    #     )  # Assuming your model has a 'user' field
