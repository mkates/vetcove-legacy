# Allow relative imports
from __future__ import absolute_import

# Standard Library Imports

# Core Django Imports
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import TemplateView, RedirectView, FormView
from django.contrib.auth import login

# Third Party App Imports

# In-App Imports
from .forms import LoginForm


#######################################################################


class SignIn(FormView):
	''' 
	Form to sign a user in
	'''
	template_name = 'accounts/signin.html'
	form_class = LoginForm
	success_url = '/home'

	def form_valid(self,form):
		'''
		Form is valid, so log the user in
		'''
		login(self.request,form.get_user())
		super(SignIn,super).form_valid(form)


class Password(TemplateView):
	template_name = 'accounts/newpassword_form.html'
