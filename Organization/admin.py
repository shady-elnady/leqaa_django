from django.contrib.admin import ModelAdmin, register
from django.db.models import JSONField

from Locale.widgets.myTranslation_json_widget import MyTranslationWidget
from Organization.models import OrganizationType, College, University
from .forms import (
    OrganizationTypeAdminForm,
    CollegeAdminForm,
    UniversityAdminForm,
)

# Register your models here.


@register(OrganizationType)
class OrganizationTypeAdmin(ModelAdmin):
    form = OrganizationTypeAdminForm
    formfield_overrides = {
        JSONField: {
            "widget": MyTranslationWidget,
        },
    }


@register(College)
class CollegeAdmin(ModelAdmin):
    form = CollegeAdminForm
    formfield_overrides = {
        JSONField: {
            "widget": MyTranslationWidget,
        },
    }


@register(University)
class UniversityAdmin(ModelAdmin):
    form = UniversityAdminForm
    formfield_overrides = {
        JSONField: {
            "widget": MyTranslationWidget,
        },
    }
