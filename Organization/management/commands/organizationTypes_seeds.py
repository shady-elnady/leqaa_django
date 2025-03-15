from django.core.management.base import BaseCommand

from Organization.models import OrganizationType


class Command(BaseCommand):
    data = "Organization Types"
    help = f"Creates initial {data} model"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        organizationTypes = [
            {
                "name": "Family",
                "translations": {
                    "ar-AS": "اسره ",
                    "ar-EG": "اسره",
                    "en-US": "Family",
                    "fr-FR": "Famille",
                    "tr-TR": "Aile",
                },
            },
        ]

        for organizationType in organizationTypes:
            try:
                OrganizationType.objects.create(
                    name=organizationType["name"],
                    translations=organizationType["translations"],
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully insert {self.data} > {organizationType}"
                    )
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed insert {self.data} > {organizationType} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.WARNING(f"Finish Created initial {self.data}"))
