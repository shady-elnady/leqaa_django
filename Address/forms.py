from django.forms import ModelForm
from django.contrib.admin.widgets import AdminFileWidget

from Address.models import Country, Governorate, City, State, Locality, Street, Location
from Language.widgets.myTranslation_json_widget import MyTranslationWidget
from Firebase.widgets import FirebaseImageWidget


class CountryAdminForm(ModelForm):
    class Meta:
        model = Country
        fields = [
            "id",
            "name",
            "country_code",
            "continent",
            "capital",
            "flag_emoji",
            "image",
            # "firebase_image_url",
            "currency",
            "language",
            "tel_code",
            "time_zone",
            "translations",
        ]
        widgets = {
            "firebase_image_url": FirebaseImageWidget(),
            "image": AdminFileWidget(),  # Regular widget for the flag field
            "translations": MyTranslationWidget,
        }


class GovernorateAdminForm(ModelForm):
    class Meta:
        model = Governorate
        fields = [
            "id",
            "name",
            "country",
            "governorate_tel_code",
            "translations",
        ]


class CityAdminForm(ModelForm):
    class Meta:
        model = City
        fields = [
            "id",
            "name",
            "country",
            "governorate",
            "translations",
        ]


class StateAdminForm(ModelForm):
    class Meta:
        model = State
        fields = [
            "id",
            "name",
            "city",
            "postal_code",
            "state_type",
            "translations",
        ]


class LocalityAdminForm(ModelForm):
    class Meta:
        model = Locality
        fields = [
            "id",
            "name",
            "state",
            "translations",
        ]


class StreetAdminForm(ModelForm):
    class Meta:
        model = Street
        fields = [
            "id",
            "name",
            "state",
            "translations",
        ]


class LocationAdminForm(ModelForm):
    class Meta:
        model = Location
        fields = [
            "id",
            "name",
            "locality",
            "street",
            "address",
            "translations",
        ]
        widgets = {"translations": MyTranslationWidget}


# https://stackoverflow.com/questions/59916324/django-how-to-save-google-maps-polygon-area-javascript-code-to-view
