from django.contrib import admin
from django.db import models

from Language.widgets.myTranslation_json_widget import MyTranslationWidget
from .forms import CurrencyAdminForm
from .models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    form = CurrencyAdminForm
    formfield_overrides = {
        models.JSONField: {
            "widget": MyTranslationWidget,
        },
    }
