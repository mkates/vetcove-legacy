# Allow relative imports
from __future__ import absolute_import

# Core Django Imports
from django.http import JsonResponse
from django.views.generic import FormView,TemplateView
from django.core.urlresolvers import reverse

# In-App Imports
from .forms import *
from .models import *



class NewClinicBasics(FormView):
    ''' 
    Form to register new clinics - basic information
    '''
    template_name = 'clinics/new/basics.html'
    form_class = NewClinicBasics
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super(NewClinicBasics, self).get_context_data(**kwargs)
        context['page_newclinicbasics'] = True
        return context


class NewClinicVerify(FormView):
    ''' 
    Form to register new clinics - verification information
    '''
    template_name = 'clinics/new/verification.html'
    form_class = NewClinicVerify
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super(NewClinicVerify, self).get_context_data(**kwargs)
        context['page_newclinicverify'] = True
        return context


class NewClinicTOS(FormView):
    '''
    Form terms of service - terms of service and agreements
    '''
    template_name = 'clinics/new/tos.html'
    success_url = '/'
    form_class = NewClinicTOS

    def get_success_url(self):
    	return reverse("clinics:new_clinic_complete")

    def get_context_data(self, **kwargs):
        context = super(NewClinicTOS, self).get_context_data(**kwargs)
        context['page_newclinictos'] = True
        return context


class NewClinicComplete(TemplateView):
    '''
    Success page after a clinic has completed registration
    '''
    template_name = 'clinics/new/complete.html'

class SalesExempt(FormView):
    '''
    Sales Exemption Form
    '''
    template_name = 'clinics/salesexempt.html'
    success_url = '/'
    form_class = SalesExempt

