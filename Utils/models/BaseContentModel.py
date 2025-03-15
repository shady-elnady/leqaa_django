# from django.db import models
from django.db.models import Model, CharField, JSONField
from django.utils.translation import gettext_lazy as _
from django.utils import formats
from datetime import datetime

# Create your models here.


class BaseContentSingleModel(Model):
    content_type = CharField(
        max_length=30,
        editable=False,
        verbose_name=_("Content Types"),
    )

    def save(self, *args, **kwargs):
        self.full_clean()
        if not self.content_type:
            self.content_type = self.__class__.__name__
        return super(BaseContentSingleModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class BaseContentMultiModel(Model):
    content_types = JSONField(
        editable=False,
        default=dict,
        blank=True,
        null=True,
        verbose_name=_("Content Types"),
    )

    def save(self, *args, **kwargs):
        self.full_clean()
        if self.__class__.__name__ not in self.content_types.keys():
            self.content_types[self.__class__.__name__] = formats.date_format(
                datetime.now().date(),
                "d-m-Y",
            )
        return super(BaseContentMultiModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
