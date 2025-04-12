#!/bin/bash

python manage.py makemessages --all


python manage.py makemessages -l ar  # For Arabic
python manage.py makemessages -l fr  # For French
python manage.py makemessages -l de  # For German
python manage.py makemessages -l tr  # For Turekish

# Compil after Translations
python manage.py compilemessages


# Finally, run the following command in the terminal. Make sure the translation file and the script are in the same folder:
python translate.py -f <filename> -l <language_code>
python ./Scripts/google_translations/translate.py -f django.po -l "tr"
