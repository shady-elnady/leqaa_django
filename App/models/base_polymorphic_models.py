from polymorphic.models import PolymorphicModel

from .base_content_models import BaseContentMultiModel, BaseContentSingleModel


class BasePolymorphicSingleModel(PolymorphicModel, BaseContentSingleModel):
    class Meta:
        abstract = True


class BasePolymorphicMultiModel(PolymorphicModel, BaseContentMultiModel):
    class Meta:
        abstract = True
