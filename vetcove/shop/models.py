# Standard Library Imports

# Django Imports
from django.db import models

# Third Party App Imports
from model_utils.models import TimeStampedModel

# In App Imports
from accounts.models import Group
from suppliers.models import Inventory


###########################################
###### Shopping Cart Items ################
###########################################


class CartItem(TimeStampedModel):

	'''A Cartitem is a products.Item and a quantity that is
	associated with a group'''

	group = models.ForeignKey('accounts.Group')
	inventory = models.ForeignKey('suppliers.Inventory') # Null means they'll take any supplier
	address = models.ForeignKey('accounts.Address')
	quantity = models.IntegerField(default=1,max_length=4)

	def total(self):
		return self.inventory.price*self.quantity