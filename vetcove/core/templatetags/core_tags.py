from django.template import Library

from core.misc import convertIntegerDollarsToFloatDollars

register = Library()

@register.filter
def dollars(value):
	
	'''Converts an integer into a dollar amount'''

	return convertIntegerDollarsToFloatDollars(value)

@register.filter
def widgetType(field):
	'''
	This tag returns the data-type attribute of the widget
	'''
	attrs = field.field.widget.attrs
	return attrs['data-type'] if 'data-type' in attrs else 'text'

@register.filter
def equals(value,arg):
	return value==arg

@register.filter
def get_range( value ):
  return range( value )

@register.filter
def get_reverse_range( value ):
  return range(value,0,-1)