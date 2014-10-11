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


class Review(TemplateView):
    template_name = 'reviews/review_page.html'

    def get_context_data(self, **kwargs):
        context = super(Review, self).get_context_data(**kwargs)
        return context

class WriteReview(TemplateView):
    template_name = 'reviews/review_write.html'

    def get_context_data(self, **kwargs):
        context = super(WriteReview, self).get_context_data(**kwargs)
        return context