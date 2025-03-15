# from django.db import models
from django.db.models import (
    BooleanField,
    DateTimeField,
    ForeignKey,
    CASCADE,
)
from django.utils.translation import gettext_lazy as _

from Utils.models.BaseModel import BaseImageModel
from User.models.Profile import Profile

# Create your models here.


class Log(BaseImageModel):
    profile = ForeignKey(
        Profile,
        on_delete=CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Profile"),
    )
    is_correct = BooleanField(
        default=False,
        verbose_name=_("is Correct"),
    )
    created_at = DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created At"),
    )

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = _("Log")
        verbose_name_plural = _("Logs")
