from django.db.models import ForeignKey, OneToOneField, CASCADE, PROTECT

from App.models import BaseModel
from App.messages import ModelsMessages, FieldsMessages
from Category.models import Category
from User.models import User


class Lecturer(BaseModel):
    user = OneToOneField(
        to=User,
        on_delete=CASCADE,
        related_name="Lecturer",
        verbose_name=ModelsMessages.USER,
    )
    Specialized_to_category = ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=PROTECT,
        related_name="Lecturers",
        verbose_name=FieldsMessages.SPECIALIZED_TO_CATEGORIES,
    )

    def __str__(self) -> str:
        return f"{self.user.username}"

    def __decode__(self) -> str:
        return f"{self.user.username}"

    class Meta:
        verbose_name = ModelsMessages.LECTURER
        verbose_name_plural = ModelsMessages.LECTURERS
