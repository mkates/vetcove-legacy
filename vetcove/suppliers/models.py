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
	COMPANY_TYPE_CHOICES = (
		('manu','Manufacturer'),
		('dist','Distributor'),
		('comp','Compounding Pharmacy'),
		('rsell','Reseller')
	)
	company_type = models.CharField(choices=COMPANY_TYPE_CHOICES,max_length=4)
	# Do they sell prescription products?
	sells_rx = models.BooleanField(default=False)
	# Optional Company Information
	description = models.TextField() # Blurb of what the company does
	# The products:manufacturer they have contrrol over
	manufacturer = models.ManyToManyField("products.Manufacturer")
	
	def __str__(self):
		return str(self.group)


class Inventory(TimeStampedModel): 
	'''
	Inventory of the supplier
	'''
	supplier = models.ForeignKey(Supplier)
	sku = models.CharField(max_length=25,null=True,blank=True) # The uploader's SKU for this product
	item = models.ForeignKey('products.Item')
	quantity_available = models.IntegerField(max_length=8) # Quantity of this amount available
	price = models.BigIntegerField(max_length=14) # Listing Price, integer format

	####### Handling Short Date Items ##############
	short_date = models.BooleanField(default=False) # Short date item?
	short_date_expiration = models.DateField(null=True,blank=True) # Expiration date?

