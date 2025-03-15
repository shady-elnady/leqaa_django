from django.db.models import ForeignKey, OneToOneField, CASCADE, PROTECT
from django.utils.translation import gettext_lazy as _

from Utils.models.BaseModel import BaseModel
from Category.models import Category
from User.models import User


class Lecturer(BaseModel):
    user = OneToOneField(
        User,
        on_delete=CASCADE,
        related_name="Lecturer",
        verbose_name=_("User"),
    )
    category = ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=PROTECT,
        related_name="Lecturers",
        verbose_name=_("Category"),
    )

    def __str__(self) -> str:
        return f"{self.user.username}"

    def __decode__(self) -> str:
        return f"{self.user.username}"

    class Meta:
        verbose_name = _("Lecturer")
        verbose_name_plural = _("Lecturers")
