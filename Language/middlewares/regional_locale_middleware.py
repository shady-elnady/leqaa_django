# middlewares/regional_locale.py
from typing import Optional
from django.utils import translation
from django.conf import settings
from django.utils.translation import get_language, to_locale
from django.core.exceptions import ImproperlyConfigured


class RegionalLocaleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self._validate_settings()

    def __call__(self, request):
        request_language = self._get_request_language(request)
        regional_lang = self._get_regional_variant(request_language)

        self._activate_language(request, regional_lang)
        response = self.get_response(request)
        self._set_language_cookie(response, regional_lang)
        self._print_info(request)

        return response

    def _validate_settings(self):
        """Validate required regional language settings."""
        if not hasattr(settings, "REGIONAL_LANGUAGES"):
            raise ImproperlyConfigured(
                "REGIONAL_LANGUAGES setting is required for RegionalLocaleMiddleware"
            )

        # Verify all regional variants have base languages defined
        for base_lang, variants in settings.REGIONAL_LANGUAGES.items():
            if base_lang not in dict(settings.LANGUAGES):
                raise ImproperlyConfigured(
                    f"Base language '{base_lang}' from REGIONAL_LANGUAGES not found in LANGUAGES setting"
                )

            if not variants:
                raise ImproperlyConfigured(
                    f"No variants defined for base language '{base_lang}' in REGIONAL_LANGUAGES"
                )

    def _get_request_language(self, request):
        """Get language from request with proper fallback order."""
        self._print_info(request)
        # 4. Check Accept-Language header
        accept_lang = request.META.get("HTTP_ACCEPT_LANGUAGE", "")
        if accept_lang:
            return accept_lang.split(",")[0].split(";")[0]

        # 1. Check URL parameter
        if "lang" in request.GET:
            return request.GET["lang"]

        # 3. Check cookie
        lang = request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME)
        if lang:
            return lang

        # 2. Check session
        if hasattr(request, "session"):
            lang = request.session.get("django_language")
            if lang:
                return lang

        if get_language():
            return get_language()

        # 5. Fallback to default
        return settings.LANGUAGE_CODE

    def _get_regional_variant(self, language_code: Optional[str] = None) -> str:
        """Get the appropriate regional variant for the language."""
        if not language_code:
            return settings.REGIONAL_LANGUAGES.get(settings.LANGUAGE_CODE)[0]

        # Normalize the input (handle both en-US and en_US)
        base_lang = language_code.replace("-", "_").split("_")[0].lower()

        # Check if we have regional variants for this language
        if base_lang in settings.REGIONAL_LANGUAGES:
            variants = settings.REGIONAL_LANGUAGES[base_lang]

            # Try to find exact match first (case insensitive)
            for variant in variants:
                if language_code.replace("-", "_").lower() == variant.lower():
                    return variant

            # Return first variant as default
            return variants[0]

        return settings.REGIONAL_LANGUAGES.get(settings.LANGUAGE_CODE)[0]

    def _normalize_language(self, language_code: Optional[str] = None) -> str:
        """Ensure consistent language code format."""
        if not language_code:
            return settings.REGIONAL_LANGUAGES.get(settings.LANGUAGE_CODE)[0]

        # Convert to standard format (en-us -> en_US)
        normalized = to_locale(language_code.lower())

        # Verify the base language is supported
        base_lang = normalized.split("_")[0]
        if base_lang not in dict(settings.LANGUAGES):
            return settings.REGIONAL_LANGUAGES.get(settings.LANGUAGE_CODE)[0]
        print(f"Normalized language: {normalized}")
        return normalized

    def _activate_language(self, request, language_code):
        """Activate the language for current request."""
        translation.activate(language_code)
        request.LANGUAGE_CODE = language_code
        request.META["HTTP_ACCEPT_LANGUAGE"] = language_code
        setattr(request, "LANGUAGE_CODE", language_code)

    def _set_language_cookie(self, response, language_code):
        """Set language cookie with secure defaults."""
        response.set_cookie(
            settings.LANGUAGE_COOKIE_NAME,
            language_code,
            max_age=settings.LANGUAGE_COOKIE_AGE or 365 * 24 * 60 * 60,
            path=settings.LANGUAGE_COOKIE_PATH or "/",
            domain=settings.LANGUAGE_COOKIE_DOMAIN,
            secure=getattr(settings, "LANGUAGE_COOKIE_SECURE", False),
            httponly=getattr(settings, "LANGUAGE_COOKIE_HTTPONLY", True),
            samesite=getattr(settings, "LANGUAGE_COOKIE_SAMESITE", "Lax"),
        )

    def _print_info(self, request):
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


"""
    # Will return 'ar_AS' or 'ar_EG' depending on active regional variant
    current_language = request.LANGUAGE_CODE
    To change language:

    # Redirect to same view with new language
    return redirect(f"{request.path}?lang=ar_EG")
    In templates:

    <!-- Show current regional language -->
    <p>Current language: {{ request.LANGUAGE_CODE }}</p>
    Run HTML
    Maintenance Benefits
"""
