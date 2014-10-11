# Standard Library Imports
import uuid, os

# Django Imports
from django.db import models

# Third Party App Imports
from model_utils.models import TimeStampedModel
from imagekit.processors import ResizeToFill, ResizeToFit
from imagekit.models import ProcessedImageField, ImageSpecField

# In App Imports
from core.models import SlugModel,ImageSizes

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
    image = models.ForeignKey('ProductImage',null=True,blank=True)

############ Categories ####################

class Category(TimeStampedModel,SlugModel):
    ''' 
    Categories 
    '''
    name = models.TextField(max_length=200)
    #industry = models.ManyToManyField(Industry)
    # We use three tiers for our category trees,
    # Rule is a parent must be at a higher level than you
    parents = models.ManyToManyField('self',null=True,blank=True) 
    LEVEL_CHOICES = ((1,1),(2,2),(3,3),(4,4))
    level = models.IntegerField(default=1,max_length=1,choices=LEVEL_CHOICES)

    def __str__(self):
        return self.name

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
    # Is this a prescription item
    is_rx = models.BooleanField(default=False)
    is_compound = models.BooleanField(default=False)
    mainimage = models.ForeignKey('ProductImage',related_name="product_mainimage",null=True,blank=True)

    def rating(self):
        #@TODO
        return None

    ### Storing normalized fields ###
    low_price = models.BigIntegerField(max_length=13,null=True,blank=True)
    high_price = models.BigIntegerField(max_length=13,null=True,blank=True)
    rating = models.IntegerField(max_length=2,default=0)
    discount = models.IntegerField(max_length=2,default=0) # Percentage, integer format
    available = models.BooleanField(default=False)

    def updateNormalizedFields(self):
        '''
        Updates the normalized fields based on the inventory related
        to this product
        '''
        items = self.item_set.all()
        inventory = Inventory.objects.filter(item__in=items).prefetch_related("item")
        quantity_available = sum([inventory_obj.quantity_available for inventory_obj in inventory])
        if inventory:
            self.low_price = min([inventory_obj.price for inventory_obj in inventory])
            self.high_price = max([inventory_obj.price for inventory_obj in inventory])
            discount = min([invntry.price/float(invntry.item.msrp_price) for invntry in inventory])
            self.discount = int((1 - round(discount,2))*100)
        else:
            self.low_price, self.high_price = None, None
        self.available = True if quantity_available else False

        self.save()
        return

class Item(TimeStampedModel,SlugModel):
    '''
    Item's are products with multiple types, i.e. 50mg and 100mg versions ###
    '''
    name = models.TextField(max_length=200)
    product = models.ForeignKey(Product)
    manufacturer_no = models.CharField(max_length=25,null=True,blank=True)
    # An item is assigned a main image
    mainimage = models.ForeignKey('ProductImage',related_name="item_mainimage",null=True,blank=True)
    description = models.CharField(max_length=300) # Describes it's size, color, amount, etc.
    unit = models.CharField(max_length=100) # Will eventually have choices for this
    msrp_price = models.BigIntegerField(max_length=13)

    def __str__(self):
        return "{}: {}".format(self.product,self.name)

class Inventory(TimeStampedModel): 
    '''
    Inventory of the supplier
    '''
    supplier = models.ForeignKey('accounts.Group')
    sku = models.CharField(max_length=25,null=True,blank=True) # The uploader's SKU for this product
    item = models.ForeignKey('Item')
    quantity_available = models.IntegerField(max_length=8) # Quantity of this amount available
    price = models.BigIntegerField(max_length=14) # Listing Price, integer format

    ####### Handling Short Date Items ##############
    short_date = models.BooleanField(default=False) # Short date item?
    short_date_expiration = models.DateField(null=True,blank=True) # Expiration date?


############################################
####### Product Tags #######################
############################################

class TagClass(models.Model):
    '''
    A tag is a searchable text string associated with a specific Category, to give more search
    parameters for a given category. Examples of tag names include the following: size, length,
    diameter, ingredient, form (powder, granule), species (equine, bovine),
    size (small,medium,large)
    '''
    category = models.ManyToManyField(Category,null=True,blank=True)
    name = models.CharField(max_length=100) 
    # A tag can be associated with the category's items or their products. For example, in an IV Set,
    # the length is specific to the item but should still be filterable
    TAG_TYPE_CHOICES = (('tex','text'),('int','number'))
    tag_type = models.CharField(max_length=3,choices=TAG_TYPE_CHOICES,default='tex')
    # Should this class be a filtering option on the search page?
    searchable = models.BooleanField(default=True)


class Tag(models.Model):
    ''' 
    The tag itself, which includes the value
    '''
    product = models.ForeignKey(Product)
    tag_class = models.ForeignKey(TagClass)
    value = models.CharField(max_length=200)


############################################
####### Product Media ######################
############################################

def image_path(instance, filename):
    ''' File path for images of a product '''
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(uuid.uuid4().hex), ext)
    return os.path.join('products/images', filename)

def file_path(instance, filename):
    ''' File path for PDF, PPT, doc (non-images) of a product '''
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(uuid.uuid4().hex), ext)
    return os.path.join('products/files', filename)
    
class ProductImage(TimeStampedModel,ImageSizes):
    '''
    Images of products are associated with a specific product,
    and optionally, an item as well
    '''
    product = models.ForeignKey(Product,related_name="image_product")
    # Can also be associated with an item of the product
    item = models.ForeignKey(Item,null=True,blank=True)
    image = models.ImageField(upload_to=image_path,null=True,blank=True)


class ProductFile(TimeStampedModel):
    '''
    A product file includes PDF and any other non-image files associated with a product
    '''
    product = models.ForeignKey(Product)
    file = models.FileField(upload_to=file_path)


class ProductVideo(TimeStampedModel):
    '''
    Product videos are YouTube links which are embedded into 
    the site
    '''
    product = models.ForeignKey(Product)
    url = models.CharField(max_length=200)
    SOURCE_TYPES = (('yt','YouTube'),)
    source = models.CharField(choices=SOURCE_TYPES,default="yt",max_length=2)


