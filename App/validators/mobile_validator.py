from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
import re

from App.messages import ValidationMessages
from App.validators import RegexValidators


@deconstructible
class MobileNumberValidator:
    message = ValidationMessages.MOBILE_INVALID_PATTERN_VALIDATION_MESSAGE
    code = "invalid"
    mobile_regex = RegexValidators.MOBILE_REGEX

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        cleaned_value = self.clean_phone_number(value)
        if not self.mobile_regex.match(cleaned_value):
            raise ValidationError(self.message, code=self.code, params={"value": value})

    def __eq__(self, other):
        return (
            isinstance(other, MobileNumberValidator)
            and self.message == other.message
            and self.code == other.code
        )

    def clean_phone_number(self, value):
        """Normalize phone number by removing all non-digit characters except leading +"""
        if not value:
            return value

        # Keep only digits and +
        cleaned = re.sub(r"[^\d+]", "", value)

        # Ensure + is at start if present
        if "+" in cleaned and not cleaned.startswith("+"):
            cleaned = "+" + cleaned.replace("+", "")

        return cleaned

    def get_help_text(self):
        return self.message
