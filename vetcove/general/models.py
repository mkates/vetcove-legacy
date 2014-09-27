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

	### Vetcove Features
	feature_sales = models.BooleanField(default=False)
	feature_support = models.BooleanField(default=False)
	feature_analytics = models.BooleanField(default=False)
	feature_invoicing = models.BooleanField(default=False)
	feature_webpresence = models.BooleanField(default=False)

	### Personal Information ###
	name = models.CharField(max_length=100)
	position = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	phonenumber = models.CharField(max_length=100,null=True,blank=True)

	### Selling Methods ###
	SELL_METHOD_CHOICES = (
		('exclusive_distribution','Exclusively through distribution'),
		('predominant_distribution','Predominantly through distribution'),
		('mixed','Mixed between distribution and direct to vets'),
		('predominant_direct','Predominantly direct to vets'),
		('exclusive_direct','Exclusively direct to vets'))
	sell_method = models.CharField(choices=SELL_METHOD_CHOICES,max_length=30)

	### Yes / No Questions ###
	selldirect = models.BooleanField(default=False)
	managing_presence = models.BooleanField(default=None)
	authorized = models.BooleanField(default=None)

	NEXT_STEPS_CHOICES = (
		('betauser',"Beta User: We'd like first access to Vetcove as a beta user"),
		('confirmed','Confirmed: We Plan to begin using Vetcove once the site is live'),
		('undecided','Undecided: Speak with us to learn more between now and launch day'))
	next_steps = models.CharField(max_length=100,choices=NEXT_STEPS_CHOICES)
	HOW_DID_YOU_HEAR_CHOICES = (
		('conference','Conference'),
		('personal_referral','Personal Referral'),
		('google','Google'),
		('emailmarketing','Email Marketing'))
	howdidyouhear = models.CharField(max_length=200,choices=HOW_DID_YOU_HEAR_CHOICES,blank=True,null=True)


class ClinicLead(TimeStampedModel):
	clinic_name = models.CharField(max_length=100)
	zipcode = models.CharField(max_length=5)
	state = models.CharField(max_length=30)
	PRACTICE_TYPE_CHOICES = (
		('small_animal_exclusive','Small Animal Exclusive'),
		('small_animal_predominant','Small Animal Predominant'),
		('large animal predominant','Large Animal Predominant'),
		('large_animal_exclusive','Large Animal Exclusive'),
		('equine_exclusive','Equine Exclusive'),
		('equine_predominant','Equine Predominant'),
		('other','Other'))
	practice_type = models.CharField(max_length=50,choices=PRACTICE_TYPE_CHOICES)
	number_of_licensed_veterinarians = models.IntegerField(max_length=3)
	total_employees = models.IntegerField(max_length=3)
	clinic_website = models.CharField(max_length=30,null=True,blank=True)
	your_name = models.CharField(max_length=100)
	your_position = models.CharField(max_length=100,null=True,blank=True)
	your_email = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=25,null=True,blank=True)
	placing_orders = models.BooleanField(default=False)
	authorized = models.BooleanField(default=False)

	### Vetcove Features
	feature_sales = models.BooleanField(default=False)
	feature_support = models.BooleanField(default=False)
	feature_analytics = models.BooleanField(default=False)
	feature_invoicing = models.BooleanField(default=False)
	feature_webpresence = models.BooleanField(default=False)

	### Beta User
	beta_user = models.BooleanField(default=False)

	HEAR_ABOUT_US_CHOICES = (
		('conference','Conference'),
		('personal referral','Personal Referral'),
		('website','Website'),
		('email','Email'),
		('other','Other'))
	howdidyouhear = models.CharField(max_length=20,choices=HEAR_ABOUT_US_CHOICES)






