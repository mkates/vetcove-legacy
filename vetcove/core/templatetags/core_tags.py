from django.template import Library

from core.misc import convertIntegerDollarsToFloatDollars

register = Library()

@register.filter
def dollars(value):
	
	'''Converts an integer into a dollar amount'''

	return convertIntegerDollarsToFloatDollars(value)