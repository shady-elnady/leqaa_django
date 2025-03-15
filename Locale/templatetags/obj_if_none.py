from django import template
# from django.template.defaulttags import register

register = template.Library()

@register.filter(name="obj_if_none")
def obj_if_none(value):
    if value is None :
        return dict()
    else:
        return value
