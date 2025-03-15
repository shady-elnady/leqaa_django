from django.db.models import EmailField
from django.utils.translation import gettext_lazy as _

from User.utils.usereMessages import UserMessages
from Utils.models.BaseModel import BaseLogoModel
from Locale.models.BaseTranslationModel import BaseTranslationModel

# Create your models here.


class University(BaseTranslationModel, BaseLogoModel):
    email = EmailField(
        unique=True,
        error_messages={"unique": UserMessages.EMAIL_UNIQUE_VALIDATION},
        verbose_name=_("E-mail"),
    )

    class Meta:
        verbose_name = _("UniversityType")
        verbose_name_plural = _("University Types")
