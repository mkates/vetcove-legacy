from __future__ import absolute_import

from django.core.management.base import BaseCommand, CommandError

import factory

from accounts.models import *
from accounts.factories import *

from products.models import *
from products.factories import *

class Command(BaseCommand):
    help = 'Populates the database from the factory boys'

    def handle(self, *args, **options):

        ### Categories
        Category.objects.all().delete()
        c_1, c_2, c_3, c_4 = CategoryFactory(), CategoryFactory(), CategoryFactory(), CategoryFactory()
        c_5, c_6, c_7 = CategoryFactory(level=2), CategoryFactory(level=2), CategoryFactory(level=2)
        c_8, c_9, c_10 = CategoryFactory(level=3), CategoryFactory(level=3), CategoryFactory(level=3)
        c_5.parents.add(c_1,c_2)
        c_6.parents.add(c_1)
        c_7.parents.add(c_1)
        c_8.parents.add(c_5,c_6)
        c_9.parents.add(c_6)
        c_10.parents.add(c_7)

        ### Manufacturers
        Manufacturer.objects.all().delete()
        m_1, m_2, m_3 = ManufacturerFactory(), ManufacturerFactory(), ManufacturerFactory()


        ### Products
        Product.objects.all().delete()
        p_1 = ProductFactory(category=c_6,manufacturer=m_1)
        p_2 = ProductFactory(category=c_6,manufacturer=m_2)
        p_3 = ProductFactory(category=c_8,manufacturer=m_3)
        p_4 = ProductFactory(category=c_8,manufacturer=m_1)
        p_5 = ProductFactory(category=c_8,manufacturer=m_2)
        p_6 = ProductFactory(category=c_8,manufacturer=m_3)
        p_7 = ProductFactory(category=c_9,manufacturer=m_1)

        # Items
        Item.objects.all().delete()
        i_1 = ItemFactory(product=p_1,msrp_price=2500)
        i_2 = ItemFactory(product=p_1,msrp_price=5000)
        i_3 = ItemFactory(product=p_2,msrp_price=8000)
        i_4 = ItemFactory(product=p_2,msrp_price=16000)
        i_5 = ItemFactory(product=p_3,msrp_price=1234)
        i_6 = ItemFactory(product=p_4,msrp_price=2345)
        i_7 = ItemFactory(product=p_5,msrp_price=3456)
        i_8 = ItemFactory(product=p_6,msrp_price=1000)
        i_9 = ItemFactory(product=p_6,msrp_price=5000)
        i_9 = ItemFactory(product=p_7,msrp_price=100000)

        ### Inventory
        Inventory.objects.all().delete()
        inv_1 = InventoryFactory(item=i_1,price=2300)
        inv_1 = InventoryFactory(item=i_1,price=2100)
        inv_1 = InventoryFactory(item=i_2,price=4900)
        inv_1 = InventoryFactory(item=i_2,price=4700)
        inv_1 = InventoryFactory(item=i_3,price=16000)
        inv_1 = InventoryFactory(item=i_4,price=1000)
        inv_1 = InventoryFactory(item=i_5,price=3456)
        inv_1 = InventoryFactory(item=i_6,price=1000)
        inv_1 = InventoryFactory(item=i_7,price=1000)
        inv_1 = InventoryFactory(item=i_8,price=1000)
        inv_1 = InventoryFactory(item=i_9,price=90000)

        

