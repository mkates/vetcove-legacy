# Allow relative imports
from __future__ import absolute_import

# Django Apps
from django import forms

# In App Imports
from .models import SupplierLead



# TODO: Work in progress
class SupplierLeadForm(forms.Form):
    ''' 
    Form for a supplier lead
     '''
    class Meta:
        model = SupplierLead

        fields = ['company','interest_listings','interest_community',
        'interest_promotions','interest_direct','product_size']
        labels = {
            'company': "Company",
            'interest_listings': 'Interest in managing product listings',
            'interest_community': 'Interest in answering questions and responding to reviews',
            'interest_promotions': 'Interest in running promotions',
            'product_size':'Number of Products',
        }
        error_messages = {
            'company': {
                'required': "Company Name is Required",
                'max_length':"Short Company Name Please",
            }
        }
        help_texts = {
            'name': {
                'max_length':"Too long",
            }
        }
        layout = {
            'company': 'inline'
        }

