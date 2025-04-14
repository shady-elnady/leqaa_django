from django.db.models import JSONField
from django.utils.translation import get_language

from App.models import BaseNameModel
from App.messages import ModelsMessages

# Create your model


class BaseTranslationModel(BaseNameModel):
    translations = JSONField(
        null=True,
        blank=True,
        verbose_name=ModelsMessages.TRANSLATIONS,
    )

    @property
    def translated_name(self) -> str:
        trans = getattr(self.translations, get_language(), None)
        return trans if trans else self.name

    def __str__(self) -> str:
        return f"{self.translated_name}"

    def __decode__(self) -> str:
        return f"{self.translated_name}"

    class Meta:
        abstract = True
