from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
from os.path import join, exists
from os import makedirs

from App.tools import get_model_name_from_class
from Organization.models import Organization, OrganizationType, University


class Command(BaseCommand):
    data = "Organizations"
    help = f"Creates initial {data} model"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        if not exists(
            join(settings.MEDIA_ROOT, "images", get_model_name_from_class(Organization))
        ):
            makedirs(
                join(
                    settings.MEDIA_ROOT,
                    "images",
                    get_model_name_from_class(Organization),
                )
            )

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
                "name": "اسره الثقافه",
                "university": 1,
                "affiliated_to": None,
                # "translations": {
                #     "ar-as": "اسره الثقافه",
                #     "ar-eg": "اسره الثقافه",
                #     "en-us": "Family of Culture",
                #     "fr-fr": "Famille culturelle",
                #     "tr-tr": "Kültür Ailesi",
                # },
            },
            {
                "organization_type": 1,
                "name": "أسره النور",
                "university": 1,
                "affiliated_to": None,
                # "translations": {
                #     "ar-as": "أسره النور",
                #     "ar-eg": "أسره النور",
                #     "en-us": "The light Family",
                #     "fr-fr": "La lumière l'a capturé",
                #     "tr-tr": "Işık ailesi",
                # },
            },
            {
                "organization_type": 1,
                "name": "مركز الإبداع الرقمي",
                "university": 1,
                "affiliated_to": None,
                # "translations": {
                #     "ar-as": "مركز الإبداع الرقمي",
                #     "ar-eg": "مركز الإبداع الرقمي",
                # },
            },
        ]
        organization_id = 1
        for organization in organizations:
            try:
                Organization.objects.create(
                    organization_type=OrganizationType.objects.get(
                        pk=organization["organization_type"]
                    ),
                    name=organization["name"],
                    image=join(
                        "images",
                        get_model_name_from_class(Organization),
                        f"{organization_id}.png",
                    ),
                    university=University.objects.get(pk=organization["university"]),
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully insert {self.data} > {organization}"
                    )
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed insert {self.data} > {organization} , \n \t Error is: \t \t{e}"
                    )
                )
            organization_id = organization_id + 1
        self.stdout.write(self.style.WARNING(f"Finish Created initial {self.data}"))
