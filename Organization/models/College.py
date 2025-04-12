from django.db.models import ForeignKey, CASCADE

from App.models import BaseImageModel
from App.messages import ModelsMessages
from Language.models.BaseTranslationModel import BaseTranslationModel
from .University import University

# Create your models here.


class College(BaseTranslationModel, BaseImageModel):
    university = ForeignKey(
        University,
        on_delete=CASCADE,
        related_name="Colleges",
        verbose_name=ModelsMessages.UNIVERSITY,
    )

    #############################################################
    ######################### Image Filed  ######################
    #############################################################
    @property
    def logo(self):
        return self.image

    @logo.setter
    def logo(self, value):
        self.image = value

    #############################################################

    class Meta:
        verbose_name = ModelsMessages.COLLEGE
        verbose_name_plural = ModelsMessages.COLLEGES
