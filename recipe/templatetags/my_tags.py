from django import template
from recipe.models import *

register=template.Library()

@register.simple_tag()
def get_cat():
	return Category.objects.filter(active=True).order_by('name')

@register.simple_tag()
def get_tag():
	return Tag.objects.filter(active=True).order_by('name')