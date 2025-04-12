from django.contrib.admin import ModelAdmin, register
from django.db.models import JSONField
from django.utils.safestring import mark_safe

from Language.widgets.myTranslation_json_widget import MyTranslationWidget
from Address.models import Country, Governorate, City, State, Locality, Street, Location

from .forms import (
    CountryAdminForm,
    GovernorateAdminForm,
    CityAdminForm,
    StateAdminForm,
    LocalityAdminForm,
    StreetAdminForm,
    LocationAdminForm,
)

# Register your models here.


@register(Country)
class CountryAdmin(ModelAdmin):
    form = CountryAdminForm
    list_display = ("name", "country_code", "show_flag")

    def show_flag(self, obj: "Country"):
        if obj.firebase_image_url:
            return mark_safe(
                f'<img src="{obj.firebase_image_url}" style="max-height: 50px;" />'
            )
        return "No flag"

    show_flag.short_description = "Flag Preview"

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


@register(Governorate)
class GovernorateAdmin(ModelAdmin):
    form = GovernorateAdminForm
    formfield_overrides = {
        JSONField: {
            "widget": MyTranslationWidget,
        },
    }


@register(City)
class CityAdmin(ModelAdmin):
    form = CityAdminForm
    formfield_overrides = {
        JSONField: {
            "widget": MyTranslationWidget,
        },
    }


@register(State)
class StateAdmin(ModelAdmin):
    form = StateAdminForm
    formfield_overrides = {
        JSONField: {
            "widget": MyTranslationWidget,
        },
    }


@register(Locality)
class LocalityAdmin(ModelAdmin):
    form = LocalityAdminForm
    formfield_overrides = {
        JSONField: {
            "widget": MyTranslationWidget,
        },
    }


@register(Street)
class StreetAdmin(ModelAdmin):
    form = StreetAdminForm
    formfield_overrides = {
        JSONField: {
            "widget": MyTranslationWidget,
        },
    }


@register(Location)
class LocationAdmin(ModelAdmin):
    form = LocationAdminForm
