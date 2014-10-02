# Allow relative imports
from __future__ import absolute_import

# Core Django Imports
from django.http import JsonResponse
from django.views.generic import FormView,TemplateView
from django.core.urlresolvers import reverse

# In-App Imports
from .forms import *
from .models import *



class NewSupplierBasics(FormView):
    ''' 
    Form to register new suppliers - basic information
    '''
    template_name = 'suppliers/new/basics.html'
    form_class = NewSupplierBasics
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super(NewSupplierBasics, self).get_context_data(**kwargs)
        context['page_newsupplierbasics'] = True
        return context


class NewSupplierContact(FormView):
    ''' 
    Form to register new suppliers - contact information
    '''
    template_name = 'suppliers/new/contact.html'
    form_class = NewSupplierContact
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super(NewSupplierContact, self).get_context_data(**kwargs)
        context['page_newsuppliercontact'] = True
        return context


class NewSupplierTOS(FormView):
    '''
    Form terms of service - terms of service and agreements
    '''
    template_name = 'suppliers/new/tos.html'
    success_url = '/'
    form_class = NewSupplierTOS

    def get_success_url(self):
    	return reverse("suppliers:new_supplier_complete")

    def get_context_data(self, **kwargs):
        context = super(NewSupplierTOS, self).get_context_data(**kwargs)
        context['page_newsuppliertos'] = True
        return context


class NewSupplierComplete(TemplateView):
    '''
    Success page after a clinic has completed registration
    '''
    template_name = 'suppliers/new/complete.html'

