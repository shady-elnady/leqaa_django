from django.forms import CharField

from App.fields.widgets.mobile_input import MobileInput
from App.validators import MobileNumberValidator
from App.messages import FieldsMessages, ValidationMessages


class MobileFormField(CharField):
    widget = MobileInput
    default_pattern_validators = [MobileNumberValidator()]
    label = FieldsMessages.MOBILE
    required = False
    help_text = ValidationMessages.MOBILE_INVALID_PATTERN_VALIDATION_MESSAGE
    default_error_messages = {
        "required": ValidationMessages.MOBILE_REQUIRED_VALIDATION_MESSAGE,
        "unique": ValidationMessages.MOBILE_INVALID_UNIQUE_VALIDATION_MESSAGE,
    }

    def __init__(self, **kwargs):
        # The default maximum length of an email is 320 characters per RFC 3696
        # section 3.
        kwargs.setdefault("max_length", 20)
        super().__init__(strip=True, **kwargs)
