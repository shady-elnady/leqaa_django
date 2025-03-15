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
                    "en-US": "Completely Paid",
                    "ar-EG": "مدفوع بالكامل",
                    "ar-AS": "مدفوع بالكامل",
                    "fr-FR": "Entièrement Payé",
                    "tr-TR": "Tamamen Ödendi",
                },
            },
            {
                "name": "Pay later",
                "payment_status_type": PAYMENT_STATUS_TYPES.PartiallyPaid,
                "translations": {
                    "en-US": "Pay later",
                    "ar-EG": "مدفوع لاحقا",
                    "fr-FR": "Payer Plus Tard",
                    "tr-TR": "Sonra öde",
                },
            },
            {
                "name": "Partially Paid",
                "payment_status_type": PAYMENT_STATUS_TYPES.PartiallyPaid,
                "translations": {
                    "en-US": "Partial Paid",
                    "ar-EG": "مدفوع جزئ",
                    "fr-FR": "Partiellement Payé",
                    "tr-TR": "Kısmen Ödenmiş",
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
