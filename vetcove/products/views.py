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
from django.http import JsonResponse

from .utils import *


class Test(TemplateView):
    template_name = 'products/test.html'

    def get_context_data(self, **kwargs):
        context = super(Test, self).get_context_data(**kwargs)
        #context['image'] = Image.objects.all()[0]
        
        return context

class Product(TemplateView):
    template_name = 'products/product.html'

    def get_context_data(self, **kwargs):
        context = super(Product, self).get_context_data(**kwargs)
        return context

