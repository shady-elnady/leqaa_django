from django.db.models import CharField, ForeignKey, CASCADE

from App.messages import ModelsMessages, FieldsMessages
from App.validators import RegexValidators
from Language.models.BaseTranslationModel import BaseTranslationModel
from Address.models import Country

# Create your models here.


class Governorate(BaseTranslationModel):  # المحافظه
    ## https://en.wikipedia.org/wiki/ISO_3166-2:EG

    country = ForeignKey(
        Country,
        on_delete=CASCADE,
        related_name="Governorate",
        verbose_name=ModelsMessages.COUNTRY,
    )
    governorate_tel_code = CharField(
        max_length=3,
        blank=True,
        null=True,
        unique=True,
        validators=[RegexValidators.governorate_tel_code_pattern_validator],
        verbose_name=FieldsMessages.TELPHONE_CODE,
    )

    class Meta:
        verbose_name = ModelsMessages.GOVERNORATE
        verbose_name_plural = ModelsMessages.GOVERNORATES
