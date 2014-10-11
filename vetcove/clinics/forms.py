# Allow relative imports
from __future__ import absolute_import

# Django Apps
from django import forms

# In App Imports
from core.form_fields import * # Custom Form Elements
from clinics.models import Clinic


class NewClinicBasics(forms.ModelForm):

    '''
    The basic clinic details, including meta informatio and address
    '''
    name = forms.CharField(
        label="Clinic Name",
        widget=CoreTextInput(attrs={'placeholder':"Colts Neck Equine"})
    )
    website = forms.CharField(
        label="Website URL",
        widget=CoreTextInput(attrs={'placeholder':"www.cnequine.com"})
    )
    address_one = forms.CharField(
        label="Address Line 1",
        help_text="Street address, P.O. box, company name, c/o",
        widget=CoreTextInput(attrs={'placeholder':"1 Main Street"})
    )
    address_two = forms.CharField(
        label="Address Line 2",
        help_text="Apartment, suite, unit, building, floor, etc.",
        widget=CoreTextInput(attrs={'placeholder':"Unit 6"})
    )
    city = forms.CharField(
        widget=CoreTextInput(attrs={'placeholder':"Colts Neck"})
    )
    state = forms.CharField(
        widget=CoreStateSelect()
    )
    postal_code = forms.CharField(
        widget=CorePostalCodeInput()
    )
    phone_number = forms.CharField(
        widget=CorePhoneNumberInput(),
        help_text="We'll call this number to confirm your account",
    )
    number_vets = forms.IntegerField(
        label = "Number of vets in your practice",
        widget=CorePositiveIntegerInput(attrs={'placeholder':"-"})
    )
    practice_type = forms.ChoiceField(
    	widget= CoreSelect(),
        choices= Clinic._meta.get_field('practice_type').choices
    )


class NewClinicVerify(forms.ModelForm):
    '''
    Verification of the clinic, including required credentials
    '''
    def __init__(self, *args, **kwargs):
        super(NewClinicVerify, self).__init__(*args, **kwargs)
        # Conditionally require the image pending the license submit option
        self.fields['license_image'].required = True

    LICENSE_SUBMIT_CHOICES = (
        ('','-----'),
        ('upload',"I'd like to upload an image now"),
        ('fax',"I'd like to fax in a copy to XXX-XXX-XXXX"),
        ('skip',"I'll skip this for now, but I'll upload one later ")
    )
    # Moved purchaser and position to the verification to avoid confusion
    purchaser = forms.CharField(
        label = "Name of person doing the purchasing",
        widget=CoreTextInput(attrs={'placeholder':"Name of purchaser"})
    )
    position = forms.CharField(
        label = "Position of person doing the purchasing",
        widget=CoreTextInput(attrs={'placeholder':"Position of purchaser"})
    )
    license_submit = forms.ChoiceField(
        widget=CoreSelect(attrs={'data-toggle-name':'license_image','data-toggle-value':'upload'}),
        label="How will you submit your license?",
        choices=LICENSE_SUBMIT_CHOICES
    )
    license_expiration_month = forms.CharField(
        label = 'Exp. Month',
        widget = CoreMonthSelect()
    )
    license_expiration_day = forms.IntegerField(
        label = 'Exp. Day',
        widget=CoreDaySelect()
    )
    license_expiration_year = forms.IntegerField(
        label = 'Exp. Year',
        widget=CoreFutureYearSelect()
    )

    class Meta:
        model = Clinic
        fields = ('first_name','middle_initial','last_name','license_state','license_image',
            'license_no','license_submit')
        labels = {
            "first_name":"Licensed Veterinarian's First Name",
            'license_image':'Upload a copy of your license',
            'purchaser':'Name of person who will be purchasing (if different)'
        }
        widgets = {
            'name': CoreTextInput(attrs={'placeholder':'Name'}),
            'license_state': CoreStateSelect(),
            'license_no': CoreTextInput(attrs={'placeholder':'Veterinary License No.'}),
            'license_image': CoreFileInput(),
        }

    def clean(self):
        # Checks that a license is uploaded if they chose to upload an image
        license_submit = self.cleaned_data['license_submit']
        license_image = self.cleaned_data['license_image']
        if license_submit == 'upload' and not license_image:
            self.add_error(None,forms.ValidationError("Please upload an image of your veterinary license"))
        return self.cleaned_data




class NewClinicTOS(forms.Form):
    '''
    The terms of service that each clinic must agree to before continuing
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

class SalesExempt(forms.Form):
	pass


