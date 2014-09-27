from django.template import Library

from core.misc import convertIntegerDollarsToFloatDollars

register = Library()

@register.filter
def dollars(value):
	
	'''Converts an integer into a dollar amount'''

	return convertIntegerDollarsToFloatDollars(value)

@register.filter
def widgetType(value):
	'''
	This tag returns the class of the widget (i.e.:TextInput or Select)
	'''
	return value.field.widget.__class__.__name__

@register.filter
def equals(value,arg):
	return value==arg