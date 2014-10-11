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

class Cart(TemplateView):
    template_name = 'shop/cart.html'


################################################
######## Checkout Experience ###################
################################################


class CheckoutShipping(TemplateView):

    template_name = 'shop/checkout/shipping.html'

    def get_context_data(self, **kwargs):
        context = super(CheckoutShipping, self).get_context_data(**kwargs)
        context['page_checkout_shipping'] = True
        context['page_checkout_title'] = "Shipping and Delivery Options"
        return context

class CheckoutBilling(TemplateView):

    template_name = 'shop/checkout/billing.html'

    def get_context_data(self, **kwargs):
        context = super(CheckoutBilling, self).get_context_data(**kwargs)
        context['page_checkout_billing'] = True
        context['page_checkout_title'] = "Payment & Billing"
        return context

class CheckoutReview(TemplateView):

    template_name = 'shop/checkout/review.html'

    def get_context_data(self, **kwargs):
        context = super(CheckoutReview, self).get_context_data(**kwargs)
        context['page_checkout_review'] = True
        context['page_checkout_title'] = "Review and CompletePurchase"
        return context