from django.db.models import ForeignKey, CASCADE

from App.messages import ModelsMessages
from Language.models.BaseTranslationModel import BaseTranslationModel
from Address.models import State

# Create your models here.


class Street(BaseTranslationModel):

    state = ForeignKey(
        State,
        on_delete=CASCADE,
        related_name="Streets",
        verbose_name=ModelsMessages.STATE,
    )

    class Meta:
        verbose_name = ModelsMessages.STREET
        verbose_name_plural = ModelsMessages.STREETS
