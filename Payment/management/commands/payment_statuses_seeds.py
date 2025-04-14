from django.core.management.base import BaseCommand

from Payment.models import PaymentStatus
from Payment.utils.enums import PAYMENT_STATUS_TYPES


class Command(BaseCommand):
    data = "Payment Methods"
    help = f"Creates initial {data} model"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        payment_statuses = [
            {
                "name": "Completely Paid",
                "payment_status_type": PAYMENT_STATUS_TYPES.Paid,
                "translations": {
                    "en-us": "Completely Paid",
                    "ar-eg": "مدفوع بالكامل",
                    "ar-as": "مدفوع بالكامل",
                    "fr-fr": "Entièrement Payé",
                    "tr-tr": "Tamamen Ödendi",
                },
            },
            {
                "name": "Pay later",
                "payment_status_type": PAYMENT_STATUS_TYPES.PartiallyPaid,
                "translations": {
                    "en-us": "Pay later",
                    "ar-eg": "مدفوع لاحقا",
                    "fr-fr": "Payer Plus Tard",
                    "tr-tr": "Sonra öde",
                },
            },
            {
                "name": "Partially Paid",
                "payment_status_type": PAYMENT_STATUS_TYPES.PartiallyPaid,
                "translations": {
                    "en-us": "Partial Paid",
                    "ar-eg": "مدفوع جزئ",
                    "fr-fr": "Partiellement Payé",
                    "tr-tr": "Kısmen Ödenmiş",
                },
            },
        ]

        for paymentStatus in payment_statuses:
            try:
                PaymentStatus.objects.create(
                    name=paymentStatus["name"],
                    payment_status_type=paymentStatus["payment_status_type"],
                    translations=paymentStatus["translations"],
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully insert {self.data} > {paymentStatus}"
                    )
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed insert {self.data} > {paymentStatus} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING(f"Finish Created initial {self.data}"))
