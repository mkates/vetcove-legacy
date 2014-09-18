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

# Third Party App Imports

# In-App Imports


class Test(TemplateView):
    template_name = 'test.html'

def test(request):
    return render_to_response('test.html',{'page_dashboard':True},context_instance=RequestContext(request))


###########################################
###### Permissions Mixins #################
###########################################

class ClinicRequiredMixin(object):
    '''Checks if the user is a member of a group and ensures
    that the group is of the type clinic. Otherwise, redirects
    to the login page'''

    def dispatch(self, request, *args, **kwargs):
        # Check if they are logged in, they belong to a group, and the group is a clinic
        user = request.user
        isClinic = (user.is_authenticated() and user.group and user.group.group_type !='clinic')
        if not isClinic:
            return redirect_to_login()
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class SupplierRequiredMixin(object):
    '''Checks if the user is a member of a group and ensures
    that the group is of the type supplier. Otherwise, redirects
    to the login page'''

    def dispatch(self, request, *args, **kwargs):
        # Check if they are logged in, they belong to a group, and the group is a supplier
        user = request.user
        isSupplier = (user.is_authenticated() and user.group and user.group.group_type =='supplier')
        if not isSupplier:
            return redirect_to_login()
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

class AnyGroupRequiredMixin(object):
    '''Checks if the user is a member of any group or sends 
    them back to the login page'''

    def dispatch(self, request, *args, **kwargs):
        # Check if they are logged in, they belong to a group
        user = request.user
        isGroup = (user.is_authenticated() and user.group)
        if not isGroup:
            return redirect_to_login()
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)



###########################################
###### Ajax Response Mixin ################
###########################################

class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    To use: set a variable ajax=True 
    """
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.ajax:
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.ajax:
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data,status=201)
        else:
            return response
