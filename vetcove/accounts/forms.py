# Allow relative imports
from __future__ import absolute_import

# Django Apps
from django import forms
from django.contrib.auth.forms import AuthenticationForm

# In App Imports
from core.form_fields import * # Imports all the custom form field attributes


class LoginForm(AuthenticationForm):

    username = forms.CharField(label="Email", widget=CoreEmailInput())
    password = forms.CharField(label="Password", widget=CorePasswordInput())
    error_messages = {
        'invalid_login': "The email/password you entered is incorrect. Please try again (make sure your caps lock is off)",
    }