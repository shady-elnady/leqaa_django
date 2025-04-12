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

from Payment.models import PaymentMethod, PaymentStatus, Transaction
from .serializers import (
    PaymentMethodSerializer,
    PaymentStatusSerializer,
    TransactionSerializer,
)


class PaymentMethodViewSet(ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
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
        "payment_Method_type",
    ]
    # This will be used as the default ordering
    ordering = "-last_updated"


class PaymentStatusViewSet(ModelViewSet):
    queryset = PaymentStatus.objects.all()
    serializer_class = PaymentStatusSerializer
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
        "payment_status_type",
    ]
    # This will be used as the default ordering
    ordering = "-last_updated"


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
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
        "transactor",
        "reservation",
        "payment_status",
        "payment_method",
        "currency",
        "due_date",
        "notified_days",
        "reference_number",
        "bank_deposit_date",
        "bank_name",
        "comment",
        "total_required_amount",
        "amount",
        "remaining_amount",
        "created_at",
        "last_updated",
    ]
    # This will be used as the default ordering
    ordering = "-last_updated"
