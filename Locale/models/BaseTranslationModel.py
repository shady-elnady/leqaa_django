# from django.db import models
from django.db.models import JSONField
from django.utils.translation import get_language, to_locale

from django.utils.translation import gettext_lazy as _

from Utils.models.BaseModel import BaseAutoIncrementNameModel

# Create your model


class BaseTranslationModel(BaseAutoIncrementNameModel):
    translations = JSONField(
        null=True,
        blank=True,
        verbose_name=_("Translations"),
    )

    @property
    def translated_name(self) -> str:

        # locale_code_list = get_language().split("-")
        # locale_code_list[1] = locale_code_list[1].upper()
        # trans = self.translations[("_").join(locale_code_list)]

        trans = self.translations[to_locale(get_language())]
        return trans if trans else self.name

    class Meta:
        abstract = True
