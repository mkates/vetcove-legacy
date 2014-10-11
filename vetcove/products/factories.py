from __future__ import absolute_import

import factory

from .models import *
from accounts.factories import GroupFactory

class ManufacturerFactory(factory.DjangoModelFactory):
    '''
    Generate Manufacturers
    '''
    class Meta:
        model = Manufacturer

    name = factory.Sequence(lambda n: 'manufacturer_%d' % n)


class CategoryFactory(factory.DjangoModelFactory):
    '''
    Generate Categories, requires and level
    '''
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: 'category_%d' % n)
    level = 1

class ProductFactory(factory.DjangoModelFactory):
    '''
    Product Factory
    '''
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: 'product_%d' % n)

class ItemFactory(factory.DjangoModelFactory):
    '''
    Item Factory
    '''
    class Meta:
        model = Item

    name = factory.Sequence(lambda n: 'item_%d' % n)
    manufacturer_no = "12345"
    unit = 'each'
    msrp_price = '3000'

class InventoryFactory(factory.DjangoModelFactory):
    '''
    Inventory Factory
    '''
    class Meta:
        model = Inventory

    supplier = factory.SubFactory(GroupFactory)
    quantity_available = 10
    price = 2500

class TagClassFactory(factory.DjangoModelFactory):
    '''
    Tag Class Factory
    '''
    class Meta:
        model = TagClass

    name = factory.Sequence(lambda n: 'tagclass_%d' % n)

class TagFactory(factory.DjangoModelFactory):
    '''
    Tag Factory
    '''
    class Meta:
        model = Tag

    