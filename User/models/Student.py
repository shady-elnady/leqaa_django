from django.db.models import ForeignKey, OneToOneField, CASCADE, PROTECT

from App.models import BaseModel
from App.messages import ModelsMessages
from Organization.models import College, University
from User.models import User


class Student(BaseModel):
    user = OneToOneField(
        User,
        on_delete=CASCADE,
        related_name="Student",
        verbose_name=ModelsMessages.USER,
    )
    university = ForeignKey(
        University,
        null=True,
        blank=True,
        on_delete=PROTECT,
        related_name="Students",
        verbose_name=ModelsMessages.UNIVERSITY,
    )
    college = ForeignKey(
        College,
        null=True,
        blank=True,
        on_delete=PROTECT,
        related_name="Students",
        verbose_name=ModelsMessages.COLLEGE,
    )

    def __str__(self) -> str:
        return f"{self.user.username}"

    def __decode__(self) -> str:
        return f"{self.user.username}"

    class Meta:
        verbose_name = ModelsMessages.STUDENT
        verbose_name_plural = ModelsMessages.STUDENTS
