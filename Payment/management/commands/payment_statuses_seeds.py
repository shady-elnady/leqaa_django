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
                    "en_US": "Completely Paid",
                    "ar_EG": "مدفوع بالكامل",
                    "ar_AS": "مدفوع بالكامل",
                    "fr_FR": "Entièrement Payé",
                    "tr_TR": "Tamamen Ödendi",
                },
            },
            {
                "name": "Pay later",
                "payment_status_type": PAYMENT_STATUS_TYPES.PartiallyPaid,
                "translations": {
                    "en_US": "Pay later",
                    "ar_EG": "مدفوع لاحقا",
                    "fr_FR": "Payer Plus Tard",
                    "tr_TR": "Sonra öde",
                },
            },
            {
                "name": "Partially Paid",
                "payment_status_type": PAYMENT_STATUS_TYPES.PartiallyPaid,
                "translations": {
                    "en_US": "Partial Paid",
                    "ar_EG": "مدفوع جزئ",
                    "fr_FR": "Partiellement Payé",
                    "tr_TR": "Kısmen Ödenmiş",
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
