from django.contrib import admin
from django.apps import apps

from Config import settings


ALLOW_UNREGISTERAPPS_LIST = []

models = apps.get_models()

for model in models:
    try:
        if model not in ALLOW_UNREGISTERAPPS_LIST:
            admin.site.register(model)
        else:
            admin.site.unregister(model)
    except admin.sites.AlreadyRegistered:
        # print(f"Model {model} already registered")
        pass
    except admin.sites.NotRegistered:
        # print(f"Model {model} already Not registered")
        pass


if apps.is_installed("django.contrib.sites"):
    from django.contrib.sites.models import Site

    try:
        Site.objects.update_or_create(
            id=getattr(settings, "SITE_ID", 1),
            defaults={
                "domain": getattr(settings, "SITE_DOMAIN", "localhost:8000"),
                "name": getattr(settings, "SITE_NAME", "Local Dev Site"),
            },
        )
    except Exception as e:
        print(f"Could not setup default site: {e}")
