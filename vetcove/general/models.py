# Standard Library Imports

# Django Imports
from django.db import models

# Third Party App Imports
from model_utils.models import TimeStampedModel

# Create your models here.
class SupplierLead(TimeStampedModel):
	company = models.CharField(max_length=100)
	current_selling_method = models.CharField(max_length=100)
	interest_listings = models.BooleanField(default=False)
	interest_community = models.BooleanField(default=False)
	interest_promotions = models.BooleanField(default=False)
	interest_direct = models.BooleanField(default=False)
	product_size = models.CharField(max_length=100)
