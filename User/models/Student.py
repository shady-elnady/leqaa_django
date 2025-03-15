from django.db.models import ForeignKey, OneToOneField, CASCADE, PROTECT
from django.utils.translation import gettext_lazy as _

from Organization.models import College, University
from Utils.models.BaseModel import BaseModel
from User.models import User


class Student(BaseModel):
    user = OneToOneField(
        User,
        on_delete=CASCADE,
        related_name="Student",
        verbose_name=_("User"),
    )
    university = ForeignKey(
        University,
        null=True,
        blank=True,
        on_delete=PROTECT,
        related_name="Students",
        verbose_name=_("University"),
    )
    college = ForeignKey(
        College,
        null=True,
        blank=True,
        on_delete=PROTECT,
        related_name="Students",
        verbose_name=_("College"),
    )

    def __str__(self) -> str:
        return f"{self.user.username}"

    def __decode__(self) -> str:
        return f"{self.user.username}"

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")
