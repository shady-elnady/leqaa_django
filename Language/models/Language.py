from django.db.models import CharField, BooleanField

from App.models import BaseNativeModel
from App.messages import ModelsMessages, FieldsMessages

# Create your model


class Language(BaseNativeModel):
    language_iso_code = CharField(
        max_length=2,
        unique=True,
        verbose_name=FieldsMessages.LANGUAGE_ISO_CODE,
    )
    is_bidirectional = BooleanField(
        default=False,
        verbose_name=FieldsMessages.BI_DIRECTONAL_STATUS,
    )

    class Meta:
        verbose_name = ModelsMessages.LANGUAGE
        verbose_name_plural = ModelsMessages.LANGUAGES
