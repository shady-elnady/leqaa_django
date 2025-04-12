from django.apps import AppConfig

from App.messages import ModelsMessages


class OrganizationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Organization"
    verbose_name = ModelsMessages.ORGANIZATION
    verbose_name_plural = ModelsMessages.ORGANIZATIONS
