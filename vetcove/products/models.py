# Standard Library Imports
import uuid, os

# Django Imports
from django.db import models

# Third Party App Imports
from model_utils.models import TimeStampedModel
from imagekit.processors import ResizeToFill, ResizeToFit
from imagekit.models import ProcessedImageField

# In App Imports
from core.models import SlugModel, ImageModel

############################################
####### Product Database Models ############
############################################

class Industry(TimeStampedModel,SlugModel):

	'''Industries'''
	def test():
		return


class Manufacturer(TimeStampedModel,SlugModel):

	'''Manufacturers of product in the system, not the group manufacturers!'''

	description = models.TextField(blank=True) # One sentence description of this manufacturer
	image = models.ForeignKey('Image',null=True,blank=True)

############ Categories ####################

class Category(TimeStampedModel,SlugModel):

	''' Categories '''

	industry = models.ManyToManyField(Industry)
	level = models.IntegerField(default=1,max_length=1)

############################################
############ Catalog #######################
############################################

class Product(TimeStampedModel,SlugModel):

	'''
	Products (which are a group of items, these are always unique at the manufactuer level)
	'''

	manufacturer = models.ForeignKey(Manufacturer)
	category = models.ForeignKey(Category)
	description = models.TextField()
	mainimage = models.ForeignKey('Image',null=True,blank=True)
	views = models.IntegerField(default=0)


class Item(TimeStampedModel,SlugModel):

	'''
	Item's are products with multiple types, i.e. 50mg and 100mg versions ###
	'''

	product = models.ForeignKey(Product)
	manufacturer_no = models.CharField(max_length=25,null=True,blank=True)
	description = models.TextField()
	itemimage = models.ForeignKey('Image',related_name="itemimage",null=True,blank=True) # if size specific image is available
	msrp_price = models.BigIntegerField(max_length=13)
	purchases = models.IntegerField(default=0)
	def __str__(self):
		return self.product.name


class Tags(models.Model):

	'''
	Tags are used for connecting products outside of traditional category tiers, for more search criteria.
	These includes things like length, rx, wound_support, etc.
	'''

	name = models.CharField(max_length=50)
	KEY_CHOICES = [('rx', 'rx'), ('compendium', 'compendium'), ('length', 'length'), ('wound_support', 'wound_support'), ('colors', 'colors'), ('year', 'year'), ('contract', 'contract')]
	key = models.CharField(max_length=20,choices=KEY_CHOICES)
	value = models.CharField(max_length=100)
	products = models.ManyToManyField(Product)



############################################
####### Product Images #####################
############################################
		
class Image(TimeStampedModel,ImageModel):
	item = models.ForeignKey(Product)





