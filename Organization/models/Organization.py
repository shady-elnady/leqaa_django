from django.db.models import ForeignKey, CASCADE

from App.models import BaseNameModel, BaseImageModel
from Organization.models import OrganizationType, University
from App.messages import ModelsMessages, FieldsMessages

# Create your models here.


class Organization(BaseNameModel, BaseImageModel):

    organization_type = ForeignKey(
        OrganizationType,
        on_delete=CASCADE,
        related_name="Organizations",
        verbose_name=ModelsMessages.ORGANIZATION_TYPE,
    )
    university = ForeignKey(
        University,
        on_delete=CASCADE,
        related_name="Organizations",
        verbose_name=ModelsMessages.UNIVERSITY,
    )
    affiliated_to = ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=CASCADE,
        related_name="Organizations",
        verbose_name=FieldsMessages.AFFILIATD_TO,
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
        verbose_name = ModelsMessages.ORGANIZATION
        verbose_name_plural = ModelsMessages.ORGANIZATIONS
