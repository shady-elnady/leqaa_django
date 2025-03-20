from django.db.models import PositiveSmallIntegerField, ForeignKey, CASCADE
from django.utils.translation import gettext_lazy as _

from Category.models import Category
from Utils.models.BaseModel import BaseModel
from .User import User


class Interest(BaseModel):
    user = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name="Interests",
        verbose_name=_("User"),
    )

    category = ForeignKey(
        Category,
        on_delete=CASCADE,
        related_name="Interests",
        verbose_name=_("Category"),
    )
    order = PositiveSmallIntegerField(
        default=0,
        verbose_name=_("Order"),
    )

    def __str__(self) -> str:
        return f"{self.user.username}>{self.category.name}"

    def __decode__(self) -> str:
        return f"{self.user.username}>{self.category.name}"

    class Meta:
        unique_together = ("user", "category")
        verbose_name = _("Interest")
        verbose_name_plural = _("Interests")
