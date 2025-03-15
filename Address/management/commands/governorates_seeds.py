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
                    "en-US": "Cairo",
                    "ar-EG": "القاهره",
                    "ar-AS": "القاهره",
                    "fr-FR": "Caire",
                    "tr-TR": "Kahire",
                },
            },
            {
                "name": "Alexandria",
                "governorate_tel_code": "03",
                "country": 1,
                "translations": {
                    "en-US": "Alexandria",
                    "ar-EG": "الاسكندريه",
                    "ar-AS": "الاسكندريه",
                    "fr-FR": "Alexandrie",
                    "tr-TR": "İskenderiye",
                },
            },
            {
                "name": "Dakahlia",
                "governorate_tel_code": "050",
                "country": 1,
                "translations": {
                    "en-US": "Dakahlia",
                    "ar-EG": "الدقهليه",
                    "ar-AS": "الدقهليه",
                    "fr-FR": "Dakalie",
                    "tr-TR": "Dakahlia",
                },
            },
            {
                "name": "Aswan",
                "governorate_tel_code": "097",
                "country": 1,
                "translations": {
                    "en-US": "Aswan",
                    "ar-EG": "أسوان",
                    "ar-AS": "أسوان",
                    "fr-FR": "Assouan",
                    "tr-TR": "Aswan",
                },
            },
            {
                "name": "Arish",
                "governorate_tel_code": "068",
                "country": 1,
                "translations": {
                    "en-US": "Arish",
                    "ar-EG": "العريش",
                    "ar-AS": "العريش",
                    "fr-FR": "Arish",
                    "tr-TR": "Arish",
                },
            },
            {
                "name": "Beni Suef",
                "governorate_tel_code": "082",
                "country": 1,
                "translations": {
                    "en-US": "Beni Suef",
                    "ar-EG": "بنى سويف",
                    "ar-AS": "بنى سويف",
                    "fr-FR": "Beni Souef",
                    "tr-TR": "Beni Suef",
                },
            },
            {
                "name": "Damietta",
                "governorate_tel_code": "057",
                "country": 1,
                "translations": {
                    "en-US": "Damietta",
                    "ar-EG": "دمياط",
                    "ar-AS": "دمياط",
                    "fr-FR": "Damiette",
                    "tr-TR": "Damietta",
                },
            },
            {
                "name": "Ismailia",
                "governorate_tel_code": "064",
                "country": 1,
                "translations": {
                    "en-US": "Ismailia",
                    "ar-EG": "اسماعليه",
                    "ar-AS": "اسماعليه",
                    "fr-FR": "Ismaïlia",
                    "tr-TR": "Ismailia",
                },
            },
            {
                "name": "Luxor",
                "governorate_tel_code": "095",
                "country": 1,
                "translations": {
                    "en-US": "Luxor",
                    "ar-EG": "الاقصر",
                    "ar-AS": "الاقصر",
                    "fr-FR": "Louxor",
                    "tr-TR": "Luxor",
                },
            },
            {
                "name": "Monufia",
                "governorate_tel_code": "048",
                "country": 1,
                "translations": {
                    "en-US": "Monufia",
                    "ar-EG": "منوفيه",
                    "ar-AS": "منوفيه",
                    "fr-FR": "Monoufia",
                    "tr-TR": "Monufia",
                },
            },
            {
                "name": "Port Said",
                "governorate_tel_code": "066",
                "country": 1,
                "translations": {
                    "en-US": "Port Said",
                    "ar-EG": "بورسعيد",
                    "ar-AS": "بورسعيد",
                    "fr-FR": "Port-Saïd",
                    "tr-TR": "Port Said",
                },
            },
            {
                "name": "Red Sea",
                "governorate_tel_code": "065",
                "country": 1,
                "translations": {
                    "en-US": "Red Sea",
                    "ar-EG": "البحرالاحمر",
                    "ar-AS": "البحرالاحمر",
                    "fr-FR": "Mer Rouge",
                    "tr-TR": "Kızıldeniz",
                },
            },
            {
                "name": "Suez",
                "governorate_tel_code": "062",
                "country": 1,
                "translations": {
                    "en-US": "Suez",
                    "ar-EG": "السويس",
                    "ar-AS": "السويس",
                    "fr-FR": "Suez",
                    "tr-TR": "Süveyş",
                },
            },
            {
                "name": "El Tour",
                "governorate_tel_code": "069",
                "country": 1,
                "translations": {
                    "en-US": "El Tour",
                    "ar-EG": "الطور",
                    "ar-AS": "الطور",
                    "fr-FR": "Le Tour",
                    "tr-TR": "El Turu",
                },
            },
            {
                "name": "10th of Ramadan",
                "governorate_tel_code": "055",
                "country": 1,
                "translations": {
                    "en-US": "10th of Ramadan",
                    "ar-EG": "العاشر من رمضان",
                    "ar-AS": "العاشر من رمضان",
                    "fr-FR": "10ème Ramadan",
                    "tr-TR": "10 Ramazan",
                },
            },
            {
                "name": "Asyut",
                "governorate_tel_code": "088",
                "country": 1,
                "translations": {
                    "en-US": "Asyut",
                    "ar-EG": "أسيوط",
                    "ar-AS": "أسيوط",
                    "fr-FR": "Assiout",
                    "tr-TR": "Asyut",
                },
            },
            {
                "name": "Damanhur",
                "governorate_tel_code": "04",
                "country": 1,
                "translations": {
                    "en-US": "Damanhur",
                    "ar-EG": "دمنهور",
                    "ar-AS": "دمنهور",
                    "fr-FR": "Damanhur",
                    "tr-TR": "Damanhur",
                },
            },
            {
                "name": "Faiyum",
                "governorate_tel_code": "084",
                "country": 1,
                "translations": {
                    "en-US": "Faiyum",
                    "ar-EG": "الفيوم",
                    "ar-AS": "الفيوم",
                    "fr-FR": "Fayoum",
                    "tr-TR": "Faiyum",
                },
            },
            {
                "name": "Kafr El Sheikh",
                "governorate_tel_code": "047",
                "country": 1,
                "translations": {
                    "en-US": "Kafr El Sheikh",
                    "ar-EG": "كفرالشيخ",
                    "ar-AS": "كفرالشيخ",
                    "fr-FR": "Kafr El Sheikh",
                    "tr-TR": "Kafr El Şeyh",
                },
            },
            {
                "name": "Marsa Matruh",
                "governorate_tel_code": "046",
                "country": 1,
                "translations": {
                    "en-US": "Marsa Matruh",
                    "ar-EG": "مرسى مطروح",
                    "ar-AS": "مرسى مطروح",
                    "fr-FR": "Marsa Matrouh",
                    "tr-TR": "Marsa Matruh",
                },
            },
            {
                "name": "Minya",
                "governorate_tel_code": "086",
                "country": 1,
                "translations": {
                    "en-US": "Minya",
                    "ar-EG": "المنيا",
                    "ar-AS": "المنيا",
                    "fr-FR": "Minya",
                    "tr-TR": "Minya",
                },
            },
            {
                "name": "New Valley",
                "governorate_tel_code": "092",
                "country": 1,
                "translations": {
                    "en-US": "New Valley",
                    "ar-EG": "الوادى الجديد",
                    "ar-AS": "الوادى الجديد",
                    "fr-FR": "Nouvelle Vallée",
                    "tr-TR": "Yeni Vadi",
                },
            },
            {
                "name": "Sohag",
                "governorate_tel_code": "093",
                "country": 1,
                "translations": {
                    "en-US": "Sohag",
                    "ar-EG": "سوهاج",
                    "ar-AS": "سوهاج",
                    "fr-FR": "Sohag",
                    "tr-TR": "Sohag",
                },
            },
            {
                "name": "Qena",
                "governorate_tel_code": "096",
                "country": 1,
                "translations": {
                    "en-US": "Qena",
                    "ar-EG": "قنا",
                    "ar-AS": "قنا",
                    "fr-FR": "Qéna",
                    "tr-TR": "Qena",
                },
            },
            {
                "name": "Tanta",
                "governorate_tel_code": "040",
                "country": 1,
                "translations": {
                    "en-US": "Tanta",
                    "ar-EG": "طنطا",
                    "ar-AS": "طنطا",
                    "fr-FR": "Tanta",
                    "tr-TR": "Tanta",
                },
            },
            {
                "name": "Qalyubia",
                "governorate_tel_code": "013",
                "country": 1,
                "translations": {
                    "en-US": "Qalyubia",
                    "ar-EG": "قليوبيه",
                    "ar-AS": "قليوبيه",
                    "fr-FR": "Qalyubia",
                    "tr-TR": "Qalyubia",
                },
            },
            {
                "name": "Isle of France",
                "governorate_tel_code": "1",
                "country": 3,
                "translations": {
                    "en-US": "Isle of France",
                    "ar-EG": "جزيرة فرنسا",
                    "ar-AS": "جزيرة فرنسا",
                    "fr-FR": "Île de France",
                    "tr-TR": "Fransa Adası",
                },
            },
            {
                "name": "Emirate of Abu Dhabi",
                "governorate_tel_code": "2",
                "country": 3,
                "translations": {
                    "en-US": "Emirate of Abu Dhabi",
                    "ar-EG": "إمارة أبو ظبي",
                    "ar-AS": "إمارة أبو ظبي",
                    "fr-FR": "Emirat d'Abou Dhabi",
                    "tr-TR": "Abu Dabi Emirliği",
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
