from __future__ import absolute_import

# Standard Library Imports

# Core Django Imports
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
# Third Party App Imports

# In-App Imports


def test(request):
	return render_to_response('test.html',{'page_dashboard':True},context_instance=RequestContext(request))