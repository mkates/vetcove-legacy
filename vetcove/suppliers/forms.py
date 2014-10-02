# Allow relative imports
from __future__ import absolute_import

# Django Apps
from django import forms

# In App Imports
from core.form_fields import * # Custom Form Elements
from .models import Supplier
from accounts.models import Address

class NewSupplierBasics(forms.Form):

    '''
    The basic clinic details, including meta informatio and address
    '''
    company_name = forms.CharField(
        label="Company Name",
        widget=CoreTextInput(attrs={'placeholder':"A&G Pharmaceuticals"})
    )
    category = forms.ChoiceField(
        label="Supplier type",
        widget = CoreSelect(),
        choices =Supplier._meta.get_field('company_type').choices
    )
    contact_name = forms.CharField(
        label="Primary Contact Name",
        widget=CoreTextInput(attrs={'placeholder':"Name"})
    )
    contact_position = forms.CharField(
        label="Primary Contact Position",
        widget=CoreTextInput(attrs={'placeholder':"Position"})
    )
    contact_email = forms.CharField(
        label="Email",
        widget=CoreEmailInput()
    )
    phone_number = forms.CharField(
        widget=CorePhoneNumberInput(),
        help_text="We'll call this number to confirm your account",
    )
    sell_rx = forms.BooleanField(
        widget=CoreCheckboxInput(),
        label = 'Do you plan on selling prescription items through Vetcove?',
        required=False
    )


class NewSupplierContact(forms.ModelForm):
    '''
    New Supplier Address
    '''
    class Meta:
        model = Address
        fields = ('address_one','address_two','city','state','postalcode')
        labels = {
            'postalcode':'Postal Code',
        }
        widgets = {
            'address_one':CoreTextInput(attrs={'placeholder':'Address Line 1'}),
            'address_two':CoreTextInput(attrs={'placeholder':'Address Line 2'}),
            'city': CoreTextInput(attrs={'placeholder':'City Name'}),
            'state': CoreStateSelect(),
            'postalcode': CorePostalCodeInput()
        }
        help_text = {
            "address_one":"Street address, P.O. box, company name, c/o",
            'address_two':'Apartment, suite, unit, building, floor, etc.',
        }


class NewSupplierTOS(forms.Form):
    '''
    The terms of service that each supplier must agree to
    '''
    term_one = forms.BooleanField(
        widget= CoreCheckboxInput(),
        label="I acknowledge that I am, or am acting on behalf, of a valid veterinarian and have the right to purchase said products"
    )
    term_two = forms.BooleanField(
        widget= CoreCheckboxInput(),
        label="I acknowledge that I am, or am acting on behalf, of a valid veterinarian and have the right to purchase said products"
    )
    term_three = forms.BooleanField(
        widget= CoreCheckboxInput(),
        label="I acknowledge that I am, or am acting on behalf, of a valid veterinarian and have the right to purchase said products"
    )
    term_four = forms.BooleanField(
        widget= CoreCheckboxInput(),
        label="I acknowledge that I am, or am acting on behalf, of a valid veterinarian and have the right to purchase said products"
    )


