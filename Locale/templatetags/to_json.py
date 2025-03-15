import json
from django import template
# from django.template.defaulttags import register

register = template.Library()

@register.filter(name="to_json")
def to_json(value):
    return json.loads(value)