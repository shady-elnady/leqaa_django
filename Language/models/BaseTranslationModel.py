from django.db.models import JSONField
from django.utils.translation import get_language, to_locale

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
        trans = self.translations[to_locale(get_language()).replace("_", "-")]
        return trans if trans else self.name

    class Meta:
        abstract = True
