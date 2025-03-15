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
                    "en-US": "Monetary",
                    "ar-EG": "نقدى",
                    "ar-AS": "نقدى",
                    "fr-FR": "Monétaire",
                    "tr-TR": "Parasal",
                },
            },
            {
                "name": "Credit Card",
                "payment_Method_type": PAYMENT_METHOD_TYPES.CreditCard,
                "translations": {
                    "en-US": "Credit Card",
                    "ar-EG": "بطاقه الائتمان",
                    "fr-FR": "Carte de Crédit",
                    "tr-TR": "Kredi kartı",
                },
            },
            {
                "name": "Bank Transfer",
                "payment_Method_type": PAYMENT_METHOD_TYPES.BankTransfer,
                "translations": {
                    "en-US": "Bank Transfer",
                    "ar-EG": "تحويل مصرفى",
                    "fr-FR": "Virement Bancaire",
                    "tr-TR": "Banka Havalesi",
                },
            },
            {
                "name": "Check",
                "payment_Method_type": PAYMENT_METHOD_TYPES.Check,
                "translations": {
                    "en-US": "Check",
                    "ar-EG": "شيك",
                    "fr-FR": "Vérifier",
                    "tr-TR": "Kontrol etmek",
                },
            },
            {
                "name": "Money Transfer",
                "payment_Method_type": PAYMENT_METHOD_TYPES.MoneyTransfer,
                "translations": {
                    "en-US": "Money Transfer",
                    "ar-EG": "نقل اموال",
                    "fr-FR": "Transfert d'Argent",
                    "tr-TR": "Para Transferi",
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
