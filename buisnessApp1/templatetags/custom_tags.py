from django import template
from django.db.models import Max



register = template.Library()

@register.filter
def increment(value):
    return value + 1

@register.filter
def decrement(value):
    return value - 1

@register.filter
def max(queryset):
    # Get the maximum id length
    a = 1
    len_list = [len(str(obj.id)) for obj in queryset]
    max_id_length = max(len_list)
    return max_id_length



