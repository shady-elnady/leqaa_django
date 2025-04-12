# templatetags/regional_lang.py
from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def get_regional_languages(current_lang):
    base_lang = current_lang.split("_")[0]
    variants = settings.LANGUAGE_VARIANTS.get(base_lang, [current_lang])
    return [(code, name) for code, name in settings.LANGUAGES if code in variants]


"""
    {% load regional_lang %}

    {% get_regional_languages LANGUAGE_CODE as regional_langs %}
    <ul>
    {% for code, name in regional_langs %}
        <li class="{% if code == LANGUAGE_CODE %}active{% endif %}">
        <a href="?lang={{ code }}">{{ name }}</a>
        </li>
    {% endfor %}
    </ul>
"""
