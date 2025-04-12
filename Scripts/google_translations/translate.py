import argparse
import polib
from googletrans import Translator
from tqdm import tqdm
import os

# Parse command-line arguments
parser = argparse.ArgumentParser(
    description="Translate .po files using Google Translate"
)
parser.add_argument("-f", "--file", required=True, help="Path to the .po file")
parser.add_argument("-l", "--lang", required=True, help="Target language code")
args = parser.parse_args()

po_file = args.file
language = args.lang

# Load the .po file
po = polib.pofile(po_file)
translator = Translator()

# Translate each message
for entry in tqdm(po, desc="Translating messages"):
    if not entry.msgstr:  # Only translate empty translations
        try:
            entry.msgstr = translator.translate(entry.msgid, dest=language).text
        except Exception as e:
            print(f"\nError translating '{entry.msgid}': {e}")

# Save the translated PO file
translated_filename = f"{os.path.splitext(po_file)[0]}_{language}.po"
po.save(translated_filename)

print(f"\nTranslation completed: {translated_filename}")
