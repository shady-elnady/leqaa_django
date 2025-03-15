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
from django.utils.translation import gettext_lazy as _
from datetime import date
import calendar

from Utils.models.BaseModel import BasAvatarModel, BaseModel
from User.utils.userRegexValidators import UserRegexValidators
from User.utils.usereMessages import UserMessages
from User.utils.enums import GENDERS, TITLES
from Locale.models.Language import Language
from Currency.models import Currency
from .User import User


class AgeModel(Model):
    day = PositiveSmallIntegerField(
        default=0,
        verbose_name=_("Day"),
    )
    month = PositiveSmallIntegerField(
        default=0,
        verbose_name=_("Month"),
    )
    year = PositiveSmallIntegerField(
        default=0,
        verbose_name=_("Year"),
    )

    class Meta:
        abstract = True


class Profile(BaseModel, BasAvatarModel):
    user = OneToOneField(
        User,
        on_delete=CASCADE,
        related_name="Profile",
        verbose_name=_("User"),
    )
    full_name = CharField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name=_("Full Name"),
    )
    national_id = CharField(
        max_length=14,
        unique=True,
        null=True,
        blank=True,
        error_messages={"unique": UserMessages.NATIONAL_ID_UNIQUE_VALIDATION},
        validators=[UserRegexValidators.national_id_regex],
        verbose_name=_("National ID"),
    )
    birth_date = DateField(
        blank=True,
        null=True,
        verbose_name=_("Birth Date"),
    )
    title = CharField(
        max_length=1,
        blank=True,
        null=True,
        choices=TITLES.choices,
        verbose_name=_("Title"),
    )
    gender = CharField(
        max_length=1,
        blank=True,
        null=True,
        choices=GENDERS.choices,
        verbose_name=_("Gender"),
    )
    university_number = CharField(
        max_length=25,
        blank=True,
        null=True,
        verbose_name=_("University Number"),
    )
    is_graduate = BooleanField(
        default=True,
        verbose_name=_("is Graduate"),
    )
    currency = ForeignKey(
        Currency,
        on_delete=PROTECT,
        blank=True,
        null=True,
        related_name=_("Persons"),
        verbose_name=_("Currency"),
    )
    language = ForeignKey(
        Language,
        on_delete=PROTECT,
        blank=True,
        null=True,
        related_name=_("Persons"),
        verbose_name=_("Language"),
    )
    contact_info = JSONField(
        blank=True,
        null=True,
        verbose_name=_("Contact Info"),
    )

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
        return AgeModel(
            year=age_years,
            month=age_months,
            day=age_days,
        )

    def __str__(self) -> str:
        return f"Profile-> {self.user.username}"

    def __decode__(self) -> str:
        return f"Profile-> {self.user.username}"

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
