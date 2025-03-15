from django.forms import ModelForm

from Payment.models import PaymentMethod, PaymentStatus


class PaymentMethodAdminForm(ModelForm):
    class Meta:
        model = PaymentMethod
        fields = [
            "name",
            "payment_Method_type",
            "translations",
        ]


class PaymentStatusAdminForm(ModelForm):
    class Meta:
        model = PaymentStatus
        fields = [
            "name",
            "payment_status_type",
            "translations",
        ]
