# Standard Library Imports

# Django Imports
from django.db import models

# Third Party App Imports
from model_utils.models import TimeStampedModel

# In App Imports
from core.models import ListField


class SupplierLead(TimeStampedModel):
	company = models.CharField(max_length=100)
	COMPANY_TYPE_CHOICES = (
		('manufacturer','Manufacturer'),
		('distributor','Distributor'),
		('compounding pharmacy','Compounding Pharmacy'),
		('reseller','Reseller')
	)
	company_type = models.CharField(choices=COMPANY_TYPE_CHOICES,max_length=25)
	COMPANY_SIZE_CHOICES = (
		('< 5','< 5 employees'),
		('5-10','5-9 employees'),
		('10-20','10-20 employees'),
		('21-50','21-50 employees'),
		('51-100','51-100 employees'),
		('101-500','101-500 employees'),
		('500+','500+ employees'),
	)
	company_size = models.CharField(choices = COMPANY_SIZE_CHOICES, max_length=100)

	sell_pharmaceuticals = models.BooleanField(default=False)
	sell_equipment = models.BooleanField(default=False)
	sell_diagnostics = models.BooleanField(default=False)
	sell_biologics = models.BooleanField(default=False)
	sell_food = models.BooleanField(default=False)
	sell_pestmanagement = models.BooleanField(default=False)
	sell_other = models.CharField(max_length=200,null=True,blank=True)
	
	name = models.CharField(max_length=100)
	position = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	phonenumber = models.CharField(max_length=100,null=True,blank=True)
	managing_presence = models.BooleanField(default=None)
	authorized = models.BooleanField(default=None)

	### For the manufacturers only ###
	sellmethod_distributor = models.BooleanField(default=None)
	sellmethod_phone = models.BooleanField(default=False)
	sellmethod_website = models.BooleanField(default=False)
	sellmethod_other = models.CharField(max_length=200,null=True,blank=True)

	### Vetcove Features ###
	feature_newcustomers = models.BooleanField(default=False)
	feature_directship = models.BooleanField(default=False)

	howdidyouhear = models.CharField(max_length=200)
	additional = models.TextField()



class ClinicLead(TimeStampedModel):
	clinic_name = models.CharField(max_length=100)
	clinic_city = models.CharField(max_length=100)
	clinic_state = models.CharField(max_length=100)
	PRACTICE_TYPE_CHOICES = (
		('Small Animal Predominant','< 5 employees'),
		('Large Animal Predominant','5-9 employees'),
		('Mixed','Mixed')
	)
	practice_type = models.CharField(max_length=200,choices=PRACTICE_TYPE_CHOICES)
	number_of_licensed_veterinarians = models.IntegerField(max_length=3)
	total_employees = models.IntegerField(max_length=3)
	clinic_website = models.CharField(max_length=30,null=True,blank=True)
	your_name = models.CharField(max_length=100)
	your_position = models.CharField(max_length=100,null=True,blank=True)
	your_email = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=15,null=True,blank=True)
	placing_orders = models.BooleanField(default=False)
	authorized_decisions = models.BooleanField(default=False)

	### Features Booleans
	feature_singlesource = models.BooleanField(default=False)
	feature_productresearch = models.BooleanField(default=False)
	feature_connectwithmanufacturers = models.BooleanField(default=False)
	feature_rebatetracking = models.BooleanField(default=False)
	feature_consolidateinvoices = models.BooleanField(default=False)
	feature_supportandreturns = models.BooleanField(default=False)
	feature_exclusivediscounts = models.BooleanField(default=False)
	feature_purchaseanalytics = models.BooleanField(default=False)
	feature_rewards = models.BooleanField(default=False)

	BETA_USER_CHOICES = (
		(1,'Yes: Please save me a spot in the beta'),
		(0,'Undecided: Just keep me in the loop for now'))
	beta_user = models.CharField(default=0,max_length=2,choices=BETA_USER_CHOICES)

	HEAR_ABOUT_US_CHOICES = (
		('conference','Conference'),
		('personal referral','Personal Referral'),
		('website','Website'),
		('email','Email'),
		('other','Other'))
	hear_about_us = models.CharField(max_length=20,choices=HEAR_ABOUT_US_CHOICES)
	hear_about_us_other = models.CharField(max_length=200,null=True,blank=True)






