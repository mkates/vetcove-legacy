# Allow relative imports
from __future__ import absolute_import

# Standard Library Imports

# Core Django Imports
from django.http import HttpResponseRedirect,HttpResponse, JsonResponse
from django.views.generic import TemplateView, RedirectView, FormView, View
from django.contrib.auth import login
from django.core.urlresolvers import reverse

# Third Party App Imports

# In-App Imports
from .forms import *
from .models import *


#######################################################################

class SignIn(FormView):
    ''' 
    Form to sign a user in
    '''
    template_name = 'accounts/signin.html'
    form_class = LoginForm
    success_url = '/home'

    def form_valid(self,form):
        '''Form is valid, so log the user in'''
        login(self.request,form.get_user())
        super(SignIn,super).form_valid(form)


class SignUp(FormView):
    ''' 
    Clinic Sign Up Form
    '''
    template_name = 'accounts/signup.html'
    form_class = SignUpForm
    success_url = "/"

    def form_valid(self,form):
        '''
        Form is valid, so send the user to the appropriate new user form
        '''
        # Create a new basic user
        basicuser = BasicUser(
            username=form['email'].value(),
            email=form['email'].value(),
            password=form['password'].value())
        basicuser.save()

        # Create a new group 
        group = Group(
            group_type=form['group_type'].value(),
            administrator = basicuser)
        group.save()

        # Link the group and the basicuser
        basicuser.group = group
        basicuser.save()

        # Redirect to the appropriate sign up page
        group_type = form['group_type'].value()
        if group_type == 'clinic':
            return HttpResponseRedirect(reverse("accounts:newclinic"))
        else:
            return HttpResponseRedirect(reverse("accounts:newsupplier"))



class NewSupplier(FormView):
    ''' 
    Form to register new clinics
    '''
    template_name = 'accounts/newclinic.html'
    form_class = SignUpForm
    success_url = "/"





class Password(TemplateView):
    ''' 
    Requesting a New Password
    '''
    template_name = 'accounts/newpassword_form.html'
