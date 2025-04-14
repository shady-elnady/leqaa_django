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
                    "en-us": "Dollar",
                    "ar-as": "دولار",
                    "ar-eg": "دولار",
                    "fr-fr": "Dollar",
                    "tr-tr": "Dolar",
                },
            },
            {
                "name": "Rupee's India",
                "iso_code": "INR",
                "symbol": "₹",
                "translations": {
                    "en-us": "Rupee's India",
                    "ar-as": "روبيه",
                    "ar-eg": "روبيه",
                    "fr-fr": "Roupies Inde",
                    "tr-tr": "Rupisi Hindistan",
                },
            },
            {
                "name": "Dollar's Taiwan",
                "iso_code": "TWD",
                "symbol": "🇹🇼",
                "translations": {
                    "en-us": "Dollar's Taiwan",
                    "ar-as": "دولار تايونى",
                    "ar-eg": "دولار تايونى",
                    "fr-fr": "Dollar de Taïwan",
                    "tr-tr": "Doları Tayvan",
                },
            },
            {
                "name": "Euro",
                "iso_code": "EUR",
                "symbol": "💶 €",
                "translations": {
                    "en-us": "Euro",
                    "ar-as": "يورو",
                    "ar-eg": "يورو",
                    "fr-fr": "Euro",
                    "tr-tr": "Euro",
                },
            },
            {
                "name": "Yen",
                "iso_code": "JPY",
                "symbol": "💴",
                "translations": {
                    "en-us": "Yen",
                    "日本語 (にほんご)": "円",
                    "ar-as": "ين",
                    "ar-eg": "ين",
                    "fr-fr": "Yen",
                    "tr-tr": "Lirası Türkiye",
                },
            },
            {
                "name": "Lira's Turkey",
                "iso_code": "TRY",
                "symbol": "₺",
                "translations": {
                    "en-us": "Lira's Turkey",
                    "Türkçe": "Türk lirası",
                    "ar-as": "ليرا تركيه",
                    "ar-eg": "ليرا تركيه",
                    "fr-fr": "La Turquie de Lira",
                    "tr-tr": "Lirası Türkiye",
                },
            },
            {
                "name": "Egyptian pound",
                "iso_code": "EGP",
                "symbol": "💷",
                "translations": {
                    "en-us": "Egyptian pound",
                    "ar-as": "جنيه مصرى",
                    "ar-eg": "جنيه مصرى",
                    "fr-fr": "Livre égyptienne",
                    "tr-tr": "Mısır poundu",
                },
            },
            {
                "name": "Dinar's Jordan",
                "iso_code": "JOD",
                "symbol": "JOD",
                "translations": {
                    "en-us": "Dinar's Jordan",
                    "ar-as": "دينار أردنى",
                    "ar-eg": "دينار أردنى",
                    "fr-fr": "La Jordanie de Dinar",
                    "tr-tr": "Dinarı Ürdün",
                },
            },
            {
                "name": "Dinar's Kuwait",
                "iso_code": "KWD",
                "symbol": "🇰🇼",
                "translations": {
                    "en-us": "Dinar's Kuwait",
                    "ar-as": "دينار كويتى",
                    "ar-eg": "دينار كويتى",
                    "fr-fr": "Dinar Koweït",
                    "tr-tr": "Dinarı Kuveyt",
                },
            },
            {
                "name": "Dinar's Libya",
                "iso_code": "LYD",
                "symbol": "LD",
                "translations": {
                    "en-us": "Dinar's Libya",
                    "ar-as": "دينار ليبى",
                    "ar-eg": "دينار ليبى",
                    "fr-fr": "Dinar Libye",
                    "tr-tr": "Dinarı Libya",
                },
            },
            {
                "name": "Dinar's Tunisia",
                "iso_code": "TND",
                "symbol": "DT",
                "translations": {
                    "en-us": "Dinar's Tunisia",
                    "ar-as": "دينار تونسى",
                    "ar-eg": "دينار تونسى",
                    "fr-fr": "Dinars tunisiens",
                    "tr-tr": "Dinarı Tunus",
                },
            },
            {
                "name": "Dinar's Iraq",
                "iso_code": "IQD",
                "symbol": "🇮🇶",
                "translations": {
                    "en-us": "Dinar's Iraq",
                    "ar-as": "دينار عراقى",
                    "ar-eg": "دينار عراقى",
                    "fr-fr": "Dinars Irak",
                    "tr-tr": "Dinarı Irak",
                },
            },
            {
                "name": "Riyal's Qatar",
                "iso_code": "QAR",
                "symbol": "🇶🇦",
                "translations": {
                    "en-us": "Riyal's Qatar",
                    "ar-as": "ريال قطرى",
                    "ar-eg": "ريال قطرى",
                    "fr-fr": "Riyals du Qatar",
                    "tr-tr": "Riyali Katar",
                },
            },
            {
                "name": "Riyal's Saudi Arabia",
                "iso_code": "SAR",
                "symbol": "🇸🇦",
                "translations": {
                    "en-us": "Riyal's Saudi Arabia",
                    "ar-as": "ريال سعودى",
                    "ar-eg": "ريال سعودى",
                    "fr-fr": "Riyals Saoudiens",
                    "tr-tr": "Riyali Suudi",
                },
            },
            {
                "name": "Riyal's Oman",
                "iso_code": "OMR",
                "symbol": "🏳️‍🌈",
                "translations": {
                    "en-us": "Riyal's Oman",
                    "ar-as": "ريال عمانى",
                    "ar-eg": "ريال عمانى",
                    "fr-fr": "Riyals d'Oman",
                    "tr-tr": "Riyali Umman",
                },
            },
            {
                "name": "Dirham",
                "iso_code": "AED",
                "symbol": "🇦🇪",
                "translations": {
                    "en-us": "Dirham",
                    "ar-as": "درهم إمارتى",
                    "ar-eg": "درهم إمارتى",
                    "fr-fr": "Dirham",
                    "tr-tr": "Dirhemi",
                },
            },
            {
                "name": "French Franc",
                "iso_code": "F",
                "symbol": "₣",
                "translations": {
                    "en-us": "French Franc",
                    "ar-as": "فرانك",
                    "ar-eg": "فرانك",
                    "fr-fr": "Franc",
                    "tr-tr": "Fransız Frangı",
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
