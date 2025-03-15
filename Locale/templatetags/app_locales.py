# from django.db.models import F, ExpressionWrapper, IntegerField, Q, Count, Sum
# from django.db.models import CharField, Value, Func
# from django.db.models.functions import Concat
# from django.utils import translation
# import json
from django import template
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.template import Node, TemplateSyntaxError  # , Variable, Library
from django.urls import reverse_lazy, reverse  # noqa: F401
import requests
from django.urls import resolve

from Locale.models import Locale

# from django.template.defaulttags import register

# for locale in Locale.objects.filter(is_app_suport=True):
#     locale: Locale = locale
#     settings.APP_LOCALES[locale.locale_code] = {
#         "is_bidi": locale.language.is_bidirectional,
#         "locale_code": locale.locale_code,
#         "language_code": locale.language.language_iso_code,
#         "country_code": locale.country.country_code,
#         "flag": str(locale.country.flag.path),
#         "name": locale.language.name,
#         "native_name": locale.language.native_name,
#     }

register = template.Library()


@register.simple_tag(takes_context=True)
def get_app_locales(context):
    request = context["request"]
    print(request.build_absolute_uri("/en-us/api/app-locales/"))
    # return resolve(request.path_info).url_name
    if not settings.APP_LOCALES["is_set"]:
        # response = requests.get(reverse("app-locale-list"))
        response = requests.get(request.build_absolute_uri("/api/app-locales/"))
        # Check the status code and process the response
        if response.status_code == 200:
            settings.APP_LOCALES["is_set"] = True
            data = response.json()
            settings.APP_LOCALES["data"] = data["results"]
        else:
            print("Failed to retrieve data", response.status_code)
    return settings.APP_LOCALES["data"]


# @register.filter("app_locales")
# def app_locales(parser):
#     if not settings.APP_LOCALES["is_set"]:
#         # response = requests.get(reverse("app-locale-list"))
#         response = requests.get("http://127.0.0.1:8000/en-us/api/app-locales/")
#         # Check the status code and process the response
#         if response.status_code == 200:
#             settings.APP_LOCALES["is_set"] = True
#             data = response.json()
#             settings.APP_LOCALES["data"] = data["results"]
#         else:
#             print("Failed to retrieve data", response.status_code)
#     return settings.APP_LOCALES["data"]


# @register.tag("app_locales")
# def do_app_locales(parser, token):
#     """
#     Store a list of language information dictionaries for the given language
#     codes in a context variable. The language codes can be specified either as
#     a list of strings or a settings.LANGUAGES style list (or any sequence of
#     sequences whose first items are language codes).

#     Usage::

#         {% app_locales for LANGUAGES as langs %}
#         {% for l in langs %}
#           {{ l.code }}
#           {{ l.name }}
#           {{ l.name_translated }}
#           {{ l.name_local }}
#           {{ l.bidi|yesno:"bi-directional,uni-directional" }}
#         {% endfor %}
#     """
#     args = token.split_contents()
#     if len(args) != 5 or args[1] != "for" or args[3] != "as":
#         raise TemplateSyntaxError(
#             "'%s' requires 'for sequence as variable' (got %r)" % (args[0], args[1:])
#         )

#     return GetLocaleInfoListNode(parser.compile_filter(args[2]), args[4])


# class GetLocaleInfoListNode(Node):
#     def __init__(self, locales, variable):
#         self.locales = locales
#         self.variable = variable

#     def get_locale_info(self, lang_code):
#         from django.conf.locale import LANG_INFO

#         try:
#             lang_info = settings.APP_LOCALES[lang_code]
#             if "fallback" in lang_info and "name" not in lang_info:
#                 info = self.get_locale_info(lang_info["fallback"][0])
#             else:
#                 info = lang_info
#         except KeyError:
#             if "-" not in lang_code:
#                 raise KeyError("Unknown Locale code %s." % lang_code)
#             generic_lang_code = lang_code.split("-")[0]
#             try:
#                 info = LANG_INFO[generic_lang_code]
#             except KeyError:
#                 raise KeyError(
#                     "Unknown Locales code %s and %s." % (lang_code, generic_lang_code)
#                 )
#         if info:
#             info["name_translated"] = _(info["name"])
#             if (
#                 (not info["native_name"])
#                 or (info["native_name"] is None)
#                 or (info["native_name"] == "")
#             ):
#                 info["native_name"] = _(info["name"])
#         return info

#     def locale_info(self, locale):
#         # ``locale`` is either a locale code string or a sequence
#         # with the locale code as its first item
#         if len(locale[0]) > 1:
#             return self.get_locale_info(locale[0])
#         else:
#             return self.get_locale_info(str(locale))

#     def render(self, context):
#         locales = self.locales.resolve(context)
#         context[self.variable] = [self.locale_info(loc) for loc in locales]
#         return ""
