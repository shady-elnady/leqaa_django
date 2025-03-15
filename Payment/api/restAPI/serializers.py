from rest_framework.serializers import HyperlinkedModelSerializer

from Payment.models import PaymentMethod, PaymentStatus, Transaction
from Currency.api import CurrencySerializer
from Reservation.api import ReservationSerializer
from User.api import UserSerializer

# Serializers define the API representation.


class PaymentMethodSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = [
            "url",
            "id",
            "name",
            "payment_Method_type",
            "translations",
            "created_at",
            "last_updated",
        ]


class PaymentStatusSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = PaymentStatus
        fields = [
            "url",
            "id",
            "name",
            "payment_status_type",
            "translations",
            "created_at",
            "last_updated",
        ]


class TransactionSerializer(HyperlinkedModelSerializer):
    transactor = UserSerializer(many=False)
    reservation = ReservationSerializer(many=False)
    payment_status = PaymentStatusSerializer(many=False)
    payment_method = PaymentMethodSerializer(many=False)
    currency = CurrencySerializer(many=False)

    class Meta:
        model = Transaction
        fields = [
            "url",
            "id",
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
