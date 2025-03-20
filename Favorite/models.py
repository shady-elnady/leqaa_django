from django.db.models import (
    ForeignKey,
    CASCADE,
)
from django.utils.translation import gettext_lazy as _

from Utils.models.BaseModel import BaseModel
from User.models import User
from Event.models import Event

# Create your model


class Favorite(BaseModel):
    user = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name=_("Favorites"),
        verbose_name=_("User"),
    )
    event = ForeignKey(
        Event,
        on_delete=CASCADE,
        related_name=_("Favorites"),
        verbose_name=_("Event"),
    )

    def __str__(self) -> str:
        return f"{self.pk}-{self.user.username}({self.event.title})"

    def __decode__(self) -> str:
        return f"{self.pk}- {self.user.username}({self.event.title})"

    class Meta:
        verbose_name = _("Favorite")
        verbose_name_plural = _("Favorites")
