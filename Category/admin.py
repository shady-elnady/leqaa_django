from django.contrib import admin
from django.db import models

from Locale.widgets.myTranslation_json_widget import MyTranslationWidget
from .forms import CategoryAdminForm
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    formfield_overrides = {
        models.JSONField: {
            "widget": MyTranslationWidget,
        },
    }
