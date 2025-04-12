from django.db.models import (
    BooleanField,
    ForeignKey,
    CASCADE,
)

from App.models import BaseImageModel, BaseModel
from App.messages import ChoicesMessages, ModelsMessages, FieldsMessages
from User.models import Profile

# Create your models here.


class Log(BaseModel, BaseImageModel):
    profile = ForeignKey(
        Profile,
        on_delete=CASCADE,
        blank=True,
        null=True,
        verbose_name=ModelsMessages.PROFILE,
    )
    is_correct = BooleanField(
        default=False,
        verbose_name=FieldsMessages.SUCCESS_STATUS,
    )

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = ChoicesMessages.SIGN_IN
        verbose_name_plural = ChoicesMessages.SIGN_IN
