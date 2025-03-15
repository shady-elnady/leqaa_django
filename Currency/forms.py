from django.forms import ModelForm

from .models import Currency


class CurrencyAdminForm(ModelForm):
    class Meta:
        model = Currency
        fields = [
            "name",
            "iso_code",
            "symbol",
            "translations",
            "exchange_rates",
        ]
