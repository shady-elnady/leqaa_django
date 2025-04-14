from django.conf import settings
from django.utils import translation
from django.utils.translation import get_language, to_locale
from Language.utils.locales_loader import get_cached_app_locales


def context_app_locales(request):
    locales = get_cached_app_locales()
    print(100 * "&")
    print(100 * "#")
    print(f"request.GET >> {request.GET}")
    print(f"translation.get_language() >> {translation.get_language()}")
    print(f"get_language() >> {get_language()}")
    print(f"request.LANGUAGE_CODE: {request.LANGUAGE_CODE}")
    print(
        f'request.session.get("django_language") >> {request.session.get("django_language")}'
    )
    print(
        f'request.META.get("HTTP_ACCEPT_LANGUAGE", "") >> {request.META.get("HTTP_ACCEPT_LANGUAGE", "")}'
    )
    print(
        f"request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME) >> {request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME)}"
    )
    print(100 * "#")
    print(f"locales >> {locales}")
    print(100 * "&")

    return {
        "app_locales": locales,
        "current_locale": list(
            filter(lambda x: x.get("locale_code") == request.LANGUAGE_CODE, locales)
        )[0].get("locale_code"),
    }
