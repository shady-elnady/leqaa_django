from django import template
from django.conf import settings
from django.urls import reverse
import requests

from Language.utils.locales_loader import (
    get_cached_app_locales,
    fetch_supported_locales,
)

register = template.Library()

# # Old Code
# @register.simple_tag(takes_context=True)
# def get_my_app_locales(context):
#     request = context["request"]
#     if not settings.APP_LOCALES["is_set"]:
#         try:
#             # Build URL using reverse() for better maintainability
#             relative_url = reverse("app-locale-list")  # Use your URL name here
#             absolute_url = request.build_absolute_uri(relative_url)
#             response = requests.get(absolute_url, timeout=5)  # Added timeout
#             if response.status_code == 200:
#                 settings.APP_LOCALES["is_set"] = True
#                 data = response.json()
#                 settings.APP_LOCALES["data"] = data["results"]
#             else:
#                 # Log the error properly in production
#                 print(f"Failed to retrieve data: {response.status_code}")
#                 return []  # Return empty list as fallback

#         except requests.exceptions.RequestException as e:
#             # Handle connection errors, timeouts, etc.
#             print(f"Error fetching app locales: {str(e)}")
#             return []  # Return empty list as fallback
#     return settings.APP_LOCALES.get("data", [])


@register.simple_tag(takes_context=True)
def get_my_app_locales(context):
    print(100 * "@")
    print(f"get_cached_app_locales() = {get_cached_app_locales()}")
    print(100 * "@")
    if settings.APP_LOCALES["is_set"]:
        return get_cached_app_locales()
    else:
        return fetch_supported_locales()
