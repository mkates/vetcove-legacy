# Allow relative imports
from __future__ import absolute_import

# Django Apps
from django import forms

# In App Imports
from core.form_fields import *
from .models import SupplierLead, ClinicLead


class SupplierLeadForm(forms.ModelForm):
    ''' 
    Form for a supplier lead
    '''
    class Meta:
        model = SupplierLead
        fields = "__all__"
        labels = {
            'feature_sales' : "Boosting sales with online promotions",
            'feature_support' : "Providing online support and responding to clinic questions and reviews",
            'feature_analytics' : "Accessing seller analytics (from both selling direct and through distribution)",
            'feature_invoicing' : "Automating order processing, clinic verification, and invoicing (when selling direct)",
            'feature_webpresence' : "Building a larger and richer web presence for your products",
            'sell_method':'Current selling channel',
            'managing_presence' : "Will you personally be managing your company's presence on Vetcove?",
            'authorized' : 'Are you authorized to make decisions on behalf of your company about joining VetCove?',
            'phonenumber': 'Phone Number',
            'howdidyouhear':'How did you hear about us?',
            'next_steps': 'Your Next Steps',
            'selldirect':'Does your company plan to accept orders on Vetcove and ship directly to customers?'
        }
        widgets = {
            'company': forms.TextInput(attrs={'placeholder':'Company Name'}),
            'name': forms.TextInput(attrs={'placeholder':'Your Full Name'}),
            'position' : forms.TextInput(attrs={'placeholder':'Your Position'}),
            'email' : CoreEmailInput(),
            'phonenumber' : CorePhoneNumberInput(),
        }


class ClinicLeadForm(forms.ModelForm):
    ''' 
    Form for a clinic lead
    '''
    class Meta:
        model = ClinicLead
        fields = "__all__"
        labels = {
            'number_of_licensed_veterinarians':'Licensed Veterinarians',
            'placing_orders':'Will you be the one placing orders on Vetcove?',
            'authorized' : 'Are you authorized to make purchase decisions on behalf of your clinic?',
            'phonenumber': 'Phone Number',
            'howdidyouhear':'How did you hear about us?',
            'beta_user': 'I would like to be part of the beta launch and be among the first clinics to use Vetcove'
        }
        widgets = {
            'clinic_name': forms.TextInput(attrs={'placeholder':'Clinic Name'}),
            'zipcode': forms.TextInput(attrs={'placeholder':'xxxxx'}),
            'state': CoreStateSelect(),
            'your_name': forms.TextInput(attrs={'placeholder':'Dr. John Doe'}),
            'your_position': forms.TextInput(attrs={'placeholder':'Vet / Practice Owner'}),
            'your_email': CoreEmailInput(),
            'phone_number': CorePhoneNumberInput(attrs={'data-required':'False'}),
            'clinic_website':forms.TextInput(attrs={'placeholder':'www.example.com'}),
            'number_of_licensed_veterinarians':CorePositiveIntegerInput(attrs={'placeholder':0}),
            'total_employees':CorePositiveIntegerInput(attrs={'placeholder':0}),
        }



