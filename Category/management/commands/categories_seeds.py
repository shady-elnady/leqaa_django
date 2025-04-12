from django.core.management.base import BaseCommand
from django.conf import settings
from os.path import join, exists
from os import makedirs

from App.tools import get_model_name_from_class
from Category.models import Category


class Command(BaseCommand):
    data = "Categories"
    help = f"Creates initial {data} model"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        if not exists(
            join(settings.MEDIA_ROOT, "images", get_model_name_from_class(Category))
        ):
            makedirs(
                join(
                    settings.MEDIA_ROOT,
                    "images",
                    get_model_name_from_class(Category),
                )
            )
        categories = [
            {
                "name": "Agriculture",
                "translations": {
                    "en_US": "Agriculture",
                    "ar_AS": "الزراعه",
                    "ar_EG": "الزراعه",
                    "fr_FR": "Agriculture",
                    "tr_TR": "Tarım",
                },
            },
            {
                "name": "Law",
                "translations": {
                    "en_US": "Law",
                    "ar_AS": "القانون",
                    "ar_EG": "القانون",
                    "fr_FR": "la Loi",
                    "tr_TR": "Huku",
                },
            },
            {
                "name": "Engineering",
                "translations": {
                    "en_US": "Engineering",
                    "ar_AS": "الهندسه",
                    "ar_EG": "الهندسه",
                    "fr_FR": "Ingénierie",
                    "tr_TR": "Mühendislik",
                },
            },
            {
                "name": "Sports",
                "translations": {
                    "en_US": "Sports",
                    "ar_AS": "الرياضه",
                    "ar_EG": "الرياضه",
                    "fr_FR": "Sportif",
                    "tr_TR": "Spor",
                },
            },
            {
                "name": "Technology",
                "translations": {
                    "en_US": "Technology",
                    "ar_AS": "التكنولوجيا",
                    "ar_EG": "التكنولوجيا",
                    "fr_FR": "Technologie",
                    "tr_TR": "Teknoloji",
                },
            },
            {
                "name": "Entrepreneurship",
                "translations": {
                    "en_US": "Entrepreneurship",
                    "ar_AS": "ريادة أعمال",
                    "ar_EG": "ريادة أعمال",
                    "fr_FR": "Entrepreneuriat",
                    "tr_TR": "Girişimcilik",
                },
            },
            {
                "name": "Science",
                "translations": {
                    "en_US": "Science",
                    "ar_AS": "العلوم",
                    "ar_EG": "العلوم",
                    "fr_FR": "les Sciences",
                    "tr_TR": "Bilim",
                },
            },
            {
                "name": "Health",
                "translations": {
                    "en_US": "Health",
                    "ar_AS": "الصحه",
                    "ar_EG": "الصحه",
                    "fr_FR": "Santé",
                    "tr_TR": "Sağlık",
                },
            },
        ]
        category_id = 1
        for category in categories:
            try:
                Category.objects.create(
                    name=category["name"],
                    image=join(
                        "images",
                        get_model_name_from_class(Category),
                        f"{category_id}.png",
                    ),
                    translations=category["translations"],
                )
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully insert {self.data} > {category}")
                )
                category_id = category_id + 1
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed insert {self.data} > {category} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING(f"Finish Created initial {self.data}"))
