from django.db.models import EmailField

from App.models import BaseImageModel
from App.messages import ModelsMessages, FieldsMessages
from Language.models.BaseTranslationModel import BaseTranslationModel

# Create your models here.


class University(BaseTranslationModel, BaseImageModel):
    email = EmailField(
        unique=True,
        verbose_name=FieldsMessages.EMAIL,
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
        verbose_name = ModelsMessages.UNIVERSITY
        verbose_name_plural = ModelsMessages.UNIVERSITIES
