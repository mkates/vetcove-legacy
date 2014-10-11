# Standard Library Imports
import uuid, os, random, string

# Django Imports
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

# Third Party App Imports
from imagekit.processors import ResizeToFill, ResizeToFit
from imagekit.models import ProcessedImageField
from model_utils.models import TimeStampedModel

from core.models import SlugModel


############################################
####### The Basic User Object ##############
############################################
class BasicUser(AbstractUser,TimeStampedModel):
    '''
    The User Model. On creation, the username (which is forced to be an email)
    is also set as the User's email address 
    '''
    group = models.ForeignKey('Group',blank=True,null=True)

    def __str__(self):
        return self.username

############################################
####### The Group Object ###################
############################################
def create_logo_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join('logo', filename)


class Group(TimeStampedModel,SlugModel):
    '''
    Groups are the main unit on VetCove. Each user belongs to a group, which can be a supplier,
    clinic, or even a client. Majority of foreign references refer directly to this group object
    '''
    ##### General Information #######

    # Company / Clinic Name
    name = models.CharField(max_length=100,blank=True,verbose_name="Company Name")
    # Points back to a user of this group
    administrator = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='group_administrator')
    # Contact Name is the name of the contact (suppliers) or purchaser (clinics)
    contact_name = models.CharField(max_length=100,verbose_name="Primary Contact Name")
    # The position of the point of contact / purchaser
    contact_position = models.CharField(max_length=100,verbose_name="Position of Primary Contact")
    # We use the email of the administrator as the point of contact
    phone_number = models.BigIntegerField(max_length=15,null=True,blank=True,verbose_name="Phone Number")
    address = models.ForeignKey('Address',related_name="main_address")
    website = models.CharField(max_length=60,blank=True)
    logo = models.ImageField(upload_to=create_logo_path,null=True,blank=True)

    ###### Referrals ##########

    # The ID that represents this clinic, set on creation
    referral_id = models.CharField(max_length=10) 
    # When group was created, who referred them?
    referred_by = models.ForeignKey('self',null=True,blank=True)


    ###### Payments ##########

    # The URI for the group's payment on Balanced
    balanceduri = models.CharField(max_length=255,blank=True,null=True)
    #payment_method = models.ForeignKey('payment.Payment',null=True,blank=True,related_name='basic_payment_method')
    #payout_method = models.ForeignKey('payment.Payment',null=True,blank=True,related_name='basic_payout_method')
    

    ### Sign Up + Verification #######

    # Where are they in the sign up process
    signup_stage = models.PositiveIntegerField(default=1)
    # Are they verified by us? this is manually turned on by a Vetcove Staff Member
    verified = models.BooleanField(default=False)


    ###### Group Foreign Keys ##########

    # References to clinic and supplier objects
    # In forms, clean() ensures that either clinic or supplier is not null
    GROUP_TYPES = (
        ('clinic','clinic'),
        ('supplier','supplier')
    )
    group_type = models.CharField(max_length=10,choices=GROUP_TYPES) 
    clinic = models.OneToOneField('clinics.Clinic',null=True,blank=True)
    supplier = models.OneToOneField('suppliers.Supplier',null=True,blank=True)
    
    ###### Group Foreign Keys ##########

    # A group can belong to several different buying groups
    buying_groups = models.ManyToManyField('BuyingGroup',null=True,blank=True) 

    def group(self):
        # Provide a handle to access the group specific credentials
        return self.supplier if self.group_type == 'supplier' else self.clinic


    def save(self, *args, **kwargs):
        if self.pk is None:
            # Set the referrer ID before model creation
            self.referrer_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))
        super(Group,self).save(*args,**kwargs)


    def __str__(self):
        return self.name


############################################
############ Addresses #####################
############################################

class Address(models.Model):
    '''
    Address
    '''
    group = models.ForeignKey(Group,related_name="address_group",null=True,blank=True)
    name = models.CharField(max_length=100) # full name
    address_one = models.CharField(max_length=100, verbose_name = "Address Line 1", help_text="Street Address, P.O. Box, Company Name c/o") 
    address_two = models.CharField(max_length=100, blank=True, verbose_name="Apartment, Suite, Unit, Building, Floor, etc.") 
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100) # Can be state/province/or region
    country = models.CharField(max_length=3, default="usa")
    postalcode = models.CharField(max_length=6,verbose_name="Zipcode") 
    # Phone number is used for non-primary addresses (drop ship addresses)
    phone_number = models.BigIntegerField(max_length=15,blank=True,null=True,verbose_name="Phone Number")

    def __str__(self):
        '''
        Prints the complete address
        '''
        address_two_string = str(self.address_two)+"\n" if self.address_two else ""
        return str(self.name)+"\n"+str(self.address_one)+"\n"+address_two_string+str(self.city)+", "+str(self.state)+" "+str(self.postalcode)


############################################
############ Buying Group ##################
############################################

class BuyingGroup(models.Model):
    '''
    A pricing group is a buying group or vetcove group that gives the
    ability for sellers to have different price points for different groups
    '''
    name = models.CharField(max_length=100) 



