# Allow relative imports
from __future__ import absolute_import

# Django Apps

# In App Imports
#import floppyforms as forms
from django import forms
#from .models import 

###### Email Input ############
class EmailInput(forms.TextInput):
     def __init__(self, attrs=None):
        default_attrs = {
            'type':'email',
            'data-type':'email',
            'data-invalid': "Invalid Email Address",
            'data-required':True,
            'placeholder': "Email Address",
            'class':'form-control'
        }
        if attrs:
            for key,value in attrs.items():
                default_attrs[key] = value
        super(EmailInput, self).__init__(default_attrs)

###### Email Input ############
class PasswordInput(forms.PasswordInput):
     def __init__(self, attrs=None):
        default_attrs = {
            'type':'password',
            'data-type':'password',
            'data-invalid': "Must be 8 at least 8 characters",
            'data-required':True,
            'placeholder': "Password",
            'class':'form-control password'
        }
        if attrs:
            for key,value in attrs.items():
                default_attrs[key] = value
        super(PasswordInput, self).__init__(default_attrs)

class ConfirmPasswordInput(forms.PasswordInput):
     def __init__(self, attrs=None):
        default_attrs = {
            'type':'password',
            'data-type':'confirmpassword',
            'data-invalid': "Passwords do not match",
            'data-required':True,
            'placeholder': "Confirm Password",
            'class':'form-control confirmpassword'
        }
        if attrs:
            for key,value in attrs.items():
                default_attrs[key] = value
        super(ConfirmPasswordInput, self).__init__(default_attrs)


class TestForm(forms.Form):
    email = forms.CharField(widget=EmailInput())
    password = forms.CharField(widget=PasswordInput())
    confirmpassword = forms.CharField(widget=ConfirmPasswordInput(),label="Confirm Password")


