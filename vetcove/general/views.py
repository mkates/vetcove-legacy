# Allow relative imports
from __future__ import absolute_import

# Standard Library Imports

# Core Django Imports
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import TemplateView, RedirectView, View, CreateView
from django.contrib.auth.views import redirect_to_login
from django.core.urlresolvers import reverse

# Third Party App Imports

# In-App Imports
from .forms import SupplierLeadForm
from core.views import AjaxableResponseMixin

######################################################################


class Index(TemplateView):
	template_name = 'general/index.html'

	def get_context_data(self, **kwargs):
		context = super(Index, self).get_context_data(**kwargs)
		context['index'] = True
		return context

############################################
###### Company Pages #######################
############################################

class About(TemplateView):
	template_name = 'general/company/about.html'

	def get_context_data(self, **kwargs):
		context = super(About, self).get_context_data(**kwargs)
		context['about'] = True
		return context

class Careers(TemplateView):
	template_name = 'general/company/careers.html'

	def get_context_data(self, **kwargs):
		context = super(Careers, self).get_context_data(**kwargs)
		context['careers'] = True
		return context

class PressKit(TemplateView):
	template_name = 'general/company/presskit.html'

	def get_context_data(self, **kwargs):
		context = super(PressKit, self).get_context_data(**kwargs)
		context['presskit'] = True
		return context

class Feedback(TemplateView):
	template_name = 'general/company/feedback.html'

	def get_context_data(self, **kwargs):
		context = super(Feedback, self).get_context_data(**kwargs)
		context['feedback'] = True
		return context


class Company(RedirectView):
	'''
	Redirect the root company to the about page
	'''
	url = '/company/about'

############################################
###### Legal Pages #########################
############################################

class GeneralPolicy(TemplateView):
	template_name = 'general/legal/generalpolicy.html'

	def get_context_data(self, **kwargs):
		context = super(GeneralPolicy, self).get_context_data(**kwargs)
		context['generalpolicy'] = True
		return context

class PrivacyPolicy(TemplateView):
	template_name = 'general/legal/privacypolicy.html'

	def get_context_data(self, **kwargs):
		context = super(PrivacyPolicy, self).get_context_data(**kwargs)
		context['privacypolicy'] = True
		return context

class TermsOfService(TemplateView):
	template_name = 'general/legal/termsofservice.html'

	def get_context_data(self, **kwargs):
		context = super(TermsOfService, self).get_context_data(**kwargs)
		context['termsofservice'] = True
		return context

class SellerAgreement(TemplateView):
	template_name = 'general/legal/selleragreement.html'

	def get_context_data(self, **kwargs):
		context = super(SellerAgreement, self).get_context_data(**kwargs)
		context['selleragreement'] = True
		return context

############################################
###### Support Pages #######################
############################################

class Support(TemplateView):
	template_name = 'general/support.html'

	def get_context_data(self, **kwargs):
		context = super(Support, self).get_context_data(**kwargs)
		context['support'] = True
		return context


class FAQ(RedirectView):

	def get_redirect_url(self):
		return reverse("general:support")


############################################
###### Explore Pages #######################
############################################

class Features(TemplateView):
	template_name = 'general/features.html'

	def get_context_data(self, **kwargs):
		context = super(Features, self).get_context_data(**kwargs)
		context['features'] = True
		return context

class Suppliers(TemplateView):
	template_name = 'general/suppliers.html'

	def get_context_data(self, **kwargs):
		context = super(Suppliers, self).get_context_data(**kwargs)
		context['suppliers'] = True
		return context

class Dashboard(TemplateView):
	template_name = 'general/dashboard.html'

	def get_context_data(self, **kwargs):
		context = super(Dashboard, self).get_context_data(**kwargs)
		context['dashboard'] = True
		return context

class Lead(AjaxableResponseMixin,CreateView):
	'''
	Supplier Lead Form
	'''
	form_class = SupplierLeadForm
	template_name = 'general/lead.html'
	ajax = True
	success_url = '/' # Required for create View








