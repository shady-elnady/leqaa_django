import json  # noqa: F401
from builtins import super

from django import forms
from django.conf import settings  # noqa: F401

from Locale.models import Locale


class MyTranslationWidget(forms.Widget):
    # class Media:
    #     js = (
    #         getattr(settings, "JSON_EDITOR_JS", 'dist/jsoneditor.min.js'),
    #     )
    #     css = {
    #         'all': (
    #             getattr(settings, "JSON_EDITOR_CSS", 'dist/jsoneditor.min.css'),
    #         )
    #     }

    template_name = "Widgets/myTranslation_json_widget.html"

    def __init__(
        self,
        attrs=None,
        locales=Locale.objects.filter(is_app_suport=True),
    ):
        self.locales = locales
        super(MyTranslationWidget, self).__init__(attrs=attrs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"]["locales"] = self.locales
        return context
