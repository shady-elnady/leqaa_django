from django.db.models import (
    CharField,
    ForeignKey,
    CASCADE,
    SET_NULL,
    TextField,
    DateTimeField,
    FloatField,
    PositiveSmallIntegerField,
    URLField,
)
from datetime import datetime
from typing import Optional, Union
from django.core.exceptions import ValidationError
from django.utils.timezone import make_aware, is_aware

from App.messages import ModelsMessages, FieldsMessages
from App.messages.validation_messages import ValidationMessages
from App.models import BaseImageModel, BaseModel
from Language.models.BaseTranslationModel import BaseTranslationModel
from Category.models import Category
from Organization.models import College, Organization, University
from User.models import Lecturer
from Address.models import Location
from Event.utils.enums import (
    EventPaidStatus,
    LecturerFinancialSystem,
    OnOrOffLineStatus,
)

# Create your models here.


class EventType(BaseTranslationModel, BaseImageModel):

    class Meta:
        verbose_name = ModelsMessages.EVENT_TYPE
        verbose_name_plural = ModelsMessages.EVENT_TYPES


class Event(BaseModel, BaseImageModel):
    title = CharField(
        max_length=100,
        verbose_name=FieldsMessages.TITLE,
    )
    hall = CharField(
        max_length=100,
        verbose_name=FieldsMessages.HALL,
    )
    event_type = ForeignKey(
        EventType,
        on_delete=CASCADE,
        related_name="Events",
        verbose_name=ModelsMessages.EVENT_TYPE,
    )
    category = ForeignKey(
        Category,
        on_delete=CASCADE,
        related_name="Events",
        verbose_name=ModelsMessages.CATEGORY,
    )
    lecturer = ForeignKey(
        Lecturer,
        blank=True,
        on_delete=CASCADE,
        related_name="Events",
        verbose_name=ModelsMessages.LECTURER,
    )
    university = ForeignKey(
        University,
        null=True,
        blank=True,
        on_delete=CASCADE,
        related_name="Events",
        verbose_name=ModelsMessages.UNIVERSITY,
    )
    college = ForeignKey(
        College,
        null=True,
        blank=True,
        on_delete=CASCADE,
        related_name="Events",
        verbose_name=ModelsMessages.COLLEGE,
    )
    organizer = ForeignKey(
        Organization,
        null=True,
        blank=True,
        on_delete=CASCADE,
        related_name="Events",
        verbose_name=FieldsMessages.ORGANIZER,
    )
    location = ForeignKey(
        Location,
        null=True,
        blank=True,
        on_delete=SET_NULL,
        related_name="Events",
        verbose_name=FieldsMessages.LOCATION,
    )
    lecturer_financial_dues = FloatField(
        null=True,
        blank=True,
        verbose_name=FieldsMessages.LECTURER_FINANCIAL_DUES,
    )
    lecturer_financial_system = CharField(
        max_length=2,
        choices=LecturerFinancialSystem.choices,
        default=LecturerFinancialSystem.Enlist,
        verbose_name=FieldsMessages.LECTURER_FINANCIAL_SYSTEM,
    )
    event_paid_status = CharField(
        max_length=2,
        choices=EventPaidStatus.choices,
        default=EventPaidStatus.Free,
        verbose_name=FieldsMessages.EVENT_PAID_STATUS,
    )
    on_or_off_line = CharField(
        max_length=2,
        choices=OnOrOffLineStatus.choices,
        default=OnOrOffLineStatus.Any,
        verbose_name=FieldsMessages.ON_OR_OFF_LINE,
    )
    short_description = TextField(
        null=True,
        blank=True,
        verbose_name=FieldsMessages.SHORT_DESCRIPTION,
    )
    complete_description = TextField(
        null=True,
        blank=True,
        verbose_name=FieldsMessages.COMPLETE_DESCRIPTION,
    )
    start_date_time = DateTimeField(
        blank=True,
        verbose_name=FieldsMessages.START_DATE_TIME,
    )
    end_date_time = DateTimeField(
        blank=True,
        verbose_name=FieldsMessages.END_DATE_TIME,
    )
    registration_link = URLField(
        blank=True,
        verbose_name=FieldsMessages.REGISTRATION_LINK,
    )

    # ==================== Start DateTime Property ====================
    @property
    def start_datetime(self) -> Optional[datetime]:
        """
        Getter for start_date_time that ensures timezone awareness
        Returns:
            Optional[datetime]: Timezone-aware datetime or None
        """
        if self.start_date_time is None:
            return None
        if not is_aware(self.start_date_time):
            return make_aware(self.start_date_time)
        return self.start_date_time

    @start_datetime.setter
    def start_datetime(self, value: Union[str, datetime, None]):
        """
        Setter for start_date_time that handles multiple input types
        Args:
            value: Can be string, datetime (naive or aware), or None
        Raises:
            ValidationError: If input format is invalid
        """
        self.start_date_time = self._parse_datetime(value)

    # ==================== End DateTime Property ====================
    @property
    def end_datetime(self) -> Optional[datetime]:
        """
        Getter for end_date_time that ensures timezone awareness
        Returns:
            Optional[datetime]: Timezone-aware datetime or None
        """
        if self.end_date_time is None:
            return None
        if not is_aware(self.end_date_time):
            return make_aware(self.end_date_time)
        return self.end_date_time

    @end_datetime.setter
    def end_datetime(self, value: Union[str, datetime, None]):
        """
        Setter for end_date_time that handles multiple input types
        Args:
            value: Can be string, datetime (naive or aware), or None
        Raises:
            ValidationError: If input format is invalid
        """
        self.end_date_time = self._parse_datetime(value)

    # ==================== Shared Helper Method ====================
    # def _parse_datetime(self, value: Union[str, datetime, None]) -> Optional[datetime]:
    #     """
    #     Parse datetime input into timezone-aware datetime
    #     Args:
    #         value: Input value to parse
    #     Returns:
    #         Optional[datetime]: Parsed datetime or None
    #     Raises:
    #         ValidationError: If input format is invalid
    #     """
    #     if value is None:
    #         return None

    #     try:
    #         if isinstance(value, str):
    #             # Parse string input (multiple formats)
    #             for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M"):
    #                 try:
    #                     dt = datetime.strptime(value, fmt)
    #                     return make_aware(dt)
    #                 except ValueError:
    #                     continue
    #             raise ValueError("No valid datetime format found")

    #         elif isinstance(value, datetime):
    #             # Handle datetime objects
    #             if not is_aware(value):
    #                 return make_aware(value)
    #             return value

    #         else:
    #             raise TypeError("Invalid datetime type")

    #     except (ValueError, TypeError) as e:
    #         raise ValidationError(f"Invalid datetime value: {str(e)}")

    # ==================== Validation ====================
    def clean(self):
        """Model validation ensuring end time is after start time"""
        if self.start_date_time and self.end_date_time:
            if self.end_date_time <= self.start_date_time:
                raise ValidationError(
                    {
                        "end_date_time": ValidationMessages.END_DATE_TIME_MUST_BE_AFTER_START_DATE_TIME,
                    },
                )

    def save(self, *args, **kwargs):
        """Ensure clean data before saving"""
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.title}"

    def __decode__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = ModelsMessages.EVENT
        verbose_name_plural = ModelsMessages.EVENTS


class EventAlbum(BaseModel, BaseImageModel):
    event = ForeignKey(
        Event,
        on_delete=CASCADE,
        related_name="EventPhotosAlbum",
        verbose_name=ModelsMessages.EVENT,
    )
    order = PositiveSmallIntegerField(
        default=1,
        verbose_name=FieldsMessages.ORDER,
    )

    def __str__(self) -> str:
        return f"{self.pk}-{self.event.title}({self.order})"

    def __decode__(self) -> str:
        return f"{self.pk}-{self.event.title}({self.order})"

    class Meta:
        verbose_name = ModelsMessages.EVENT_ALBUM
        verbose_name_plural = ModelsMessages.EVENT_ALBUMS


# # Use Property Setter and Getter for Date Time Fileds
"""
    event = Event()

    # Set from string (form input)
    event.start_datetime = "2025-04-17 10:05:00"
    event.end_datetime = "2025-04-17 18:30:00"

    # Set from naive datetime
    event.start_datetime = datetime(2025, 4, 17, 10, 5)

    # Set from aware datetime
    aware_dt = make_aware(datetime(2025, 4, 17, 18, 30))
    event.end_datetime = aware_dt

    # Get values (always returns aware datetime)
    print(event.start_datetime)  # Returns timezone-aware datetime
    print(event.end_datetime)    # Returns timezone-aware datetime

    # None handling
    event.start_datetime = None
"""
