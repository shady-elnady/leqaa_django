# Create your models here.
from django.db.models import CharField, ImageField, URLField, TextField
from django.utils.translation import gettext_lazy as _

from Utils.models.BaseModel import BaseAutoIncrementModel, BaseImageModel
from os.path import join
from django.db.models import Max

# Create your mofrom django.utils.text import slugify


def upload_image_to(instance, file_name):

    all_objects = instance.__class__.objects.all()
    # might be possible model has no records so make sure to handle None
    next_id = all_objects.aggregate(Max("id"))["id__max"] + 1 if all_objects else 1

    extention = file_name.split(".")[-1]
    img_name = getattr(instance, f"{instance.title}", f"{next_id}")
    new_name = f"{img_name}.{extention}"
    return str(
        join(
            "images",
            f"{instance._meta.verbose_name_plural}".strip().replace(" ", "_"),
            new_name,
        )
    )


class Advertisement(BaseAutoIncrementModel, BaseImageModel):
    title = CharField(
        max_length=1100,
        verbose_name=_("Title"),
    )
    url = URLField(
        max_length=200,
        unique=True,
        verbose_name=_("URL"),
    )
    description = TextField(
        null=True,
        blank=True,
        verbose_name=_("Description"),
    )
    image = ImageField(
        upload_to=upload_image_to,
        verbose_name=_("Image"),
    )

    def __str__(self) -> str:
        return f"{self.title}"

    def __decode__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = _("Advertisement")
        verbose_name_plural = _("Advertisements")
