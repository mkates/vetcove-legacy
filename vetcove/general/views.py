# Allow relative imports
from __future__ import absolute_import

# Standard Library Imports

# Core Django Imports
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.views import redirect_to_login

# Third Party App Imports

# In-App Imports


class Index(TemplateView):
	template_name = 'general/index.html'

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
	'''Redirect the root company to the about page'''

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

class FAQ(TemplateView):
	template_name = 'general/faq.html'

############################################
###### Explore Pages #######################
############################################

class Features(TemplateView):
	template_name = 'general/features.html'

class Suppliers(TemplateView):
	template_name = 'general/suppliers.html'

class Lead(TemplateView):
	template_name = 'general/lead.html'











