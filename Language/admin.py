from django.contrib import admin
from django.utils.safestring import mark_safe

from Language.models import Language, Locale

# Register your models here.


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("language_iso_code", "name", "native_name", "is_bidirectional")
    list_filter = ["is_bidirectional"]
    search_fields = ("language_iso_code", "name", "native_name")


@admin.register(Locale)
class LocaleAdmin(admin.ModelAdmin):
    list_display = (
        "locale_code",
        "language_native_name",
        "show_locale_flag",
        "is_app_suport",
    )
    list_editable = ["is_app_suport"]
    list_filter = ("language", "is_app_suport")
    search_fields = ("locale_code", "language_native_name")
    autocomplete_fields = ["language"]

    def show_locale_flag(self, obj: "Locale"):
        if obj.locale_flag:
            return mark_safe(
                f'<img src="{obj.locale_flag}" style="max-height: 50px;" />'
            )
        return "No flag"

    show_locale_flag.short_description = "Flag Preview"

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
