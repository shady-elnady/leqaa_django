from django.db.models import PROTECT
from polymorphic_tree.models import PolymorphicMPTTModel, PolymorphicTreeForeignKey

from App.messages import ChoicesMessages
from .base_content_models import BaseContentMultiModel, BaseContentSingleModel

# Create your models here.


class BaseTreeNode(PolymorphicMPTTModel):
    parent = PolymorphicTreeForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=PROTECT,
        related_name="children",
        verbose_name=ChoicesMessages.PARENT,
    )

    class Meta(PolymorphicMPTTModel.Meta):
        abstract = True


class BaseTreeNodeSingleModel(BaseContentSingleModel, BaseTreeNode):
    class Meta:
        abstract = True


class BaseTreeNodeMultiModel(BaseContentMultiModel, BaseTreeNode):
    class Meta:
        abstract = True
