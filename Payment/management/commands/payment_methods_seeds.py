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
                    "en_US": "Monetary",
                    "ar_EG": "نقدى",
                    "ar_AS": "نقدى",
                    "fr_FR": "Monétaire",
                    "tr_TR": "Parasal",
                },
            },
            {
                "name": "Credit Card",
                "payment_Method_type": PAYMENT_METHOD_TYPES.CreditCard,
                "translations": {
                    "en_US": "Credit Card",
                    "ar_EG": "بطاقه الائتمان",
                    "fr_FR": "Carte de Crédit",
                    "tr_TR": "Kredi kartı",
                },
            },
            {
                "name": "Bank Transfer",
                "payment_Method_type": PAYMENT_METHOD_TYPES.BankTransfer,
                "translations": {
                    "en_US": "Bank Transfer",
                    "ar_EG": "تحويل مصرفى",
                    "fr_FR": "Virement Bancaire",
                    "tr_TR": "Banka Havalesi",
                },
            },
            {
                "name": "Check",
                "payment_Method_type": PAYMENT_METHOD_TYPES.Check,
                "translations": {
                    "en_US": "Check",
                    "ar_EG": "شيك",
                    "fr_FR": "Vérifier",
                    "tr_TR": "Kontrol etmek",
                },
            },
            {
                "name": "Money Transfer",
                "payment_Method_type": PAYMENT_METHOD_TYPES.MoneyTransfer,
                "translations": {
                    "en_US": "Money Transfer",
                    "ar_EG": "نقل اموال",
                    "fr_FR": "Transfert d'Argent",
                    "tr_TR": "Para Transferi",
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
