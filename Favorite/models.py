from django.db.models import (
    ForeignKey,
    CASCADE,
)

from App.models.base_models import BaseModel
from App.messages import ModelsMessages
from User.models import User
from Event.models import Event

# Create your model


class Favorite(BaseModel):
    user = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name="Favorites",
        verbose_name=ModelsMessages.USER,
    )
    event = ForeignKey(
        Event,
        on_delete=CASCADE,
        related_name="Favorites",
        verbose_name=ModelsMessages.EVENT,
    )

    def __str__(self) -> str:
        return f"{self.pk}-{self.user.username}({self.event.title})"

    def __decode__(self) -> str:
        return f"{self.pk}- {self.user.username}({self.event.title})"

    class Meta:
        verbose_name = ModelsMessages.FAVORITE
        verbose_name_plural = ModelsMessages.FAVORITES
