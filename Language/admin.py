from django.contrib import admin

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
        "language",
        "language_native_name",
        "locale_flag",
        "is_app_suport",
    )
    list_editable = ["is_app_suport"]
    list_filter = ("language", "is_app_suport")
    search_fields = ("locale_code", "language_native_name")
    autocomplete_fields = ["language"]
