from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
from os.path import exists, join
from os import makedirs


class Command(BaseCommand):
    help = "Generate translation files for all regional language variants"

    def add_arguments(self, parser):
        parser.add_argument(
            "--ignore",
            action="append",
            default=["venv/*", "node_modules/*", ".git/*"],
            help="Patterns to ignore when scanning for translations",
        )

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.MIGRATE_HEADING("Starting translation file generation")
        )

        if not hasattr(settings, "REGIONAL_LANGUAGES"):
            self.stdout.write(
                self.style.ERROR("REGIONAL_LANGUAGES not defined in settings")
            )
            return

        # Create locale directory if needed
        locale_path = (
            settings.LOCALE_PATHS[0]
            if settings.LOCALE_PATHS
            else join(settings.BASE_DIR, "locale")
        )
        makedirs(locale_path, exist_ok=True)

        # Process all variants
        success_count = 0
        for base_lang, variants in settings.REGIONAL_LANGUAGES.items():
            for variant in variants:
                try:
                    call_command(
                        "makemessages",
                        locale=[variant],
                        ignore=options["ignore"],
                        no_location=True,  # Cleaner PO files
                        no_obsolete=True,  # Remove obsolete strings
                        verbosity=options["verbosity"],
                    )
                    success_count += 1
                    self.stdout.write(
                        self.style.SUCCESS(f" ✓ Processing Locale for {variant}")
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.NOTICE(
                            f" ✗ Processing Locale for {variant},\n \t Error: {str(e)}"
                        )
                    )

        # Summary
        self.stdout.write(
            "\n"
            + self.style.MIGRATE_HEADING(
                f"Completed: {success_count} language files generated"
            )
        )
