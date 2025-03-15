from django.db.models import IPAddressField
from django.utils.translation import gettext_lazy as _

from .BaseModel import BaseAutoIncrementModel, BaseTimeStampModel


class Blocklist(BaseAutoIncrementModel, BaseTimeStampModel):
    ip_address = IPAddressField(
        verbose_name=_("IP Address"),
    )

    class Meta:
        verbose_name = _("Block list")
        verbose_name_plural = _("Block lists")
