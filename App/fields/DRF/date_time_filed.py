from rest_framework import serializers
from django.utils.dateparse import parse_datetime
from rest_framework.serializers import DateTimeField
from django.utils.timezone import make_aware, is_aware


class DateTimeDRFField(DateTimeField):
    """Custom datetime field that handles timezone awareness"""

    def to_internal_value(self, value):
        try:
            if isinstance(value, str):
                parsed = parse_datetime(value)
                if parsed and not is_aware(parsed):
                    return make_aware(parsed)
            return super().to_internal_value(value)
        except (ValueError, TypeError) as e:
            raise serializers.ValidationError(str(e))
