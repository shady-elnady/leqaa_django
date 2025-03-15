from django.utils.translation import get_language, to_locale
from django.utils import translation
from django.conf import settings
import locale
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import gettext_lazy as _


class UserLanguageMiddleware:

    LANG_TO_LOCALE = {
        "en": "en_US.UTF8",
        "nl": "nl_NL.UTF8",
        "es": "es_ES.UTF8",
        "ar": "ar_AS.UTF8",
    }

    def __init__(self, get_response):
        self.get_response = get_response

    def lang_to_locale(self, language_code):
        return self.LANG_TO_LOCALE.get(language_code)

    def __call__(self, request):

        if not hasattr(settings.APP_LOCALES["data"], to_locale(get_language())):
            headers = dict(request.headers)

        # else:
        #     setattr(request, "LANGUAGE_CODE", translation.get_language())

        # translation.activate("ar_EG")

        # headers["Accept-Language"] = "ar_EG"

        response = self.get_response(request)

        # translation.deactivate()

        print("===========================================================")
        # headers["Accept-Language"] = "ar-ff"
        print(f"1 >> {getattr(headers, "Accept-Language", None)}")
        print("===========================================================")
        print(f"2 >> {get_language()}")
        print("===========================================================")
        print(f"3 >> {request.LANGUAGE_CODE}")
        print("===========================================================")
        # locale.setlocale(locale.LC_ALL, self.lang_to_locale("ar"))
        # print(f"1 >> {locale.getlocale()}")
        # print("===========================================================")

        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response


"""

https://developer.mozilla.org/en-US/docs/Web/API/Navigator


"""
