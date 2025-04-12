from django.core.cache import cache
from django.conf import settings

from Language.models import Locale


LOCALE_CACHE_KEY = "app_supported_locales"


def fetch_supported_locales():
    """
    Fetch supported locales from API and update settings.APP_LOCALES
    """
    try:
        locales = [
            {
                "language_name": locale.language_native_name,
                "language_code": locale.language.language_iso_code,
                "language_is_bidir": locale.is_bidirectional,
                "locale_code": locale.locale_code,
                "locale_flag": locale.locale_flag.url,
            }
            for locale in Locale.objects.filter(is_app_suport=True)
        ]

        # Update cache and settings
        cache.set(LOCALE_CACHE_KEY, locales, timeout=None)  # No expiration
        settings.APP_LOCALES["is_set"] = True
        return locales

    except Exception as e:
        print(f"Error fetching locales: {str(e)}")
        return settings["APP_LOCALES"]["data"]


def get_cached_app_locales():
    """
    Get locales from cache or fetch from API if not available
    """
    locales = cache.get(LOCALE_CACHE_KEY)
    if locales is None:
        locales = fetch_supported_locales()
    return locales
