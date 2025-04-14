import uuid
from django.db.models import (
    Model,
    UUIDField,
    AutoField,
    CharField,
    DateTimeField,
)
from datetime import datetime
from typing import Optional, Union
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.utils.timezone import make_aware, is_aware

from App.messages import FieldsMessages
from App.fields import BarcodeModelField
from App.tools import uuid_to_urlsafe_base64

# Create your models here.


class BaseModel(Model):
    id = AutoField(
        primary_key=True,
        verbose_name=FieldsMessages.ID,
    )
    uid = UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        verbose_name=FieldsMessages.UID,
    )
    created_at = DateTimeField(
        auto_now_add=True,
        editable=False,
        db_index=True,
        verbose_name=FieldsMessages.CREATED_AT,
    )
    last_updated = DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name=FieldsMessages.LAST_UPDATE,
    )

    # ==================== Start DateTime Property ====================
    @property
    def uid_to_urlsafe_base64(self):
        return uuid_to_urlsafe_base64(self.uid)

    # ==================== Start DateTime Property ====================
    @property
    def created_datetime(self) -> Optional[datetime]:
        """
        Getter for created_at_date_time that ensures timezone awareness
        Returns:
            Optional[datetime]: Timezone-aware datetime or None
        """
        if self.created_at is None:
            return None
        if not is_aware(self.created_at):
            return make_aware(self.created_at)
        return self.created_at

    @created_datetime.setter
    def created_datetime(self, value: Union[str, datetime, None]):
        """
        Setter for start_date_time that handles multiple input types
        Args:
            value: Can be string, datetime (naive or aware), or None
        Raises:
            ValidationError: If input format is invalid
        """
        self.created_at = self._parse_datetime(value)

    # ==================== End DateTime Property ====================
    @property
    def last_update(self) -> Optional[datetime]:
        """
        Getter for last_updated that ensures timezone awareness
        Returns:
            Optional[datetime]: Timezone-aware datetime or None
        """
        if self.last_updated is None:
            return None
        if not is_aware(self.last_updated):
            return make_aware(self.last_updated)
        return self.last_updated

    @last_update.setter
    def last_update(self, value: Union[str, datetime, None]):
        """
        Setter for last_updated that handles multiple input types
        Args:
            value: Can be string, datetime (naive or aware), or None
        Raises:
            ValidationError: If input format is invalid
        """
        self.last_updated = self._parse_datetime(value)

    # ==================== Shared Helper Method ====================
    def _parse_datetime(self, value: Union[str, datetime, None]) -> Optional[datetime]:
        """
        Parse datetime input into timezone-aware datetime
        Args:
            value: Input value to parse
        Returns:
            Optional[datetime]: Parsed datetime or None
        Raises:
            ValidationError: If input format is invalid
        """
        if value is None:
            return None

        try:
            if isinstance(value, str):
                # Parse string input (multiple formats)
                for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M"):
                    try:
                        dt = datetime.strptime(value, fmt)
                        return make_aware(dt)
                    except ValueError:
                        continue
                raise ValueError("No valid datetime format found")

            elif isinstance(value, datetime):
                # Handle datetime objects
                if not is_aware(value):
                    return make_aware(value)
                return value

            else:
                raise TypeError("Invalid datetime type")

        except (ValueError, TypeError) as e:
            raise ValidationError(f"Invalid datetime value: {str(e)}")

    def __str__(self) -> str:
        return str(self.uid)

    def __decode__(self) -> str:
        return str(self.uid)

    @property
    def slug(self) -> str:
        return slugify(f"{self.uid}")

    class Meta:
        ordering = "-last_updated"
        abstract = True


class BaseBarcodeModel(Model):
    bar_code = BarcodeModelField(
        verbose_name=FieldsMessages.BARCODE,
    )

    @property
    def slug(self) -> str:
        return slugify(f"{self.bar_code}")

    class Meta:
        abstract = True


class BaseNameModel(BaseModel):
    name = CharField(
        max_length=50,
        unique=True,
        verbose_name=FieldsMessages.NAME,
    )

    def __str__(self) -> str:
        return f"{self.name}"

    def __decode__(self) -> str:
        return f"{self.name}"

    class Meta:
        abstract = True


class BaseNativeModel(BaseNameModel):
    native_name = CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True,
        verbose_name=FieldsMessages.NATIVE_NAME,
    )

    def __str__(self) -> str:
        return f"{self.native_name}"

    def __decode__(self) -> str:
        return f"{self.native_name}"

    class Meta:
        abstract = True


class BaseEmojiModel(Model):
    emoji = CharField(
        max_length=5,
        unique=True,
        null=True,
        blank=True,
        verbose_name=FieldsMessages.EMOJI,
    )

    class Meta:
        abstract = True
