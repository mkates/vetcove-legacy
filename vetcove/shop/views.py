# Core Django Imports
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.contrib.auth.views import redirect_to_login
from django.http import JsonResponse

# Third Party App Imports

# In-App Imports


class OrderHistory(TemplateView):
    template_name = 'shop/orderhistory.html'

