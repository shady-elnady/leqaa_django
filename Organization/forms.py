from django.forms import ModelForm

from Organization.models import Organization, OrganizationType, College, University


class OrganizationTypeAdminForm(ModelForm):
    class Meta:
        model = OrganizationType
        fields = [
            "id",
            "name",
            "translations",
        ]


class OrganizationAdminForm(ModelForm):
    class Meta:
        model = Organization
        fields = [
            "id",
            "name",
            "logo",
            "organization_type",
            "university",
            "affiliated_to",
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
