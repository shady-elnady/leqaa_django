from django.db.models import ForeignKey, CASCADE

from App.messages import ModelsMessages
from Language.models.BaseTranslationModel import BaseTranslationModel
from Address.models import State

# Create your models here.


class Locality(BaseTranslationModel):
    state = ForeignKey(
        State,
        on_delete=CASCADE,
        related_name="Areas",
        verbose_name=ModelsMessages.STATE,
    )

    class Meta:
        verbose_name = ModelsMessages.LOCALITY
        verbose_name_plural = ModelsMessages.LOCALITIES
