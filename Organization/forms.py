from django.forms import ModelForm

from Organization.models import OrganizationType, College, University


class OrganizationTypeAdminForm(ModelForm):
    class Meta:
        model = OrganizationType
        fields = [
            "id",
            "name",
            "translations",
        ]


class CollegeAdminForm(ModelForm):
    class Meta:
        model = College
        fields = [
            "id",
            "name",
            "logo",
            "university",
            "translations",
        ]


class UniversityAdminForm(ModelForm):
    class Meta:
        model = University
        fields = [
            "id",
            "name",
            "logo",
            "email",
            "translations",
        ]
