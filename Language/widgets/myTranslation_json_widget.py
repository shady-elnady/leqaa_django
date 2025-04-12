from django.forms import Widget
from builtins import super

from Language.models import Locale


class MyTranslationWidget(Widget):
    # # Add CSS
    # class Media:
    #     js = (
    #         getattr(settings, "JSON_EDITOR_JS", 'dist/jsoneditor.min.js'),
    #     )
    #     css = {
    #         'all': (
    #             getattr(settings, "JSON_EDITOR_CSS", 'dist/jsoneditor.min.css'),
    #         )
    #     }

    template_name = "widgets/myTranslation_json_widget.html"

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
