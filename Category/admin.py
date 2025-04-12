from typing import Optional
from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe

from Language.widgets.myTranslation_json_widget import MyTranslationWidget
from .forms import CategoryAdminForm
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = (
        "name",
        "show_photo",
        "created_at",
        "last_updated",
    )
    readonly_fields = ("firebase_image_url",)
    formfield_overrides = {
        models.JSONField: {
            "widget": MyTranslationWidget,
        },
    }

    def show_photo(self, obj: "Category"):
        photo: Optional[str] = (
            obj.firebase_image_url if obj.firebase_image_url else obj.image.url
        )
        if photo:
            return mark_safe(f'<img src="{photo}" style="max-height: 50px;" />')
        return "No Photo"

    show_photo.short_description = "Photo Preview"
    show_photo.allow_tags = True

    class Media:
        css = {
            "all": (
                "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css",
            )
        }
        js = (
            "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js",
            "admin/js/firebase_upload.js",  # We'll create this next
        )
