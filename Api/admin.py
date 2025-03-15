from django.contrib import admin
from django.apps import apps
from django.utils.translation import gettext_lazy as _


models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
