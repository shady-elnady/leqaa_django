# Create your models here.
from django.db.models import CharField, URLField, TextField
from django.utils.translation import gettext_lazy as _

from Utils.models.BaseModel import BaseAutoIncrementModel, BaseImageModel

# Create your mofrom django.utils.text import slugify


class Advertisement(BaseAutoIncrementModel, BaseImageModel):
    title = CharField(
        max_length=1100,
        require=True,
        verbose_name=_("Title"),
    )
    url = URLField(
        max_length=200,
        unique=True,
        require=True,
        verbose_name=_("URL"),
    )
    description = TextField(
        null=True,
        blank=True,
        verbose_name=_("Description"),
    )

    def __str__(self) -> str:
        return f"{self.title}"

    def __decode__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = _("Advertisement")
        verbose_name_plural = _("Advertisements")
