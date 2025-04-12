from django.db.models import (
    ForeignKey,
    CASCADE,
)

from App.models import BaseModel
from App.messages import ModelsMessages
from User.models import User
from Category.models import Category

# Create your model


class Notification(BaseModel):
    user = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name="Notifications",
        verbose_name=ModelsMessages.USER,
    )
    category = ForeignKey(
        Category,
        on_delete=CASCADE,
        related_name="Notifications",
        verbose_name=ModelsMessages.CATEGORY,
    )

    def __str__(self) -> str:
        return f"{self.pk}-{self.user.username}({self.category.name})"

    def __decode__(self) -> str:
        return f"{self.pk}- {self.user.username}({self.category.name})"

    class Meta:
        verbose_name = ModelsMessages.NOTIFICATION
        verbose_name_plural = ModelsMessages.NOTIFICATIONS
