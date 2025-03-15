from django.db.models import (
    CharField,
    ForeignKey,
    CASCADE,
    TextField,
    DateTimeField,
    FloatField,
    PositiveSmallIntegerField,
)
from django.utils.translation import gettext_lazy as _

from Event.utils.enums import EventPaidStatus, LecturerFinancialSystem
from Utils.models.BaseModel import BaseImageModel, BaseModel, BasePhotoModel
from Locale.models.BaseTranslationModel import BaseTranslationModel
from Category.models import Category
from Organization.models import College, Organization, University
from User.models import Lecturer

# Create your models here.


class EventType(BaseTranslationModel, BaseImageModel):

    class Meta:
        verbose_name = _("Event Type")
        verbose_name_plural = _("Event Types")


class Event(BaseModel, BaseImageModel):
    title = CharField(
        max_length=100,
        verbose_name=_("Title"),
    )
    hall = CharField(
        max_length=100,
        verbose_name=_("Hall"),
    )
    event_type = ForeignKey(
        EventType,
        on_delete=CASCADE,
        related_name="Events",
        verbose_name=_("Event Type"),
    )
    category = ForeignKey(
        Category,
        on_delete=CASCADE,
        related_name=_("Events"),
        verbose_name=_("Category"),
    )
    lecturer = ForeignKey(
        Lecturer,
        null=True,
        blank=True,
        on_delete=CASCADE,
        related_name=_("Events"),
        verbose_name=_("Lecturer"),
    )
    university = ForeignKey(
        University,
        on_delete=CASCADE,
        related_name=_("Events"),
        verbose_name=_("University"),
    )
    college = ForeignKey(
        College,
        null=True,
        blank=True,
        on_delete=CASCADE,
        related_name=_("Events"),
        verbose_name=_("College"),
    )
    organizer = ForeignKey(
        Organization,
        null=True,
        blank=True,
        on_delete=CASCADE,
        related_name=_("Events"),
        verbose_name=_("Organizer"),
    )
    lecturer_financial_dues = FloatField(
        null=True,
        blank=True,
        verbose_name=_("Lecturer Financial Dues"),
    )
    lecturer_financial_system = CharField(
        max_length=100,
        choices=LecturerFinancialSystem.choices,
        default=LecturerFinancialSystem.Enlist,
        verbose_name=_("Hall"),
    )
    event_paid_status = CharField(
        max_length=100,
        choices=EventPaidStatus.choices,
        default=EventPaidStatus.Free,
        verbose_name=_("Event Paid Status"),
    )
    description = TextField(
        null=True,
        blank=True,
        verbose_name=_("Description"),
    )
    start_date_time = DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Start Date Time"),
    )

    def __str__(self) -> str:
        return f"{self.title}"

    def __decode__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")


class EventAlbum(BaseModel, BasePhotoModel):
    event = ForeignKey(
        Event,
        on_delete=CASCADE,
        related_name="EventPhotosAlbum",
        verbose_name=_("Event"),
    )
    order = PositiveSmallIntegerField(
        default=1,
        verbose_name=_("Order"),
    )

    def __str__(self) -> str:
        return f"{self.pk}-{self.event.title}({self.order})"

    def __decode__(self) -> str:
        return f"{self.pk}-{self.event.title}({self.order})"

    class Meta:
        verbose_name = _("Event Album")
        verbose_name_plural = _("Events Albums")
