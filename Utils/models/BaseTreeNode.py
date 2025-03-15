# from django.db import models
from django.db.models import PROTECT
from django.utils.translation import gettext_lazy as _

from polymorphic_tree.models import PolymorphicMPTTModel, PolymorphicTreeForeignKey

from .BaseContentModel import BaseContentMultiModel, BaseContentSingleModel

# Create your models here.


class BaseTreeNode(PolymorphicMPTTModel):
    parent = PolymorphicTreeForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=PROTECT,
        related_name="children",
        verbose_name=_("Parent"),
    )

    class Meta(PolymorphicMPTTModel.Meta):
        abstract = True


class BaseTreeNodeSingleModel(BaseContentSingleModel, BaseTreeNode):
    class Meta:
        abstract = True


class BaseTreeNodeMultiModel(BaseContentMultiModel, BaseTreeNode):
    class Meta:
        abstract = True
