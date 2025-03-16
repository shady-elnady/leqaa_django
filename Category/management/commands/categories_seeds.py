from django.core.management.base import BaseCommand
from django.conf import settings
from os.path import join, exists
from os import makedirs

from Category.models import Category


class Command(BaseCommand):
    data = "Categories"
    help = f"Creates initial {data} model"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        IMAGES_ROOT = join(settings.MEDIA_ROOT, "images")

        categories_images_directory = join(IMAGES_ROOT, "Categories")
        if not exists(categories_images_directory):
            makedirs(categories_images_directory)

        categories = [
            {
                "name": "Agriculture",
                "translations": {
                    "en-US": "Agriculture",
                    "ar-AS": "الزراعه",
                    "ar-EG": "الزراعه",
                    "fr-FR": "Agriculture",
                    "tr-TR": "Tarım",
                },
            },
            {
                "name": "Law",
                "translations": {
                    "en-US": "Law",
                    "ar-AS": "القانون",
                    "ar-EG": "القانون",
                    "fr-FR": "la Loi",
                    "tr-TR": "Huku",
                },
            },
            {
                "name": "Engineering",
                "translations": {
                    "en-US": "Engineering",
                    "ar-AS": "الهندسه",
                    "ar-EG": "الهندسه",
                    "fr-FR": "Ingénierie",
                    "tr-TR": "Mühendislik",
                },
            },
            {
                "name": "Sports",
                "translations": {
                    "en-US": "Sports",
                    "ar-AS": "الرياضه",
                    "ar-EG": "الرياضه",
                    "fr-FR": "Sportif",
                    "tr-TR": "Spor",
                },
            },
            {
                "name": "Technology",
                "translations": {
                    "en-US": "Technology",
                    "ar-AS": "التكنولوجيا",
                    "ar-EG": "التكنولوجيا",
                    "fr-FR": "Technologie",
                    "tr-TR": "Teknoloji",
                },
            },
            {
                "name": "Entrepreneurship",
                "translations": {
                    "en-US": "Entrepreneurship",
                    "ar-AS": "ريادة أعمال",
                    "ar-EG": "ريادة أعمال",
                    "fr-FR": "Entrepreneuriat",
                    "tr-TR": "Girişimcilik",
                },
            },
            {
                "name": "Science",
                "translations": {
                    "en-US": "Science",
                    "ar-AS": "العلوم",
                    "ar-EG": "العلوم",
                    "fr-FR": "les Sciences",
                    "tr-TR": "Bilim",
                },
            },
            {
                "name": "Health",
                "translations": {
                    "en-US": "Health",
                    "ar-AS": "الصحه",
                    "ar-EG": "الصحه",
                    "fr-FR": "Santé",
                    "tr-TR": "Sağlık",
                },
            },
        ]
        category_id = 1
        for category in categories:
            try:
                Category.objects.create(
                    name=category["name"],
                    image=join(categories_images_directory, f"{category_id}.png"),
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
