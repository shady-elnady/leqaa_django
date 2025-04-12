from rest_framework.serializers import CharField

from App.messages import ValidationMessages
from App.validators import MobileNumberValidator


class MobileDRFField(CharField):
    default_error_messages = {
        "unique": ValidationMessages.MOBILE_INVALID_UNIQUE_VALIDATION_MESSAGE,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        validator = MobileNumberValidator()
        self.max_length = 20
        self.required = False
        self.allow_blank = True
        self.allow_null = True
        self.validators.append(validator)
