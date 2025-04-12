# management/commands/compile_regional_messages.py
from django.core.management.commands.compilemessages import (
    Command as CompileMessagesCommand,
)

from Config import settings


class Command(CompileMessagesCommand):
    help = "Compiles regional message files"

    def handle(self, *args, **options):
        # Process all regional variants
        for base_lang, variants in settings.REGIONAL_LANGUAGES.items():
            for variant in variants:
                options["locale"] = variant
                super().handle(*args, **options)
