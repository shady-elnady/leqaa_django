from django.conf import settings

from Language.utils.locales_loader import get_cached_app_locales


def context_app_locales(request):
    locales = get_cached_app_locales()

    return {
        "app_locales": locales,
        "current_locale": list(
            filter(lambda x: x.get("locale_code") == request.LANGUAGE_CODE, locales)
        )[0].get("locale_code"),
    }
