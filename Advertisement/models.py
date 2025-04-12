# Create your models here.
from django.db.models import CharField, URLField, TextField

from App.messages import ModelsMessages, FieldsMessages
from App.models import BaseImageModel, BaseModel

# Create your mofrom django.utils.text import slugify


class Advertisement(BaseModel, BaseImageModel):
    title = CharField(
        max_length=1100,
        verbose_name=FieldsMessages.TITLE,
    )
    advertisement_url = URLField(
        max_length=200,
        unique=True,
        null=True,
        blank=True,
        verbose_name=FieldsMessages.ADVERTISEMENT_URL,
    )
    description = TextField(
        null=True,
        blank=True,
        verbose_name=FieldsMessages.DESCRIPTION,
    )

    def __str__(self) -> str:
        return f"{self.title}"

    def __decode__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = ModelsMessages.ADVERTISEMENT
        verbose_name_plural = ModelsMessages.ADVERTISEMENTS
