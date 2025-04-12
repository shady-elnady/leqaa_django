from django.contrib import admin
from django.apps import apps


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
