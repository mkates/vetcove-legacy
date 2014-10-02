# Allow relative imports
from __future__ import absolute_import

# Django Apps
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from localflavor.us.us_states import US_STATES

# In App Imports
from core.form_fields import * # Imports all the custom form field attributes

class LoginForm(AuthenticationForm):
    ''' 
    Standard Login Form
    '''
    username = forms.CharField(label="Email", widget=CoreEmailInput())
    password = forms.CharField(label="Password", widget=CorePasswordInput())
    error_messages = {
        'invalid_login': "The email/password you entered is incorrect. Please try again (make sure your caps lock is off)",
    }

class SignUpForm(forms.Form):

    '''
    Sign up form for either user type
    '''
    email = forms.CharField(label="Email", widget=CoreEmailInput())
    password = forms.CharField(label="Password", widget=CorePasswordInput())
    confirm_password = forms.CharField(label="Confirm Password", widget=CoreConfirmPasswordInput())
    GROUP_TYPE_CHOICES = (
        ('','-----------'),
        ('clinic','Veterinarian / Clinic / Hospital'),
        ('supplier','Supplier / Manufacturer / Compounder / Distributor'))
    group_type = forms.ChoiceField(
        label="Type of Vetcove User",
        choices = GROUP_TYPE_CHOICES,
        widget=CoreSelect()
    )
    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        confirmpassword = cleaned_data.get("confirm_password")
        group_type = cleaned_data.get("group_type")
        # Make sure passwords are equal to each other
        if not password or len(password) < 6:
            self.add_error(None,forms.ValidationError("Password must be at least 6 characters"))
        # Make sure password and confirm password are equal
        if password != confirmpassword:
            self.add_error(None,forms.ValidationError("Passwords do not match"))
        # Check that the email is unique 
        if BasicUser.objects.filter(username=email).exists():
            self.add_error(None,forms.ValidationError("Account already exists for {}, please log in instead".format(email)))
        # Check the group type was either clinic or supplier
        if group_type not in ['clinic','supplier']:
            self.add_error(None,forms.ValidationError("Please select the type of Vetcove user"))
        # Return the cleaned data
        return cleaned_data

