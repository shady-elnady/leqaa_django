# from django.db import models
from django.db.models import BooleanField, ForeignKey, CASCADE
from django.utils.translation import gettext_lazy as _

from Utils.models.BaseModel import BaseModel
from .Language import Language

# Create your model


class Locale(BaseModel):
    language = ForeignKey(
        Language,
        on_delete=CASCADE,
        related_name=_("Locales"),
        verbose_name=_("Language"),
    )
    country = ForeignKey(
        "Address.Country",
        on_delete=CASCADE,
        related_name=_("Locales"),
        verbose_name=_("Country"),
    )
    is_app_suport = BooleanField(
        default=True,
        verbose_name=_("Is Application Support"),
    )

    @property
    def locale_code(self) -> str:
        return f"{self.language.language_iso_code}-{self.country.country_code}"

    @property
    def language_native_name(self) -> str:
        return self.language.native_name

    @property
    def is_bidirectional(self) -> str:
        return self.language.is_bidirectional

    @property
    def locale_flag(self) -> str:
        return self.country.flag

    def __str__(self) -> str:
        return f"{self.language.language_iso_code}-{self.country.country_code}"

    def __decode__(self) -> str:
        return f"{self.language.language_iso_code}-{self.country.country_code}"

    class Meta:
        verbose_name = _("Locale")
        verbose_name_plural = _("Locales")


# activate language to auth user
"""
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.urls import translate_url
from django.utils.translation import activate, LANGUAGE_SESSION_KEY

# available languages should be obtained from settings.LANGUAGES
available_languages = [lang_code for (lang_code, lang_name) in settings.LANGUAGES]

class CustomLoginView(LoginView):
    def get_success_url(self):
        url = super(CustomLoginView, self).get_success_url()
        user = self.request.user
        if user.is_authenticated():
            language = user.get_setting('language')

            if language in available_languages:
                url = translate_url(url, language)
                activate(language)
                if hasattr(self.request, 'session'):
                    self.request.session[LANGUAGE_SESSION_KEY] = language

        return url
"""

# What's the correct way to set up Django translation?
"""
https://stackoverflow.com/questions/20467626/whats-the-correct-way-to-set-up-django-translation#76475418

https://stackoverflow.com/questions/53962200/django-store-the-language-of-user-in-database

"""
