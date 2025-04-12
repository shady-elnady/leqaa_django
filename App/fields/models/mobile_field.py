from django.db.models import CharField

from App.fields.forms.mobile_field import MobileFormField
from App.messages import FieldsMessages, ValidationMessages
from App.validators import MobileNumberValidator


class MobileModelField(CharField):
    default_pattern_validators = [MobileNumberValidator()]
    description = FieldsMessages.MOBILE

    def __init__(self, *args, **kwargs):
        # max_length=254 to be compliant with RFCs 3696 and 5321
        kwargs.setdefault("max_length", 20)
        kwargs.setdefault("verbose_name", FieldsMessages.MOBILE)
        kwargs.setdefault("unique", True)
        kwargs.setdefault("blank", True)
        kwargs.setdefault("null", True)
        kwargs.setdefault(
            "error_messages",
            {
                "unique": ValidationMessages.MOBILE_INVALID_UNIQUE_VALIDATION_MESSAGE,
            },
        )
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        # We do not exclude max_length if it matches default as we want to change
        # the default in future.
        return name, path, args, kwargs

    def formfield(self, **kwargs):
        # As with CharField, this will cause email validation to be performed
        # twice.
        return super().formfield(
            **{
                "form_class": MobileFormField,
                **kwargs,
            }
        )
