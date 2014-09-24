# Allow relative imports
from __future__ import absolute_import

# Django Apps
from django import forms

# In App Imports
from core.form_fields import * # Imports all the custom form field attributes

#from .models import 

class TestForm(forms.Form):
    company = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Company Name','class':'form-control'}))
    email = forms.CharField(widget=EmailInput())
    password = forms.CharField(widget=PasswordInput())
    confirmpassword = forms.CharField(widget=ConfirmPasswordInput(),label="Confirm Password")
    choices = (('','Select a color. . .'),('red','red'),('blue','blue'))
    color = forms.ChoiceField(widget=forms.CheckboxSelectMultiple,choices=choices)
    file = forms.FileField(widget=forms.ClearableFileInput,required=False)
