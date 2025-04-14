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
                    "en-us": "Cairo",
                    "ar-eg": "القاهره",
                    "ar-as": "القاهره",
                    "fr-fr": "Caire",
                    "tr-tr": "Kahire",
                },
            },
            {
                "name": "Alexandria",
                "governorate_tel_code": "03",
                "country": 1,
                "translations": {
                    "en-us": "Alexandria",
                    "ar-eg": "الاسكندريه",
                    "ar-as": "الاسكندريه",
                    "fr-fr": "Alexandrie",
                    "tr-tr": "İskenderiye",
                },
            },
            {
                "name": "Dakahlia",
                "governorate_tel_code": "050",
                "country": 1,
                "translations": {
                    "en-us": "Dakahlia",
                    "ar-eg": "الدقهليه",
                    "ar-as": "الدقهليه",
                    "fr-fr": "Dakalie",
                    "tr-tr": "Dakahlia",
                },
            },
            {
                "name": "Aswan",
                "governorate_tel_code": "097",
                "country": 1,
                "translations": {
                    "en-us": "Aswan",
                    "ar-eg": "أسوان",
                    "ar-as": "أسوان",
                    "fr-fr": "Assouan",
                    "tr-tr": "Aswan",
                },
            },
            {
                "name": "Arish",
                "governorate_tel_code": "068",
                "country": 1,
                "translations": {
                    "en-us": "Arish",
                    "ar-eg": "العريش",
                    "ar-as": "العريش",
                    "fr-fr": "Arish",
                    "tr-tr": "Arish",
                },
            },
            {
                "name": "Beni Suef",
                "governorate_tel_code": "082",
                "country": 1,
                "translations": {
                    "en-us": "Beni Suef",
                    "ar-eg": "بنى سويف",
                    "ar-as": "بنى سويف",
                    "fr-fr": "Beni Souef",
                    "tr-tr": "Beni Suef",
                },
            },
            {
                "name": "Damietta",
                "governorate_tel_code": "057",
                "country": 1,
                "translations": {
                    "en-us": "Damietta",
                    "ar-eg": "دمياط",
                    "ar-as": "دمياط",
                    "fr-fr": "Damiette",
                    "tr-tr": "Damietta",
                },
            },
            {
                "name": "Ismailia",
                "governorate_tel_code": "064",
                "country": 1,
                "translations": {
                    "en-us": "Ismailia",
                    "ar-eg": "اسماعليه",
                    "ar-as": "اسماعليه",
                    "fr-fr": "Ismaïlia",
                    "tr-tr": "Ismailia",
                },
            },
            {
                "name": "Luxor",
                "governorate_tel_code": "095",
                "country": 1,
                "translations": {
                    "en-us": "Luxor",
                    "ar-eg": "الاقصر",
                    "ar-as": "الاقصر",
                    "fr-fr": "Louxor",
                    "tr-tr": "Luxor",
                },
            },
            {
                "name": "Monufia",
                "governorate_tel_code": "048",
                "country": 1,
                "translations": {
                    "en-us": "Monufia",
                    "ar-eg": "منوفيه",
                    "ar-as": "منوفيه",
                    "fr-fr": "Monoufia",
                    "tr-tr": "Monufia",
                },
            },
            {
                "name": "Port Said",
                "governorate_tel_code": "066",
                "country": 1,
                "translations": {
                    "en-us": "Port Said",
                    "ar-eg": "بورسعيد",
                    "ar-as": "بورسعيد",
                    "fr-fr": "Port-Saïd",
                    "tr-tr": "Port Said",
                },
            },
            {
                "name": "Red Sea",
                "governorate_tel_code": "065",
                "country": 1,
                "translations": {
                    "en-us": "Red Sea",
                    "ar-eg": "البحرالاحمر",
                    "ar-as": "البحرالاحمر",
                    "fr-fr": "Mer Rouge",
                    "tr-tr": "Kızıldeniz",
                },
            },
            {
                "name": "Suez",
                "governorate_tel_code": "062",
                "country": 1,
                "translations": {
                    "en-us": "Suez",
                    "ar-eg": "السويس",
                    "ar-as": "السويس",
                    "fr-fr": "Suez",
                    "tr-tr": "Süveyş",
                },
            },
            {
                "name": "El Tour",
                "governorate_tel_code": "069",
                "country": 1,
                "translations": {
                    "en-us": "El Tour",
                    "ar-eg": "الطور",
                    "ar-as": "الطور",
                    "fr-fr": "Le Tour",
                    "tr-tr": "El Turu",
                },
            },
            {
                "name": "10th of Ramadan",
                "governorate_tel_code": "055",
                "country": 1,
                "translations": {
                    "en-us": "10th of Ramadan",
                    "ar-eg": "العاشر من رمضان",
                    "ar-as": "العاشر من رمضان",
                    "fr-fr": "10ème Ramadan",
                    "tr-tr": "10 Ramazan",
                },
            },
            {
                "name": "Asyut",
                "governorate_tel_code": "088",
                "country": 1,
                "translations": {
                    "en-us": "Asyut",
                    "ar-eg": "أسيوط",
                    "ar-as": "أسيوط",
                    "fr-fr": "Assiout",
                    "tr-tr": "Asyut",
                },
            },
            {
                "name": "Damanhur",
                "governorate_tel_code": "04",
                "country": 1,
                "translations": {
                    "en-us": "Damanhur",
                    "ar-eg": "دمنهور",
                    "ar-as": "دمنهور",
                    "fr-fr": "Damanhur",
                    "tr-tr": "Damanhur",
                },
            },
            {
                "name": "Faiyum",
                "governorate_tel_code": "084",
                "country": 1,
                "translations": {
                    "en-us": "Faiyum",
                    "ar-eg": "الفيوم",
                    "ar-as": "الفيوم",
                    "fr-fr": "Fayoum",
                    "tr-tr": "Faiyum",
                },
            },
            {
                "name": "Kafr El Sheikh",
                "governorate_tel_code": "047",
                "country": 1,
                "translations": {
                    "en-us": "Kafr El Sheikh",
                    "ar-eg": "كفرالشيخ",
                    "ar-as": "كفرالشيخ",
                    "fr-fr": "Kafr El Sheikh",
                    "tr-tr": "Kafr El Şeyh",
                },
            },
            {
                "name": "Marsa Matruh",
                "governorate_tel_code": "046",
                "country": 1,
                "translations": {
                    "en-us": "Marsa Matruh",
                    "ar-eg": "مرسى مطروح",
                    "ar-as": "مرسى مطروح",
                    "fr-fr": "Marsa Matrouh",
                    "tr-tr": "Marsa Matruh",
                },
            },
            {
                "name": "Minya",
                "governorate_tel_code": "086",
                "country": 1,
                "translations": {
                    "en-us": "Minya",
                    "ar-eg": "المنيا",
                    "ar-as": "المنيا",
                    "fr-fr": "Minya",
                    "tr-tr": "Minya",
                },
            },
            {
                "name": "New Valley",
                "governorate_tel_code": "092",
                "country": 1,
                "translations": {
                    "en-us": "New Valley",
                    "ar-eg": "الوادى الجديد",
                    "ar-as": "الوادى الجديد",
                    "fr-fr": "Nouvelle Vallée",
                    "tr-tr": "Yeni Vadi",
                },
            },
            {
                "name": "Sohag",
                "governorate_tel_code": "093",
                "country": 1,
                "translations": {
                    "en-us": "Sohag",
                    "ar-eg": "سوهاج",
                    "ar-as": "سوهاج",
                    "fr-fr": "Sohag",
                    "tr-tr": "Sohag",
                },
            },
            {
                "name": "Qena",
                "governorate_tel_code": "096",
                "country": 1,
                "translations": {
                    "en-us": "Qena",
                    "ar-eg": "قنا",
                    "ar-as": "قنا",
                    "fr-fr": "Qéna",
                    "tr-tr": "Qena",
                },
            },
            {
                "name": "Tanta",
                "governorate_tel_code": "040",
                "country": 1,
                "translations": {
                    "en-us": "Tanta",
                    "ar-eg": "طنطا",
                    "ar-as": "طنطا",
                    "fr-fr": "Tanta",
                    "tr-tr": "Tanta",
                },
            },
            {
                "name": "Qalyubia",
                "governorate_tel_code": "013",
                "country": 1,
                "translations": {
                    "en-us": "Qalyubia",
                    "ar-eg": "قليوبيه",
                    "ar-as": "قليوبيه",
                    "fr-fr": "Qalyubia",
                    "tr-tr": "Qalyubia",
                },
            },
            {
                "name": "Isle of France",
                "governorate_tel_code": "1",
                "country": 3,
                "translations": {
                    "en-us": "Isle of France",
                    "ar-eg": "جزيرة فرنسا",
                    "ar-as": "جزيرة فرنسا",
                    "fr-fr": "Île de France",
                    "tr-tr": "Fransa Adası",
                },
            },
            {
                "name": "Emirate of Abu Dhabi",
                "governorate_tel_code": "2",
                "country": 3,
                "translations": {
                    "en-us": "Emirate of Abu Dhabi",
                    "ar-eg": "إمارة أبو ظبي",
                    "ar-as": "إمارة أبو ظبي",
                    "fr-fr": "Emirat d'Abou Dhabi",
                    "tr-tr": "Abu Dabi Emirliği",
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
