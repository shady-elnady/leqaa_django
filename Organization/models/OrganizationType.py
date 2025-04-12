from App.messages import ModelsMessages

from Language.models import BaseTranslationModel

# Create your models here.


class OrganizationType(BaseTranslationModel):

    class Meta:
        verbose_name = ModelsMessages.ORGANIZATION_TYPE
        verbose_name_plural = ModelsMessages.ORGANIZATION_TYPES
