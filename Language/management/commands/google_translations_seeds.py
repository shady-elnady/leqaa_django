import time
import random
from pathlib import Path
from django.core.management.base import BaseCommand
from django.conf import settings
from polib import pofile
from googletrans import Translator


class Command(BaseCommand):
    help = "Generate translated locale files using Google Translate"

    def add_arguments(self, parser):
        parser.add_argument(
            "--source-lang", default="en", help="Source language code (default: en)"
        )
        parser.add_argument(
            "--sleep",
            type=float,
            default=2.0,
            help="Seconds between API calls (default: 2.0)",
        )
        parser.add_argument(
            "--jitter",
            type=float,
            default=0.5,
            help="Random delay variation (default: 0.5)",
        )
        parser.add_argument(
            "--retries",
            type=int,
            default=3,
            help="Max retries per translation (default: 3)",
        )
        parser.add_argument(
            "--overwrite", action="store_true", help="Overwrite existing translations"
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting locale file translation..."))

        # Initialize translator with multiple service URLs
        translator = Translator(
            service_urls=[
                "translate.google.com",
                "translate.google.co.kr",
            ],
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        )

        # Process all regional variants
        for base_lang, variants in settings.REGIONAL_LANGUAGES.items():
            for variant in variants:
                self.process_locale(
                    variant=variant,
                    base_lang=base_lang,
                    translator=translator,
                    source_lang=options["source_lang"],
                    sleep_time=options["sleep"],
                    jitter=options["jitter"],
                    retries=options["retries"],
                    overwrite=options["overwrite"],
                )

        self.stdout.write(self.style.SUCCESS("\nTranslation process completed!"))

    def process_locale(
        self,
        variant,
        base_lang,
        translator,
        source_lang,
        sleep_time,
        jitter,
        retries,
        overwrite,
    ):
        """Process a single locale variant"""
        locale_path = self.get_locale_path(variant)
        if not locale_path.exists():
            self.stdout.write(
                self.style.WARNING(f"Locale directory not found for {variant}")
            )
            return

        po_file = locale_path / "LC_MESSAGES" / "django.po"
        if not po_file.exists():
            self.stdout.write(self.style.WARNING(f"PO file not found: {po_file}"))
            return

        self.stdout.write(f"\nProcessing {variant} ({base_lang})...")

        try:
            po = pofile(str(po_file))
            stats = {"translated": 0, "skipped": 0, "errors": 0}

            for entry in po:
                if not entry.msgid or entry.obsolete:
                    continue

                # Skip if translation exists and not overwriting
                if entry.msgstr and not overwrite:
                    stats["skipped"] += 1
                    continue

                # Translate with retries
                translated = False
                for attempt in range(retries):
                    try:
                        entry.msgstr = self.translate_text(
                            translator,
                            entry.msgid,
                            src=source_lang,
                            dest=base_lang,  # Use base language for API
                            sleep_time=sleep_time,
                            jitter=jitter,
                        )
                        stats["translated"] += 1
                        translated = True
                        break
                    except Exception as e:
                        if attempt == retries - 1:
                            self.stdout.write(
                                self.style.ERROR(
                                    f"Failed to translate after {retries} attempts: {entry.msgid[:50]}..."
                                )
                            )
                            stats["errors"] += 1
                        time.sleep(
                            (sleep_time + random.uniform(0, jitter)) * (attempt + 1)
                        )

            # Save the translated file
            if stats["translated"] > 0:
                backup_path = po_file.with_suffix(".po.bak")
                if po_file.exists():
                    po_file.rename(backup_path)
                po.save(str(po_file))
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Translated {stats['translated']} strings (skipped {stats['skipped']}, errors {stats['errors']}"
                    )
                )
            else:
                self.stdout.write(self.style.WARNING("No new translations made"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error processing {variant}: {str(e)}"))

    def translate_text(self, translator, text, src, dest, sleep_time, jitter):
        """Translate text with rate limiting"""
        time.sleep(sleep_time + random.uniform(0, jitter))
        try:
            return translator.translate(text, src=src, dest=dest).text
        except Exception as e:
            if "429" in str(e):  # Rate limited
                time.sleep(10)  # Extended wait if rate limited
            raise

    def get_locale_path(self, variant):
        """Get the locale directory path for a variant"""
        for locale_path in settings.LOCALE_PATHS:
            path = Path(locale_path) / variant
            if path.exists():
                return path
        return (
            Path(settings.LOCALE_PATHS[0]) / variant
            if settings.LOCALE_PATHS
            else Path(settings.BASE_DIR) / "locale" / variant
        )
