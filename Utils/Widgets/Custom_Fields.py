from django.db.models import Field, CharField, AutoField  # noqa: F401


class QRField(Field):
    def __init__(self, max_length=24, *args, **kwargs):
        self.max_length = max_length
        super().__init__(*args, **kwargs)

    def db_type(self, connection):
        return "char(%s)" % self.max_length


class BarCodeField(CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 24
        kwargs["primary_key"] = True
        kwargs["verbose_name"] = "BarCode"
        super().__init__(*args, **kwargs)
