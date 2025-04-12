from django.core.management.base import BaseCommand

from Address.models import Country, Governorate


class Command(BaseCommand):
    help = "Creates initial Governorates Load Data"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        governorates = [
            {
                "name": "Cairo",
                "governorate_tel_code": "02",
                "country": 1,
                "translations": {
                    "en_US": "Cairo",
                    "ar_EG": "القاهره",
                    "ar_AS": "القاهره",
                    "fr_FR": "Caire",
                    "tr_TR": "Kahire",
                },
            },
            {
                "name": "Alexandria",
                "governorate_tel_code": "03",
                "country": 1,
                "translations": {
                    "en_US": "Alexandria",
                    "ar_EG": "الاسكندريه",
                    "ar_AS": "الاسكندريه",
                    "fr_FR": "Alexandrie",
                    "tr_TR": "İskenderiye",
                },
            },
            {
                "name": "Dakahlia",
                "governorate_tel_code": "050",
                "country": 1,
                "translations": {
                    "en_US": "Dakahlia",
                    "ar_EG": "الدقهليه",
                    "ar_AS": "الدقهليه",
                    "fr_FR": "Dakalie",
                    "tr_TR": "Dakahlia",
                },
            },
            {
                "name": "Aswan",
                "governorate_tel_code": "097",
                "country": 1,
                "translations": {
                    "en_US": "Aswan",
                    "ar_EG": "أسوان",
                    "ar_AS": "أسوان",
                    "fr_FR": "Assouan",
                    "tr_TR": "Aswan",
                },
            },
            {
                "name": "Arish",
                "governorate_tel_code": "068",
                "country": 1,
                "translations": {
                    "en_US": "Arish",
                    "ar_EG": "العريش",
                    "ar_AS": "العريش",
                    "fr_FR": "Arish",
                    "tr_TR": "Arish",
                },
            },
            {
                "name": "Beni Suef",
                "governorate_tel_code": "082",
                "country": 1,
                "translations": {
                    "en_US": "Beni Suef",
                    "ar_EG": "بنى سويف",
                    "ar_AS": "بنى سويف",
                    "fr_FR": "Beni Souef",
                    "tr_TR": "Beni Suef",
                },
            },
            {
                "name": "Damietta",
                "governorate_tel_code": "057",
                "country": 1,
                "translations": {
                    "en_US": "Damietta",
                    "ar_EG": "دمياط",
                    "ar_AS": "دمياط",
                    "fr_FR": "Damiette",
                    "tr_TR": "Damietta",
                },
            },
            {
                "name": "Ismailia",
                "governorate_tel_code": "064",
                "country": 1,
                "translations": {
                    "en_US": "Ismailia",
                    "ar_EG": "اسماعليه",
                    "ar_AS": "اسماعليه",
                    "fr_FR": "Ismaïlia",
                    "tr_TR": "Ismailia",
                },
            },
            {
                "name": "Luxor",
                "governorate_tel_code": "095",
                "country": 1,
                "translations": {
                    "en_US": "Luxor",
                    "ar_EG": "الاقصر",
                    "ar_AS": "الاقصر",
                    "fr_FR": "Louxor",
                    "tr_TR": "Luxor",
                },
            },
            {
                "name": "Monufia",
                "governorate_tel_code": "048",
                "country": 1,
                "translations": {
                    "en_US": "Monufia",
                    "ar_EG": "منوفيه",
                    "ar_AS": "منوفيه",
                    "fr_FR": "Monoufia",
                    "tr_TR": "Monufia",
                },
            },
            {
                "name": "Port Said",
                "governorate_tel_code": "066",
                "country": 1,
                "translations": {
                    "en_US": "Port Said",
                    "ar_EG": "بورسعيد",
                    "ar_AS": "بورسعيد",
                    "fr_FR": "Port-Saïd",
                    "tr_TR": "Port Said",
                },
            },
            {
                "name": "Red Sea",
                "governorate_tel_code": "065",
                "country": 1,
                "translations": {
                    "en_US": "Red Sea",
                    "ar_EG": "البحرالاحمر",
                    "ar_AS": "البحرالاحمر",
                    "fr_FR": "Mer Rouge",
                    "tr_TR": "Kızıldeniz",
                },
            },
            {
                "name": "Suez",
                "governorate_tel_code": "062",
                "country": 1,
                "translations": {
                    "en_US": "Suez",
                    "ar_EG": "السويس",
                    "ar_AS": "السويس",
                    "fr_FR": "Suez",
                    "tr_TR": "Süveyş",
                },
            },
            {
                "name": "El Tour",
                "governorate_tel_code": "069",
                "country": 1,
                "translations": {
                    "en_US": "El Tour",
                    "ar_EG": "الطور",
                    "ar_AS": "الطور",
                    "fr_FR": "Le Tour",
                    "tr_TR": "El Turu",
                },
            },
            {
                "name": "10th of Ramadan",
                "governorate_tel_code": "055",
                "country": 1,
                "translations": {
                    "en_US": "10th of Ramadan",
                    "ar_EG": "العاشر من رمضان",
                    "ar_AS": "العاشر من رمضان",
                    "fr_FR": "10ème Ramadan",
                    "tr_TR": "10 Ramazan",
                },
            },
            {
                "name": "Asyut",
                "governorate_tel_code": "088",
                "country": 1,
                "translations": {
                    "en_US": "Asyut",
                    "ar_EG": "أسيوط",
                    "ar_AS": "أسيوط",
                    "fr_FR": "Assiout",
                    "tr_TR": "Asyut",
                },
            },
            {
                "name": "Damanhur",
                "governorate_tel_code": "04",
                "country": 1,
                "translations": {
                    "en_US": "Damanhur",
                    "ar_EG": "دمنهور",
                    "ar_AS": "دمنهور",
                    "fr_FR": "Damanhur",
                    "tr_TR": "Damanhur",
                },
            },
            {
                "name": "Faiyum",
                "governorate_tel_code": "084",
                "country": 1,
                "translations": {
                    "en_US": "Faiyum",
                    "ar_EG": "الفيوم",
                    "ar_AS": "الفيوم",
                    "fr_FR": "Fayoum",
                    "tr_TR": "Faiyum",
                },
            },
            {
                "name": "Kafr El Sheikh",
                "governorate_tel_code": "047",
                "country": 1,
                "translations": {
                    "en_US": "Kafr El Sheikh",
                    "ar_EG": "كفرالشيخ",
                    "ar_AS": "كفرالشيخ",
                    "fr_FR": "Kafr El Sheikh",
                    "tr_TR": "Kafr El Şeyh",
                },
            },
            {
                "name": "Marsa Matruh",
                "governorate_tel_code": "046",
                "country": 1,
                "translations": {
                    "en_US": "Marsa Matruh",
                    "ar_EG": "مرسى مطروح",
                    "ar_AS": "مرسى مطروح",
                    "fr_FR": "Marsa Matrouh",
                    "tr_TR": "Marsa Matruh",
                },
            },
            {
                "name": "Minya",
                "governorate_tel_code": "086",
                "country": 1,
                "translations": {
                    "en_US": "Minya",
                    "ar_EG": "المنيا",
                    "ar_AS": "المنيا",
                    "fr_FR": "Minya",
                    "tr_TR": "Minya",
                },
            },
            {
                "name": "New Valley",
                "governorate_tel_code": "092",
                "country": 1,
                "translations": {
                    "en_US": "New Valley",
                    "ar_EG": "الوادى الجديد",
                    "ar_AS": "الوادى الجديد",
                    "fr_FR": "Nouvelle Vallée",
                    "tr_TR": "Yeni Vadi",
                },
            },
            {
                "name": "Sohag",
                "governorate_tel_code": "093",
                "country": 1,
                "translations": {
                    "en_US": "Sohag",
                    "ar_EG": "سوهاج",
                    "ar_AS": "سوهاج",
                    "fr_FR": "Sohag",
                    "tr_TR": "Sohag",
                },
            },
            {
                "name": "Qena",
                "governorate_tel_code": "096",
                "country": 1,
                "translations": {
                    "en_US": "Qena",
                    "ar_EG": "قنا",
                    "ar_AS": "قنا",
                    "fr_FR": "Qéna",
                    "tr_TR": "Qena",
                },
            },
            {
                "name": "Tanta",
                "governorate_tel_code": "040",
                "country": 1,
                "translations": {
                    "en_US": "Tanta",
                    "ar_EG": "طنطا",
                    "ar_AS": "طنطا",
                    "fr_FR": "Tanta",
                    "tr_TR": "Tanta",
                },
            },
            {
                "name": "Qalyubia",
                "governorate_tel_code": "013",
                "country": 1,
                "translations": {
                    "en_US": "Qalyubia",
                    "ar_EG": "قليوبيه",
                    "ar_AS": "قليوبيه",
                    "fr_FR": "Qalyubia",
                    "tr_TR": "Qalyubia",
                },
            },
            {
                "name": "Isle of France",
                "governorate_tel_code": "1",
                "country": 3,
                "translations": {
                    "en_US": "Isle of France",
                    "ar_EG": "جزيرة فرنسا",
                    "ar_AS": "جزيرة فرنسا",
                    "fr_FR": "Île de France",
                    "tr_TR": "Fransa Adası",
                },
            },
            {
                "name": "Emirate of Abu Dhabi",
                "governorate_tel_code": "2",
                "country": 3,
                "translations": {
                    "en_US": "Emirate of Abu Dhabi",
                    "ar_EG": "إمارة أبو ظبي",
                    "ar_AS": "إمارة أبو ظبي",
                    "fr_FR": "Emirat d'Abou Dhabi",
                    "tr_TR": "Abu Dabi Emirliği",
                },
            },
        ]

        for governorate in governorates:
            try:
                Governorate.objects.create(
                    name=governorate["name"],
                    country=Country.objects.get(pk=governorate["country"]),
                    governorate_tel_code=governorate["governorate_tel_code"],
                    translations=governorate["translations"],
                )

                self.stdout.write(
                    self.style.SUCCESS(f"Successfully Create {governorate['name']}")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed Create {governorate['name']} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING("Finish Initial Governorates Load Data"))
