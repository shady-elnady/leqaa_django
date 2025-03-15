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
                    "en-US": "Dollar",
                    "ar-AS": "دولار",
                    "ar-EG": "دولار",
                    "fr-FR": "Dollar",
                    "tr-TR": "Dolar",
                },
            },
            {
                "name": "Rupee's India",
                "iso_code": "INR",
                "symbol": "₹",
                "translations": {
                    "en-US": "Rupee's India",
                    "ar-AS": "روبيه",
                    "ar-EG": "روبيه",
                    "fr-FR": "Roupies Inde",
                    "tr-TR": "Rupisi Hindistan",
                },
            },
            {
                "name": "Dollar's Taiwan",
                "iso_code": "TWD",
                "symbol": "🇹🇼",
                "translations": {
                    "en-US": "Dollar's Taiwan",
                    "ar-AS": "دولار تايونى",
                    "ar-EG": "دولار تايونى",
                    "fr-FR": "Dollar de Taïwan",
                    "tr-TR": "Doları Tayvan",
                },
            },
            {
                "name": "Euro",
                "iso_code": "EUR",
                "symbol": "💶 €",
                "translations": {
                    "en-US": "Euro",
                    "ar-AS": "يورو",
                    "ar-EG": "يورو",
                    "fr-FR": "Euro",
                    "tr-TR": "Euro",
                },
            },
            {
                "name": "Yen",
                "iso_code": "JPY",
                "symbol": "💴",
                "translations": {
                    "en-US": "Yen",
                    "日本語 (にほんご)": "円",
                    "ar-AS": "ين",
                    "ar-EG": "ين",
                    "fr-FR": "Yen",
                    "tr-TR": "Lirası Türkiye",
                },
            },
            {
                "name": "Lira's Turkey",
                "iso_code": "TRY",
                "symbol": "₺",
                "translations": {
                    "en-US": "Lira's Turkey",
                    "Türkçe": "Türk lirası",
                    "ar-AS": "ليرا تركيه",
                    "ar-EG": "ليرا تركيه",
                    "fr-FR": "La Turquie de Lira",
                    "tr-TR": "Lirası Türkiye",
                },
            },
            {
                "name": "Egyptian pound",
                "iso_code": "EGP",
                "symbol": "💷",
                "translations": {
                    "en-US": "Egyptian pound",
                    "ar-AS": "جنيه مصرى",
                    "ar-EG": "جنيه مصرى",
                    "fr-FR": "Livre égyptienne",
                    "tr-TR": "Mısır poundu",
                },
            },
            {
                "name": "Dinar's Jordan",
                "iso_code": "JOD",
                "symbol": "JOD",
                "translations": {
                    "en-US": "Dinar's Jordan",
                    "ar-AS": "دينار أردنى",
                    "ar-EG": "دينار أردنى",
                    "fr-FR": "La Jordanie de Dinar",
                    "tr-TR": "Dinarı Ürdün",
                },
            },
            {
                "name": "Dinar's Kuwait",
                "iso_code": "KWD",
                "symbol": "🇰🇼",
                "translations": {
                    "en-US": "Dinar's Kuwait",
                    "ar-AS": "دينار كويتى",
                    "ar-EG": "دينار كويتى",
                    "fr-FR": "Dinar Koweït",
                    "tr-TR": "Dinarı Kuveyt",
                },
            },
            {
                "name": "Dinar's Libya",
                "iso_code": "LYD",
                "symbol": "LD",
                "translations": {
                    "en-US": "Dinar's Libya",
                    "ar-AS": "دينار ليبى",
                    "ar-EG": "دينار ليبى",
                    "fr-FR": "Dinar Libye",
                    "tr-TR": "Dinarı Libya",
                },
            },
            {
                "name": "Dinar's Tunisia",
                "iso_code": "TND",
                "symbol": "DT",
                "translations": {
                    "en-US": "Dinar's Tunisia",
                    "ar-AS": "دينار تونسى",
                    "ar-EG": "دينار تونسى",
                    "fr-FR": "Dinars tunisiens",
                    "tr-TR": "Dinarı Tunus",
                },
            },
            {
                "name": "Dinar's Iraq",
                "iso_code": "IQD",
                "symbol": "🇮🇶",
                "translations": {
                    "en-US": "Dinar's Iraq",
                    "ar-AS": "دينار عراقى",
                    "ar-EG": "دينار عراقى",
                    "fr-FR": "Dinars Irak",
                    "tr-TR": "Dinarı Irak",
                },
            },
            {
                "name": "Riyal's Qatar",
                "iso_code": "QAR",
                "symbol": "🇶🇦",
                "translations": {
                    "en-US": "Riyal's Qatar",
                    "ar-AS": "ريال قطرى",
                    "ar-EG": "ريال قطرى",
                    "fr-FR": "Riyals du Qatar",
                    "tr-TR": "Riyali Katar",
                },
            },
            {
                "name": "Riyal's Saudi Arabia",
                "iso_code": "SAR",
                "symbol": "🇸🇦",
                "translations": {
                    "en-US": "Riyal's Saudi Arabia",
                    "ar-AS": "ريال سعودى",
                    "ar-EG": "ريال سعودى",
                    "fr-FR": "Riyals Saoudiens",
                    "tr-TR": "Riyali Suudi",
                },
            },
            {
                "name": "Riyal's Oman",
                "iso_code": "OMR",
                "symbol": "🏳️‍🌈",
                "translations": {
                    "en-US": "Riyal's Oman",
                    "ar-AS": "ريال عمانى",
                    "ar-EG": "ريال عمانى",
                    "fr-FR": "Riyals d'Oman",
                    "tr-TR": "Riyali Umman",
                },
            },
            {
                "name": "Dirham",
                "iso_code": "AED",
                "symbol": "🇦🇪",
                "translations": {
                    "en-US": "Dirham",
                    "ar-AS": "درهم إمارتى",
                    "ar-EG": "درهم إمارتى",
                    "fr-FR": "Dirham",
                    "tr-TR": "Dirhemi",
                },
            },
            {
                "name": "French Franc",
                "iso_code": "F",
                "symbol": "₣",
                "translations": {
                    "en-US": "French Franc",
                    "ar-AS": "فرانك",
                    "ar-EG": "فرانك",
                    "fr-FR": "Franc",
                    "tr-TR": "Fransız Frangı",
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
