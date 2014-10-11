# Django Imports
from django.db import models

# Third Party App Imports
from model_utils.models import TimeStampedModel

# In-App Imports
from products.models import Item, Manufacturer

############################################
####### Supplier ###########################
############################################

class Supplier(TimeStampedModel):
	'''
	The Main Supplier Model
	'''
	SELLER_TYPE_CHOICES = (
		('manu','Manufacturer'),
		('dist','Distributor'),
		('comp','Compounding Pharmacy'),
		('rsell','Reseller')
	)
	seller_type = models.CharField(choices=SELLER_TYPE_CHOICES,max_length=4)
	# Do they sell prescription products?
	sells_rx = models.BooleanField(default=False)
	# Optional Company Information
	description = models.TextField() # Blurb of what the company does
	# The products:manufacturer they have control over
	manufacturer = models.ManyToManyField("products.Manufacturer")
	
	def __str__(self):
		return str(self.group)

