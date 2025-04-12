# from django import forms
# from django.utils.safestring import mark_safe
# from django.conf import settings


# class ImageSliderWidget(forms.FileInput):
#     template_name = "Widgets/image_slider.html"  # Create this template

#     # def render(self, name, value, attrs=None, renderer=None):
#     #     context = self.get_context(name, value, attrs)
#     #     return mark_safe(self._render(self.template_name, context, renderer))
#     def __init__(
#         self,
#         attrs=None,
#     ):
#         super(ImageSliderWidget, self).__init__(attrs=attrs)

#     def get_context(self, name, value, attrs):
#         context = super().get_context(name, value, attrs)
#         context["name"] = name
#         context["value"] = value
#         context["id"] = id(str(self))
#         context["MEDIA_URL"] = settings.MEDIA_URL
#         return context
"""

https://stackoverflow.com/questions/1696877/how-to-set-a-value-to-a-file-input-in-html-to-a-client-side-disk-file-system-pat

"""
