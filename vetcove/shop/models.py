# Standard Library Imports

# Django Imports
from django.db import models

# Third Party App Imports
from model_utils.models import TimeStampedModel

# In App Imports
from accounts.models import Group
from products.models import Inventory


###########################################
###### Shopping Cart Items ################
###########################################


class CartItem(TimeStampedModel):

	'''
	A Cartitem is a cart item associated with a group

	'''

	buyer = models.ForeignKey('accounts.Group')
	inventory = models.ForeignKey('products.Inventory')
	quantity = models.IntegerField(default=1,max_length=4)
	
	### Shipping  ###
	address = models.ForeignKey('accounts.Address')
	SHIPPING_OPTION_TYPES = (
		('std','Standard'),
		('two','Two Day'),
		('one','One Day')
	)
	shipping_type = models.CharField(default="std",choices=SHIPPING_OPTION_TYPES,max_length=3)
	
	instructions = models.TextField() # The special shipping/seller instructions


	def total(self):
		return self.inventory.price*self.quantity