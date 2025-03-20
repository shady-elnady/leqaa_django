from django.core.management.base import BaseCommand

from Organization.models import OrganizationType


class Command(BaseCommand):
    data = "Organization Types"
    help = f"Creates initial {data} model"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        organization_types = [
            {
                "name": "Family",
                "translations": {
                    "ar-AS": "اسره",
                    "ar-EG": "اسره",
                    "en-US": "Family",
                    "fr-FR": "Famille",
                    "tr-TR": "Aile",
                },
            },
            {
                "name": "Educational Center",
                "translations": {
                    "ar-AS": "سنتر تعليمى",
                    "ar-EG": "سنتر تعليمى",
                    "en-US": "Educational Center",
                    "fr-FR": "Centre éducatif",
                    "tr-TR": "Eğitim Merkezi",
                },
            },
        ]

        for organization_type in organization_types:
            try:
                OrganizationType.objects.create(
                    name=organization_type["name"],
                    translations=organization_type["translations"],
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully insert {self.data} > {organization_type}"
                    )
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed insert {self.data} > {organization_type} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING(f"Finish Created initial {self.data}"))
