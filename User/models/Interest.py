from django.db.models import (
    PositiveSmallIntegerField,
    ForeignKey,
    BooleanField,
    CASCADE,
)

from App.models import BaseModel
from App.messages import ModelsMessages, FieldsMessages
from Category.models import Category
from User.models import User


class Interest(BaseModel):
    user = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name="Interests",
        verbose_name=ModelsMessages.USER,
    )

    category = ForeignKey(
        Category,
        on_delete=CASCADE,
        related_name="Interests",
        verbose_name=ModelsMessages.CATEGORY,
    )
    order = PositiveSmallIntegerField(
        default=0,
        verbose_name=FieldsMessages.ORDER,
    )
    is_notifiable = BooleanField(
        default=False,
        verbose_name=FieldsMessages.NOTIFIABLE_STATUS,
    )

    def __str__(self) -> str:
        return f"{self.user.username}>{self.category.name}"

    def __decode__(self) -> str:
        return f"{self.user.username}>{self.category.name}"

    class Meta:
        unique_together = ("user", "category")
        verbose_name = ModelsMessages.INTEREST
        verbose_name_plural = ModelsMessages.INTERESTS
