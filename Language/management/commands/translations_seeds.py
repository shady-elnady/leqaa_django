from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
from os.path import join, exists
from os import listdir, makedirs


class Command(BaseCommand):
    help = "Translations Messages Files"

    # Function to simulate translation (replace with actual translation in real use)
    def simulate_translation(self, text):
        return f"[FR] {text}"

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f"Start {self.help}"))

        locales_dir: str = (
            settings.settings.LOCALE_PATHS[0]
            if len(settings.settings.LOCALE_PATHS) > 0
            else join(settings.BASE_DIR, "locale")
        )

        for locale_dir in listdir(locales_dir):
            origin_file = join(locales_dir, locale_dir, "LC_MESSAGES", "django.po")
            # Read the original .po file
            with open(origin_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
                # Translate each msgid to msgstr
                translated_lines = []
                in_msgid = False
                msgid_lines = []
                for line in lines:
                    if line.startswith("msgid "):
                        in_msgid = True
                        msgid_lines = [line]
                    elif in_msgid and line.startswith('"'):
                        msgid_lines.append(line)
                    elif in_msgid:
                        # End of msgid block
                        in_msgid = False
                        msgid_text = "".join(line.strip()[1:-1] for line in msgid_lines)
                        msgstr_translation = self.simulate_translation(msgid_text)
                        translated_lines.extend(msgid_lines)
                        translated_lines.append(f'msgstr "{msgstr_translation}"\n')
                        translated_lines.append(line)
                    else:
                        translated_lines.append(line)

                    # Save translated file
                    translated_file_path = origin_file = join(
                        locales_dir,
                        locale_dir,
                        "LC_MESSAGES",
                        "django_fr_FR_translated.po",
                    )
                    try:
                        with open(translated_file_path, "w", encoding="utf-8") as f:
                            f.writelines(translated_lines)
                        self.stdout.write(
                            self.style.SUCCESS(
                                f"Successfully Translate >>  {locale_dir}"
                            )
                        )
                    except Exception as e:
                        self.stdout.write(
                            self.style.ERROR(f"Failed Translate >>  {locale_dir}")
                        )
        self.stdout.write(self.style.WARNING(f"Finish Created initial {self.data}"))
