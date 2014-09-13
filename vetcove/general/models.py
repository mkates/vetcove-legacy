# Standard Library Imports

# Django Imports
from django.db import models

# Third Party App Imports


# Create your models here.
class SupplierInformation(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	company = models.CharField(max_length=100)
	current_selling_method = models.CharField(max_length=100)
	interest_listings = models.BooleanField(default=False)
	interest_community = models.BooleanField(default=False)
	interest_promotions = models.BooleanField(default=False)
	interest_direct = models.BooleanField(default=False)
	product_size = models.CharField(max_length=100)
	referral_source = models.CharField(max_length=100,blank=True)