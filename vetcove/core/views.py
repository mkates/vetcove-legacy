# Allow relative imports
from __future__ import absolute_import

# Standard Library Imports

# Core Django Imports
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.contrib.auth.views import redirect_to_login

# Third Party App Imports

# In-App Imports


class Test(TemplateView):
	template_name = 'test.html'

def test(request):
	return render_to_response('test.html',{'page_dashboard':True},context_instance=RequestContext(request))


###########################################
###### Permissions Mixins #################
###########################################

class ClinicRequiredMixin(object):
	'''Checks if the user is a member of a group and ensures
	that the group is of the type clinic. Otherwise, redirects
	to the login page'''

	def dispatch(self, request, *args, **kwargs):
		# Check if they are logged in, they belong to a group, and the group is a clinic
		user = request.user
		isClinic = (user.is_authenticated() and user.group and user.group.group_type !='clinic')
		if not isClinic:
			return redirect_to_login()
		return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class SupplierRequiredMixin(object):
	'''Checks if the user is a member of a group and ensures
	that the group is of the type supplier. Otherwise, redirects
	to the login page'''

	def dispatch(self, request, *args, **kwargs):
		# Check if they are logged in, they belong to a group, and the group is a supplier
		user = request.user
		isSupplier = (user.is_authenticated() and user.group and user.group.group_type !='supplier')
		if not isSupplier:
			return redirect_to_login()
		return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

class AnyGroupRequiredMixin(object):
	'''Checks if the user is a member of any group or sends 
	them back to the login page'''

	def dispatch(self, request, *args, **kwargs):
		# Check if they are logged in, they belong to a group, and the group is a supplier
		user = request.user
		isGroup = (user.is_authenticated() and user.group)
		if not isGroup:
			return redirect_to_login()
		return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
