from django.contrib import admin
from django.db import models

from Locale.widgets.myTranslation_json_widget import MyTranslationWidget
from Payment.models import PaymentMethod, PaymentStatus
from .forms import PaymentMethodAdminForm, PaymentStatusAdminForm


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    form = PaymentMethodAdminForm
    formfield_overrides = {
        models.JSONField: {
            "widget": MyTranslationWidget,
        },
    }


@admin.register(PaymentStatus)
class PaymentStatusAdmin(admin.ModelAdmin):
    form = PaymentStatusAdminForm
    formfield_overrides = {
        models.JSONField: {
            "widget": MyTranslationWidget,
        },
    }
