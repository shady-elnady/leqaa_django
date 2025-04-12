from App.messages import ModelsMessages

from App.models import BaseImageModel
from Language.models.BaseTranslationModel import BaseTranslationModel

# Create your mofrom django.utils.text import slugify


class Category(BaseTranslationModel, BaseImageModel):

    class Meta:
        verbose_name = ModelsMessages.CATEGORY
        verbose_name_plural = ModelsMessages.CATEGORIES
