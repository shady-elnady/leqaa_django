from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from Language.models import Language, Locale
from Language.utils.locales_loader import fetch_supported_locales


@receiver(post_save, sender=Language)
@receiver(post_delete, sender=Language)
@receiver(post_save, sender=Locale)
@receiver(post_delete, sender=Locale)
def update_locales_on_change(sender, instance, **kwargs):
    """Refresh locales cache when language/locale models change"""
    fetch_supported_locales()
