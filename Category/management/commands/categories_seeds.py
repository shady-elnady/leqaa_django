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
                    "en-us": "Agriculture",
                    "ar-as": "الزراعه",
                    "ar-eg": "الزراعه",
                    "fr-fr": "Agriculture",
                    "tr-tr": "Tarım",
                },
            },
            {
                "name": "Law",
                "translations": {
                    "en-us": "Law",
                    "ar-as": "القانون",
                    "ar-eg": "القانون",
                    "fr-fr": "la Loi",
                    "tr-tr": "Huku",
                },
            },
            {
                "name": "Engineering",
                "translations": {
                    "en-us": "Engineering",
                    "ar-as": "الهندسه",
                    "ar-eg": "الهندسه",
                    "fr-fr": "Ingénierie",
                    "tr-tr": "Mühendislik",
                },
            },
            {
                "name": "Sports",
                "translations": {
                    "en-us": "Sports",
                    "ar-as": "الرياضه",
                    "ar-eg": "الرياضه",
                    "fr-fr": "Sportif",
                    "tr-tr": "Spor",
                },
            },
            {
                "name": "Technology",
                "translations": {
                    "en-us": "Technology",
                    "ar-as": "التكنولوجيا",
                    "ar-eg": "التكنولوجيا",
                    "fr-fr": "Technologie",
                    "tr-tr": "Teknoloji",
                },
            },
            {
                "name": "Entrepreneurship",
                "translations": {
                    "en-us": "Entrepreneurship",
                    "ar-as": "ريادة أعمال",
                    "ar-eg": "ريادة أعمال",
                    "fr-fr": "Entrepreneuriat",
                    "tr-tr": "Girişimcilik",
                },
            },
            {
                "name": "Science",
                "translations": {
                    "en-us": "Science",
                    "ar-as": "العلوم",
                    "ar-eg": "العلوم",
                    "fr-fr": "les Sciences",
                    "tr-tr": "Bilim",
                },
            },
            {
                "name": "Health",
                "translations": {
                    "en-us": "Health",
                    "ar-as": "الصحه",
                    "ar-eg": "الصحه",
                    "fr-fr": "Santé",
                    "tr-tr": "Sağlık",
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
