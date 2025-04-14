from django.core.management.base import BaseCommand

from Payment.models import PaymentMethod
from Payment.utils.enums import PAYMENT_METHOD_TYPES


class Command(BaseCommand):
    data = "Payment Methods"
    help = f"Creates initial {data} model"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        payment_methods = [
            {
                "name": "Monetary",
                "payment_Method_type": PAYMENT_METHOD_TYPES.Monetary,
                "translations": {
                    "en-us": "Monetary",
                    "ar-eg": "نقدى",
                    "ar-as": "نقدى",
                    "fr-fr": "Monétaire",
                    "tr-tr": "Parasal",
                },
            },
            {
                "name": "Credit Card",
                "payment_Method_type": PAYMENT_METHOD_TYPES.CreditCard,
                "translations": {
                    "en-us": "Credit Card",
                    "ar-eg": "بطاقه الائتمان",
                    "fr-fr": "Carte de Crédit",
                    "tr-tr": "Kredi kartı",
                },
            },
            {
                "name": "Bank Transfer",
                "payment_Method_type": PAYMENT_METHOD_TYPES.BankTransfer,
                "translations": {
                    "en-us": "Bank Transfer",
                    "ar-eg": "تحويل مصرفى",
                    "fr-fr": "Virement Bancaire",
                    "tr-tr": "Banka Havalesi",
                },
            },
            {
                "name": "Check",
                "payment_Method_type": PAYMENT_METHOD_TYPES.Check,
                "translations": {
                    "en-us": "Check",
                    "ar-eg": "شيك",
                    "fr-fr": "Vérifier",
                    "tr-tr": "Kontrol etmek",
                },
            },
            {
                "name": "Money Transfer",
                "payment_Method_type": PAYMENT_METHOD_TYPES.MoneyTransfer,
                "translations": {
                    "en-us": "Money Transfer",
                    "ar-eg": "نقل اموال",
                    "fr-fr": "Transfert d'Argent",
                    "tr-tr": "Para Transferi",
                },
            },
        ]

        for paymentMethod in payment_methods:
            try:
                PaymentMethod.objects.create(
                    name=paymentMethod["name"],
                    payment_Method_type=paymentMethod["payment_Method_type"],
                    translations=paymentMethod["translations"],
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully insert {self.data} > {paymentMethod}"
                    )
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed insert {self.data} > {paymentMethod} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING(f"Finish Created initial {self.data}"))
