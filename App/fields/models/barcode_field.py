from django.db.models import CharField


class BarcodeModelField(CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 24
        kwargs["primary_key"] = True
        kwargs["verbose_name"] = "BarCode"
        super().__init__(*args, **kwargs)
