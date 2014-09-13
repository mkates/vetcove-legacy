# Django Imports
from django.db import models

# Third Party App Imports
from model_utils.models import TimeStampedModel

# In-App Imports
from products.models import Item

############################################
####### Supplier ###########################
############################################

class Supplier(TimeStampedModel):

	primary_contact = models.CharField(max_length=100)
	description = models.TextField()
	can_sell_rx = models.BooleanField(default=False)

	def __str__(self):
		return str(self.group)

class Inventory(TimeStampedModel): 

	'''
	Inventory of each product
	'''

	supplier = models.ForeignKey(Supplier)
	sku = models.CharField(max_length=25,null=True,blank=True) # The uploader's SKU for this product
	item = models.ForeignKey('products.Item')
	quantity_available = models.IntegerField(max_length=8) # Quantity of this amount available
	price = models.BigIntegerField(max_length=14) # Listing Price