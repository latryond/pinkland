
from django import template

register = template.Library()

@register.simple_tag
def discount(value, discount_percent):
    discounted_value = value*(discount_percent/100);
    return discounted_value
