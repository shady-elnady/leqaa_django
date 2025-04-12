import os
from django.core.management.base import BaseCommand
from django.conf import settings
from polib import pofile
from translate import Translator  # Install: pip install translate


class Command(BaseCommand):
    help = "Automatically translate .po files for all languages in LOCALE_PATHS"

    def handle(self, *args, **options):
        if not hasattr(settings, "LOCALE_PATHS") or not settings.LOCALE_PATHS:
            self.stdout.write(self.style.ERROR("LOCALE_PATHS not defined in settings."))
            return

        for locale_path in settings.LOCALE_PATHS:
            if not os.path.exists(locale_path):
                self.stdout.write(
                    self.style.WARNING(f"Locale path {locale_path} does not exist.")
                )
                continue

            # Process each .po file in the locale directory
            for root, _, files in os.walk(locale_path):
                for file in files:
                    if file.endswith(".po"):
                        source_po_path = os.path.join(root, file)
                        self.stdout.write(f"Processing: {source_po_path}")

                        source_po = pofile(source_po_path)
                        source_lang = source_po.metadata.get(
                            "Language", "en"
                        )  # Default source = English

                        # Skip if no translatable strings
                        if not source_po.translated_entries():
                            self.stdout.write(
                                f"Skipping (no translations needed): {source_po_path}"
                            )
                            continue

                        # Translate to all target languages (from settings.LANGUAGES)
                        for lang_code, _ in settings.LANGUAGES:
                            if lang_code == source_lang:
                                continue  # Skip same language

                            target_dir = os.path.join(
                                locale_path, lang_code, "LC_MESSAGES"
                            )
                            os.makedirs(target_dir, exist_ok=True)
                            target_po_path = os.path.join(target_dir, file)

                            # Skip if target file already exists
                            if os.path.exists(target_po_path):
                                self.stdout.write(
                                    f"Skipping existing: {target_po_path}"
                                )
                                continue

                            # Initialize translator
                            translator = Translator(
                                to_lang=lang_code, from_lang=source_lang
                            )

                            # Create new PO file (copy metadata from source)
                            target_po = pofile(source_po_path)
                            target_po.metadata["Language"] = lang_code

                            # Translate each entry
                            for entry in target_po:
                                if (
                                    not entry.msgstr
                                ):  # Only translate untranslated strings
                                    try:
                                        translated_text = translator.translate(
                                            entry.msgid
                                        )
                                        entry.msgstr = translated_text
                                    except Exception as e:
                                        self.stdout.write(
                                            self.style.ERROR(
                                                f'Error translating "{entry.msgid}": {e}'
                                            )
                                        )
                                        continue

                            # Save translated .po file
                            target_po.save(target_po_path)
                            self.stdout.write(
                                self.style.SUCCESS(
                                    f"Translated to {lang_code}: {target_po_path}"
                                )
                            )

        self.stdout.write(self.style.SUCCESS("Translation completed!"))
