# Allow relative imports
from __future__ import absolute_import

# Django Apps
from django import forms
from django.contrib.auth.forms import AuthenticationForm

# In App Imports
#from .models import 

class EmailAuthenticationForm(AuthenticationForm):

    error_messages = {
        'invalid_login': "Please enter a correct email and password",
        'inactive': "This account is inactive.",
    }