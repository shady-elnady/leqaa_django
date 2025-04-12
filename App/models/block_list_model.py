from django.db.models import IPAddressField

from App.messages import ModelsMessages, FieldsMessages
from .base_models import BaseModel


class Blocklist(BaseModel):
    ip_address = IPAddressField(
        verbose_name=FieldsMessages.IP_ADDRESS,
    )

    class Meta:
        verbose_name = ModelsMessages.BLOCK_LIST
        verbose_name_plural = ModelsMessages.BLOCK_LISTS
