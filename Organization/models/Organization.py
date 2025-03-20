from django.db.models import ForeignKey, CASCADE
from django.utils.translation import gettext_lazy as _

from Utils.models.BaseModel import BaseAutoIncrementNameModel, BaseLogoModel
from Organization.models import OrganizationType, University

# Create your models here.


class Organization(BaseAutoIncrementNameModel, BaseLogoModel):

    organization_type = ForeignKey(
        OrganizationType,
        on_delete=CASCADE,
        related_name=_("Organizations"),
        verbose_name=_("Organization Type"),
    )
    university = ForeignKey(
        University,
        on_delete=CASCADE,
        related_name=_("Organizations"),
        verbose_name=_("University"),
    )
    affiliated_to = ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=CASCADE,
        related_name=_("Organizations"),
        verbose_name=_("Affiliated To"),
    )

    class Meta:
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")
