from django.forms import Widget


class MobileInput(Widget):
    input_type = "text"
    template_name = "widgets/mobile.html"
