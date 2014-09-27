from django.conf import settings # import the settings file

def static_variables(request):
	'''
	Add any settings variables we need on every page here 
	'''

	return {'STATIC_DEBUG': settings.STATIC_DEBUG}