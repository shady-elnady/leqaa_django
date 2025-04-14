from typing import Optional, Union
from django.db.models import (
    Model,
    CharField,
    PositiveSmallIntegerField,
    OneToOneField,
    ForeignKey,
    DateField,
    CASCADE,
    PROTECT,
    BooleanField,
    JSONField,
)
from django.utils import timezone
from datetime import datetime, date
from django.core.exceptions import ValidationError
from os.path import join
import calendar

from App.messages.validation_messages import ValidationMessages
from App.models import BaseImageModel, BaseModel
from App.validators import RegexValidators
from App.messages import ModelsMessages, FieldsMessages
from User.utils.enums import GENDERS, TITLES
from Language.models.Language import Language
from Currency.models import Currency
from .User import User


class Profile(BaseModel, BaseImageModel):
    user = OneToOneField(
        User,
        on_delete=CASCADE,
        related_name="Profile",
        verbose_name=ModelsMessages.USER,
    )
    full_name = CharField(
        max_length=150,
        unique=True,
        null=True,
        blank=True,
        error_messages={
            "unique": ValidationMessages.FULL_NAME_INVALID_UNIQUE_VALIDATION_MESSAGE,
        },
        validators=[RegexValidators.full_name_pattern_validator],
        verbose_name=FieldsMessages.FULL_NAME,
    )
    national_id = CharField(
        max_length=14,
        unique=True,
        null=True,
        blank=True,
        error_messages={
            "unique": ValidationMessages.NATIONAL_ID_INVALID_UNIQUE_VALIDATION_MESSAGE,
        },
        validators=[RegexValidators.national_id_pattern_validator],
        verbose_name=FieldsMessages.NATIONAL_ID,
    )
    birth_date = DateField(
        blank=True,
        null=True,
        verbose_name=FieldsMessages.BIRTH_DATE,
    )
    title = CharField(
        max_length=1,
        blank=True,
        null=True,
        choices=TITLES.choices,
        verbose_name=FieldsMessages.TITLE,
    )
    gender = CharField(
        max_length=1,
        blank=True,
        null=True,
        choices=GENDERS.choices,
        verbose_name=FieldsMessages.GENDER,
    )
    university_number = CharField(
        max_length=25,
        blank=True,
        null=True,
        verbose_name=FieldsMessages.UNIVERSITY_NUMBER,
    )
    is_graduate = BooleanField(
        default=True,
        verbose_name=FieldsMessages.GRADUATE_STATUS,
    )
    currency = ForeignKey(
        Currency,
        on_delete=PROTECT,
        blank=True,
        null=True,
        related_name="Persons",
        verbose_name=ModelsMessages.CURRENCY,
    )
    language = ForeignKey(
        Language,
        on_delete=PROTECT,
        blank=True,
        null=True,
        related_name="Persons",
        verbose_name=ModelsMessages.LANGUAGE,
    )
    contact_info = JSONField(
        blank=True,
        null=True,
        verbose_name=FieldsMessages.CONTACT_INFO,
    )

    #############################################################
    ######################### Image Filed  ######################
    #############################################################
    @property
    def avatar(self):
        return (
            self.image.url
            if self.image
            else join("Images", "Profile", "default_avatar.png")
        )

    @avatar.setter
    def avatar(self, value):
        self.image = value

    #############################################################

    @property
    def birth_date_property(self) -> Optional[date]:
        """
        Getter for birth_date that returns a timezone-aware date
        Note: Dates don't actually need timezone handling, but we're being consistent
        """
        return self.birth_date

    @birth_date_property.setter
    def birth_date_property(self, value: Union[str, datetime, date]):
        """
        Setter for birth_date that handles multiple input types:
        - String (form input)
        - datetime object (naive or aware)
        - date object
        """
        if value is None:
            self.birth_date = None
            return

        try:
            if isinstance(value, str):
                # Parse string input (from forms/APIs)
                naive_dt = datetime.strptime(value, "%Y-%m-%d")
                self.birth_date = naive_dt.date()
            elif isinstance(value, datetime):
                # Handle datetime objects (convert to date)
                if timezone.is_aware(value):
                    # Convert to system timezone then get date
                    sys_tz = timezone.get_current_timezone()
                    value = timezone.localtime(value, timezone=sys_tz)
                self.birth_date = value.date()
            elif isinstance(value, date):
                # Direct date assignment
                self.birth_date = value
            else:
                raise ValidationError("Invalid date format")
        except (ValueError, TypeError) as e:
            raise ValidationError(f"Invalid date value: {str(e)}")

    def save(self, *args, **kwargs):
        """Ensure clean data before saving"""
        # You could add additional validation here if needed
        super().save(*args, **kwargs)

    @property
    def age(self):
        born = self.birth_date
        calendar.setfirstweekday(calendar.SUNDAY)
        today = date.today()
        if today.month >= born.month:
            year = today.year
        else:
            year = today.year - 1
        age_years = year - born.year
        try:  # raised when birth day is February 29 and the current year is not a leap year
            age_days = (today - (born.replace(year=year))).days
        except ValueError:
            age_days = (today - (born.replace(year=year, day=born.day - 1))).days + 1
        month = born.month
        age_months = 0
        while age_days > calendar.monthrange(year, month)[1]:
            age_days = age_days - calendar.monthrange(year, month)[1]
            if month == 12:
                month = 1
                year += 1
            else:
                month += 1
            age_months += 1
        return {  # Return dict instead of AgeModel instance
            "years": age_years,
            "months": age_months,
            "days": age_days,
        }

    def __str__(self) -> str:
        return f"Profile-> {self.user.username}"

    def __decode__(self) -> str:
        return f"Profile-> {self.user.username}"

    class Meta:
        verbose_name = ModelsMessages.PROFILE
        verbose_name_plural = ModelsMessages.PROFILES


# # Use Getter and Setter for Birth Date Property
"""
    # Setting the birth date from different input types
    profile = Profile()

    # From string (form input)
    profile.birth_date_property = "2025-04-17"  # Automatically converted

    # From naive datetime
    profile.birth_date_property = datetime(2025, 4, 17)

    # From timezone-aware datetime
    aware_dt = timezone.make_aware(datetime(2025, 4, 17, 10, 5))
    profile.birth_date_property = aware_dt  # Extracts just the date part

    # Getting the value
    print(profile.birth_date_property)  # Returns date object
"""
