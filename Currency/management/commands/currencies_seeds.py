from django.core.management.base import BaseCommand

from Currency.models import Currency


class Command(BaseCommand):
    data = "Currencies"
    help = "Creates initial Currencies Load Data"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        currencies = [
            {
                "name": "Dollar",
                "iso_code": "USD",
                "symbol": "💲",
                "translations": {
                    "en_US": "Dollar",
                    "ar_AS": "دولار",
                    "ar_EG": "دولار",
                    "fr_FR": "Dollar",
                    "tr_TR": "Dolar",
                },
            },
            {
                "name": "Rupee's India",
                "iso_code": "INR",
                "symbol": "₹",
                "translations": {
                    "en_US": "Rupee's India",
                    "ar_AS": "روبيه",
                    "ar_EG": "روبيه",
                    "fr_FR": "Roupies Inde",
                    "tr_TR": "Rupisi Hindistan",
                },
            },
            {
                "name": "Dollar's Taiwan",
                "iso_code": "TWD",
                "symbol": "🇹🇼",
                "translations": {
                    "en_US": "Dollar's Taiwan",
                    "ar_AS": "دولار تايونى",
                    "ar_EG": "دولار تايونى",
                    "fr_FR": "Dollar de Taïwan",
                    "tr_TR": "Doları Tayvan",
                },
            },
            {
                "name": "Euro",
                "iso_code": "EUR",
                "symbol": "💶 €",
                "translations": {
                    "en_US": "Euro",
                    "ar_AS": "يورو",
                    "ar_EG": "يورو",
                    "fr_FR": "Euro",
                    "tr_TR": "Euro",
                },
            },
            {
                "name": "Yen",
                "iso_code": "JPY",
                "symbol": "💴",
                "translations": {
                    "en_US": "Yen",
                    "日本語 (にほんご)": "円",
                    "ar_AS": "ين",
                    "ar_EG": "ين",
                    "fr_FR": "Yen",
                    "tr_TR": "Lirası Türkiye",
                },
            },
            {
                "name": "Lira's Turkey",
                "iso_code": "TRY",
                "symbol": "₺",
                "translations": {
                    "en_US": "Lira's Turkey",
                    "Türkçe": "Türk lirası",
                    "ar_AS": "ليرا تركيه",
                    "ar_EG": "ليرا تركيه",
                    "fr_FR": "La Turquie de Lira",
                    "tr_TR": "Lirası Türkiye",
                },
            },
            {
                "name": "Egyptian pound",
                "iso_code": "EGP",
                "symbol": "💷",
                "translations": {
                    "en_US": "Egyptian pound",
                    "ar_AS": "جنيه مصرى",
                    "ar_EG": "جنيه مصرى",
                    "fr_FR": "Livre égyptienne",
                    "tr_TR": "Mısır poundu",
                },
            },
            {
                "name": "Dinar's Jordan",
                "iso_code": "JOD",
                "symbol": "JOD",
                "translations": {
                    "en_US": "Dinar's Jordan",
                    "ar_AS": "دينار أردنى",
                    "ar_EG": "دينار أردنى",
                    "fr_FR": "La Jordanie de Dinar",
                    "tr_TR": "Dinarı Ürdün",
                },
            },
            {
                "name": "Dinar's Kuwait",
                "iso_code": "KWD",
                "symbol": "🇰🇼",
                "translations": {
                    "en_US": "Dinar's Kuwait",
                    "ar_AS": "دينار كويتى",
                    "ar_EG": "دينار كويتى",
                    "fr_FR": "Dinar Koweït",
                    "tr_TR": "Dinarı Kuveyt",
                },
            },
            {
                "name": "Dinar's Libya",
                "iso_code": "LYD",
                "symbol": "LD",
                "translations": {
                    "en_US": "Dinar's Libya",
                    "ar_AS": "دينار ليبى",
                    "ar_EG": "دينار ليبى",
                    "fr_FR": "Dinar Libye",
                    "tr_TR": "Dinarı Libya",
                },
            },
            {
                "name": "Dinar's Tunisia",
                "iso_code": "TND",
                "symbol": "DT",
                "translations": {
                    "en_US": "Dinar's Tunisia",
                    "ar_AS": "دينار تونسى",
                    "ar_EG": "دينار تونسى",
                    "fr_FR": "Dinars tunisiens",
                    "tr_TR": "Dinarı Tunus",
                },
            },
            {
                "name": "Dinar's Iraq",
                "iso_code": "IQD",
                "symbol": "🇮🇶",
                "translations": {
                    "en_US": "Dinar's Iraq",
                    "ar_AS": "دينار عراقى",
                    "ar_EG": "دينار عراقى",
                    "fr_FR": "Dinars Irak",
                    "tr_TR": "Dinarı Irak",
                },
            },
            {
                "name": "Riyal's Qatar",
                "iso_code": "QAR",
                "symbol": "🇶🇦",
                "translations": {
                    "en_US": "Riyal's Qatar",
                    "ar_AS": "ريال قطرى",
                    "ar_EG": "ريال قطرى",
                    "fr_FR": "Riyals du Qatar",
                    "tr_TR": "Riyali Katar",
                },
            },
            {
                "name": "Riyal's Saudi Arabia",
                "iso_code": "SAR",
                "symbol": "🇸🇦",
                "translations": {
                    "en_US": "Riyal's Saudi Arabia",
                    "ar_AS": "ريال سعودى",
                    "ar_EG": "ريال سعودى",
                    "fr_FR": "Riyals Saoudiens",
                    "tr_TR": "Riyali Suudi",
                },
            },
            {
                "name": "Riyal's Oman",
                "iso_code": "OMR",
                "symbol": "🏳️‍🌈",
                "translations": {
                    "en_US": "Riyal's Oman",
                    "ar_AS": "ريال عمانى",
                    "ar_EG": "ريال عمانى",
                    "fr_FR": "Riyals d'Oman",
                    "tr_TR": "Riyali Umman",
                },
            },
            {
                "name": "Dirham",
                "iso_code": "AED",
                "symbol": "🇦🇪",
                "translations": {
                    "en_US": "Dirham",
                    "ar_AS": "درهم إمارتى",
                    "ar_EG": "درهم إمارتى",
                    "fr_FR": "Dirham",
                    "tr_TR": "Dirhemi",
                },
            },
            {
                "name": "French Franc",
                "iso_code": "F",
                "symbol": "₣",
                "translations": {
                    "en_US": "French Franc",
                    "ar_AS": "فرانك",
                    "ar_EG": "فرانك",
                    "fr_FR": "Franc",
                    "tr_TR": "Fransız Frangı",
                },
            },
        ]

        for currency in currencies:
            try:
                Currency.objects.create(
                    name=currency["name"],
                    iso_code=currency["iso_code"],
                    symbol=currency["symbol"],
                    translations=currency["translations"],
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully insert {self.data} > {currency['name']}"
                    )
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed insert {self.data} > {currency['name']} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING(f"Finish Created initial {self.data}"))
