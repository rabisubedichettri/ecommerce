# product/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def subtract(value, arg):
    return value - int(arg)