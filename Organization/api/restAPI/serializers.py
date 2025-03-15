from rest_framework.serializers import HyperlinkedModelSerializer

from Organization.models import Organization, OrganizationType, College, University

# Serializers define the API representation.


class OrganizationTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = OrganizationType
        fields = [
            "url",
            "id",
            "name",
            "translations",
            "created_at",
            "last_updated",
        ]


class UniversitySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = University
        fields = [
            "url",
            "id",
            "name",
            "logo",
            "email",
            "translations",
            "created_at",
            "last_updated",
        ]


class OrganizationSerializer(HyperlinkedModelSerializer):
    organization_type = OrganizationTypeSerializer(many=False)
    university = UniversitySerializer(many=False)

    class Meta:
        model = Organization
        fields = [
            "url",
            "id",
            "name",
            "logo",
            "organization_type",
            "university",
            "affiliated_to",
            "translations",
            "created_at",
            "last_updated",
        ]


class CollegeSerializer(HyperlinkedModelSerializer):
    university = UniversitySerializer(many=False)

    class Meta:
        model = College
        fields = [
            "url",
            "id",
            "name",
            "logo",
            "university",
            "translations",
            "created_at",
            "last_updated",
        ]
