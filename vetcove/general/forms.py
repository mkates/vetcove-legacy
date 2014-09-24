# Allow relative imports
from __future__ import absolute_import

# Django Apps
from django import forms

# In App Imports
from core.form_fields import *
from .models import SupplierLead



# TODO: Work in progress
class SupplierLeadForm(forms.ModelForm):
    ''' 
    Form for a supplier lead
     '''
    class Meta:
        model = SupplierLead
        widgets = {
            'company': TextInput(),
            'sell_pharmaceuticals': CheckboxInput(),
            'sell_equipment': CheckboxInput(),
            'sell_diagnostics': CheckboxInput(),
            'sell_biologics': CheckboxInput(),
            'sell_food': CheckboxInput(),
            'sell_pestmanagement': CheckboxInput(),
            'sell_other':TextInput(),
            # 'sell_equipment': Checkbox(attrs={}),
            # 'sell_equipment': Checkbox(attrs={}),
            # 'sell_equipment': Checkbox(attrs={}),
            # 'sell_equipment': Checkbox(attrs={}),
            # 'sell_equipment': Checkbox(attrs={}),
        }



    # company = models.CharField(max_length=100)
    # COMPANY_TYPE_CHOICES = (
    #     ('manufacturer','Manufacturer'),
    #     ('distributor','Distributor'),
    #     ('compounding pharmacy','Compounding Pharmacy'),
    #     ('reseller','Reseller')
    # )
    # company_type = models.CharField(choices=COMPANY_TYPE_CHOICES,max_length=25)
    # COMPANY_SIZE_CHOICES = (
    #     ('< 5','< 5 employees'),
    #     ('5-10','5-9 employees'),
    #     ('10-20','10-20 employees'),
    #     ('21-50','21-50 employees'),
    #     ('51-100','51-100 employees'),
    #     ('101-500','101-500 employees'),
    #     ('500+','500+ employees'),
    # )
    # company_size = models.CharField(choices = COMPANY_SIZE_CHOICES, max_length=100)

    # sell_pharmaceuticals = models.BooleanField(default=False)
    # sell_equipment = models.BooleanField(default=False)
    # sell_diagnostics = models.BooleanField(default=False)
    # sell_biologics = models.BooleanField(default=False)
    # sell_food = models.BooleanField(default=False)
    # sell_pestmanagement = models.BooleanField(default=False)
    # sell_other = models.CharField(max_length=200,null=True,blank=True)
    
    # name = models.CharField(max_length=100)
    # position = models.CharField(max_length=100)
    # email = models.CharField(max_length=100)
    # phonenumber = models.CharField(max_length=100,null=True,blank=True)
    # managing_presence = models.BooleanField(default=None)
    # authorized = models.BooleanField(default=None)

    # ### For the manufacturers only ###
    # sellmethod_distributor = models.BooleanField(default=None)
    # sellmethod_phone = models.BooleanField(default=False)
    # sellmethod_website = models.BooleanField(default=False)
    # sellmethod_other = models.CharField(max_length=200,null=True,blank=True)

    # ### Vetcove Features ###
    # feature_newcustomers = models.BooleanField(default=False)
    # feature_directship = models.BooleanField(default=False)

    # howdidyouhear = models.CharField(max_length=200)
    # additional = models.TextField()