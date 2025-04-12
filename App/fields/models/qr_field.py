from django.db.models import Field


class QRModelField(Field):
    def __init__(self, max_length=24, *args, **kwargs):
        self.max_length = max_length
        super().__init__(*args, **kwargs)

    def db_type(self, connection):
        return "char(%s)" % self.max_length
