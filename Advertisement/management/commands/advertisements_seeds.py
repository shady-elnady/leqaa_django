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
                "name": "Medicine",
                # "image": "images/Categories/1.png",
                "translations": {
                    "en-US": "Medicine",
                    "ar-AS": "الطب",
                    "ar-EG": "الطب",
                    "fr-FR": "Médecine",
                    "tr-TR": "Tıp",
                },
            },
            {
                "name": "Science",
                # "image": "images/Categories/2.png",
                "translations": {
                    "en-US": "Science",
                    "ar-AS": "العلوم",
                    "ar-EG": "العلوم",
                    "fr-FR": "les Sciences",
                    "tr-TR": "Bilim",
                },
            },
            {
                "name": "Engineering",
                # "image": "images/Categories/3.png",
                "translations": {
                    "en-US": "Engineering",
                    "ar-AS": "الهندسه",
                    "ar-EG": "الهندسه",
                    "fr-FR": "Ingénierie",
                    "tr-TR": "Mühendislik",
                },
            },
            {
                "name": "Culture & Arts",
                # "image": "images/Categories/4.png",
                "translations": {
                    "en-US": "Culture & Arts",
                    "ar-AS": "الثقافه والفنون",
                    "ar-EG": "الثقافه والفنون",
                    "fr-FR": "Culture et Arts",
                    "tr-TR": "Kültür ve Sanat",
                },
            },
            {
                "name": "Technology",
                # "image": "images/Categories/5.png",
                "translations": {
                    "en-US": "Technology",
                    "ar-AS": "التكنولوجيا",
                    "ar-EG": "التكنولوجيا",
                    "fr-FR": "Technologie",
                    "tr-TR": "Teknoloji",
                },
            },
            {
                "name": "Agriculture",
                # "image": "images/Categories/6.png",
                "translations": {
                    "en-US": "Agriculture",
                    "ar-AS": "الزراعه",
                    "ar-EG": "الزراعه",
                    "fr-FR": "Agriculture",
                    "tr-TR": "Tarım",
                },
            },
            {
                "name": "Sports",
                # "image": "images/Categories/7.png",
                "translations": {
                    "en-US": "Sports",
                    "ar-AS": "الرياضه",
                    "ar-EG": "الرياضه",
                    "fr-FR": "Sportif",
                    "tr-TR": "Spor",
                },
            },
            {
                "name": "Law",
                # "image": "images/Categories/8.png",
                "translations": {
                    "en-US": "Law",
                    "ar-AS": "القانون",
                    "ar-EG": "القانون",
                    "fr-FR": "la Loi",
                    "tr-TR": "Huku",
                },
            },
        ]
        id = 1
        for category in categories:
            try:
                Category.objects.create(
                    name=category["name"],
                    image=join(categories_images_directory, f"{id}.png"),
                    translations=category["translations"],
                )
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully insert {self.data} > {category}")
                )
                id = id + 1
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed insert {self.data} > {category} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING(f"Finish Created initial {self.data}"))
