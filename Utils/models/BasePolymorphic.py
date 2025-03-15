# from django.db import models
# from django.db.models import Model, JSONField
# from django.utils.translation import gettext_lazy as _

# from django.contrib.contenttypes.models import ContentType
# from django.contrib.postgres.fields import ArrayField

from polymorphic.models import PolymorphicModel

from .BaseContentModel import BaseContentMultiModel, BaseContentSingleModel

# from Utils.managers import CustomPolymorphicManager

# Create your models here.


class BasePolymorphicSingleModel(PolymorphicModel, BaseContentSingleModel):
    class Meta:
        abstract = True


class BasePolymorphicMultiModel(PolymorphicModel, BaseContentMultiModel):
    class Meta:
        abstract = True
