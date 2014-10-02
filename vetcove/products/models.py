# Standard Library Imports
import uuid, os

# Django Imports
from django.db import models

# Third Party App Imports
from model_utils.models import TimeStampedModel
from imagekit.processors import ResizeToFill, ResizeToFit
from imagekit.models import ProcessedImageField, ImageSpecField

# In App Imports
from core.models import SlugModel

############################################
####### Product Database Models ############
############################################

class Industry(TimeStampedModel,SlugModel):

    '''Industries'''
    name = models.TextField(max_length=200)


class Manufacturer(TimeStampedModel,SlugModel):

    '''
    Manufacturers of products in the system. There is a a many to many
    relationship between products:manufacturer and suppliers:supplier where
    a supplier can have control over several manufacturers, and a manufacturer's
    content can be edited by multiple suppliers
    '''
    name = models.TextField(max_length=200)
    description = models.TextField(blank=True) # One sentence description of this manufacturer
    image = models.ForeignKey('Image',null=True,blank=True)

############ Categories ####################

class Category(TimeStampedModel,SlugModel):
    ''' 
    Categories 
    '''
    name = models.TextField(max_length=200)
    #industry = models.ManyToManyField(Industry)
    # We use three tiers for our category trees,
    # Rule is a parent must be at a higher level than you
    parents = models.ForeignKey('self',null=True,blank=True) 
    LEVEL_CHOICES = ((1,1),(2,2),(3,3),(4,4))
    level = models.IntegerField(default=1,max_length=1,choices=LEVEL_CHOICES)

############################################
############ Catalog #######################
############################################

class Product(TimeStampedModel,SlugModel):
    '''
    Products (which are a group of items, these are always unique at the manufacturer level)
    '''
    name = models.TextField(max_length=200)
    manufacturer = models.ForeignKey(Manufacturer)
    category = models.ForeignKey(Category)
    description = models.TextField()
    mainimage = models.ForeignKey('Image',related_name="product_mainimage",null=True,blank=True)


class Item(TimeStampedModel,SlugModel):

    '''
    Item's are products with multiple types, i.e. 50mg and 100mg versions ###
    '''
    name = models.TextField(max_length=200)
    product = models.ForeignKey(Product)
    manufacturer_no = models.CharField(max_length=25,null=True,blank=True)
    # An item is assigned a main image
    mainimage = models.ForeignKey('Image',related_name="item_mainimage",null=True,blank=True)
    description = models.CharField(max_length=300) # Describes it's size, color, amount, etc.
    unit = models.CharField(max_length=100) # Will eventually have choices for this
    msrp_price = models.BigIntegerField(max_length=13)

    def __str__(self):
        return self.product.name


# class Tags(models.Model):

#   '''
#   Items and products are given special tags, which give extra search parameters
#   and classification mechanisms.  
#   '''

#   pass


############################################
####### Product Images #####################
############################################
def file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(uuid.uuid4()), ext)
    return os.path.join('userimages', filename)
    
class Image(TimeStampedModel):

    product = models.ForeignKey(Product,related_name="image_product",null=True,blank=True)
    # Can also be associated with an item of the product
    item = models.ForeignKey(Item,null=True,blank=True)
    original = models.ImageField(upload_to=file_path,null=True,blank=True)
    thumbnail = ImageSpecField(source='original',
                          processors=[ResizeToFit(200, 200)],
                          format='PNG')




