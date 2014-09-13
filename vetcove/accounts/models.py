# Standard Library Imports
import uuid, os, random, string

# Django Imports
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

# Third Party App Imports
from imagekit.processors import ResizeToFill, ResizeToFit
from imagekit.models import ProcessedImageField
from model_utils.models import TimeStampedModel


####### Paths for Logos  ##################
def create_group_path(instance, filename):
	ext = filename.split('.')[-1]
	filename = "%s.%s" % (str(uuid.uuid4()), ext)
	return os.path.join('grouplogos', filename)

############################################
####### The Basic User Object ##############
############################################
class BasicUser(AbstractUser,TimeStampedModel):
	group = models.ForeignKey('Group',blank=True,null=True)
	
	def __str__(self):
		return self.username

############################################
####### The Group Object ###################
############################################
class Group(TimeStampedModel):

	'''Groups are the main unit on VetCove. Each user belongs to a group, which can be a supplier,
	clinic, or even a client. Majority of foreign references refer directly to the group object'''

	### General Information ###
	name = models.CharField(max_length=60,blank=True,null=True)
	administrator = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='group_administrator')
	address = models.ForeignKey('Address',related_name="main_address",null=True,blank=True)
	phonenumber = models.BigIntegerField(max_length=15)
	website = models.CharField(max_length=60,blank=True,null=True)
	image = ProcessedImageField(upload_to=create_group_path,format='JPEG',options={'quality': 60},null=True,blank=True)
	
	### Referral Information ###
	referrer_id = models.CharField(max_length=10) # The ID used to give out referrals
	referrer_user = models.ForeignKey('self',null=True,blank=True) # Did another clinic refer them to join?, let's store it

	### Payments ###
	balanceduri = models.CharField(max_length=255,blank=True,null=True)
	#payment_method = models.ForeignKey('payment.Payment',null=True,blank=True,related_name='basic_payment_method')
	#payout_method = models.ForeignKey('payment.Payment',null=True,blank=True,related_name='basic_payout_method')
	
	# Current credit balance
	credits = models.BigIntegerField(max_length=12,default=0) # Everyone can earn credits!

	# Are they verified by us?, this is manually toggled in the staff application
	verified = models.BooleanField(default=False)

	# References to clinic and supplier objects
	# Clean() ensures that at either clinic or supplier is not null
	GROUP_TYPES = (('clinic','clinic'),('supplier','supplier'))
	group_type = models.CharField(max_length=10,choices=GROUP_TYPES) 
	clinic = models.OneToOneField('clinics.Clinic',null=True,blank=True)
	supplier = models.OneToOneField('suppliers.Supplier',null=True,blank=True)
	
	def group(self):
		return self.supplier if self.group_type == 'supplier' else self.clinic

	def __str__(self):
		return self.name


############################################
############ Addresses #####################
############################################

class Address(models.Model):
	group = models.ForeignKey(Group,null=True,blank=True,related_name="address_group")
	name = models.CharField(max_length=50) # full name
	address_one = models.CharField(max_length=100) # street address,p.o. box, company name c/o
	address_two = models.CharField(max_length=100,blank=True,null=True) # apartment, suite, unit, building,floor,etc.
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100) # Can be state/province/or region
	country = models.CharField(max_length=50, default="United States")
	postalcode = models.CharField(max_length=10) # Can be zipcode or postal code, i.e. in Canada its A2E4D9
	telephone = models.BigIntegerField(max_length=15,blank=True,null=True) # Optional phone number

	def __str__(self):
		address_two_string = str(self.address_two)+"\n" if self.address_two else ""
		return str(self.name)+"\n"+str(self.address_one)+"\n"+address_two_string+str(self.city)+", "+str(self.state)+" "+str(self.postalcode)



