from django.contrib.admin import ModelAdmin, register
from django.db.models import JSONField

from Locale.widgets.myTranslation_json_widget import MyTranslationWidget
from Address.models import Country, Governorate, City, State, Locality, Street, Address

from .forms import (
    CountryAdminForm,
    GovernorateAdminForm,
    CityAdminForm,
    StateAdminForm,
    LocalityAdminForm,
    StreetAdminForm,
    AddressAdminForm,
)

# Register your models here.


@register(Country)
class CountryAdmin(ModelAdmin):
    form = CountryAdminForm
    formfield_overrides = {
        JSONField: {
            "widget": MyTranslationWidget,
        },
    }


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


@register(Address)
class AddressAdmin(ModelAdmin):
    form = AddressAdminForm
