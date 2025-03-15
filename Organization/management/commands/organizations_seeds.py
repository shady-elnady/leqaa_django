from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
from os.path import join, exists
from os import makedirs

from Organization.models import Organization, OrganizationType, University


class Command(BaseCommand):
    data = "Organizations"
    help = f"Creates initial {data} model"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        IMAGES_ROOT = join(settings.MEDIA_ROOT, "images")

        Organizations_images_directory = join(IMAGES_ROOT, "Organizations")
        if not exists(Organizations_images_directory):
            makedirs(Organizations_images_directory)

        commands = [
            "organizationTypes_seeds",
            "universities_seeds",
            "colleges_seeds",
        ]

        for command in commands:
            try:
                call_command(command)
                self.stdout.write(self.style.SUCCESS(f"Successfully {command}"))
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"{command} Failed  \n \t \t Error is: {e}")
                )

        #######################################################################

        organizations = [
            {
                "organization_type": 1,
                "name": "Family of Culture",
                # "logo": join(Organizations_images_directory, f"{id}.png"),
                "university": 1,
                "affiliated_to": None,
                "translations": {
                    "ar-AS": "اسره الثقافه",
                    "ar-EG": "اسره الثقافه",
                    "en-US": "Family of Culture",
                    "fr-FR": "Famille culturelle",
                    "tr-TR": "Kültür Ailesi",
                },
            },
            {
                "organization_type": 1,
                "name": "The light Family",
                # "logo": "Images/Organizations/2.png",
                "university": 1,
                "affiliated_to": None,
                "translations": {
                    "ar-AS": "أسره النور",
                    "ar-EG": "أسره النور",
                    "en-US": "The light Family",
                    "fr-FR": "La lumière l'a capturé",
                    "tr-TR": "Işık ailesi",
                },
            },
        ]
        id = 1
        for organization in organizations:
            try:
                Organization.objects.create(
                    organization_type=OrganizationType.objects.get(
                        pk=organization["organization_type"]
                    ),
                    name=organization["name"],
                    logo=join(Organizations_images_directory, f"{id}.png"),
                    university=University.objects.get(pk=organization["university"]),
                    # affiliated_to=organization["affiliated_to"],
                    translations=organization["translations"],
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully insert {self.data} > {organization}"
                    )
                )
                id = id + 1
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed insert {self.data} > {organization} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING(f"Finish Created initial {self.data}"))
