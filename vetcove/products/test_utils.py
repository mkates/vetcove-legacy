from __future__ import absolute_import

from django.test import TestCase

from .factories import *
from .utils import *
from .models import *

class ProductUtilities(TestCase):

	'Tests the product utilities functions'
	def setUp(self):
		### Categories
		self.c_1, self.c_2, self.c_3, self.c_4 = CategoryFactory(), CategoryFactory(), CategoryFactory(), CategoryFactory()
		self.c_5, self.c_6, self.c_7 = CategoryFactory(level=2), CategoryFactory(level=2), CategoryFactory(level=2)
		self.c_8, self.c_9, self.c_10 = CategoryFactory(level=3), CategoryFactory(level=3), CategoryFactory(level=3)
		self.c_5.parents.add(self.c_1,self.c_2)
		self.c_6.parents.add(self.c_1)
		self.c_7.parents.add(self.c_1)
		self.c_8.parents.add(self.c_5,self.c_6)
		self.c_9.parents.add(self.c_6)
		self.c_10.parents.add(self.c_7)

		### Manufacturers
		self.m_1, self.m_2, self.m_3 = ManufacturerFactory(), ManufacturerFactory(), ManufacturerFactory()

		### Create some tags
		self.tagclass_1 = TagClassFactory(name="disease_treated",tag_type='tex')
		self.tagclass_1.category.add(self.c_1)
		self.tagclass_2 = TagClassFactory(name="length",tag_type='num')
		self.tagclass_2.category.add(self.c_1)

		### Products

		self.p_1 = ProductFactory(category=self.c_6,manufacturer=self.m_1)
		self.i_1 = ItemFactory(product=self.p_1,msrp_price=1000)
		self.inv_1 = InventoryFactory(item=self.i_1,price=500)
		self.inv_2 = InventoryFactory(item=self.i_1,price=700)
		self.tag_1 = TagFactory(product=self.p_1,tag_class=self.tagclass_1,value="rabies")
		self.tag_2 = TagFactory(product=self.p_1,tag_class=self.tagclass_1,value="herpes")

		self.p_2 = ProductFactory(category=self.c_6,manufacturer=self.m_2)
		self.i_2 = ItemFactory(product=self.p_2,msrp_price=5000)
		self.i_3 = ItemFactory(product=self.p_2,msrp_price=10000)
		self.inv_3 = InventoryFactory(item=self.i_2,price=5000)
		self.tag_3 = TagFactory(product=self.p_2,tag_class=self.tagclass_2,value=45)

		self.p_3 = ProductFactory(category=self.c_6,manufacturer=self.m_3)
		self.i_4 = ItemFactory(product=self.p_3,msrp_price=6000)


		# Normalize our database
		for product in Product.objects.all():
			product.updateNormalizedFields()

	def test_noFilters(self):
		search_result = productSearch('')
		self.assertEqual(3, len(search_result))

	def test_PriceFilter(self):
		filters = { 'high_price':5500 }
		search_result = productSearch('',filters=filters)
		self.assertEqual(2,len(search_result))

	def test_Manufacturers(self):
		filters = { 'manufacturers':[self.m_1.id,self.m_2.id] }
		search_result = productSearch('',filters=filters)
		self.assertEqual(2,len(search_result))

	def test_Discount(self):
		filters = { 'discount': 50 }
		search_result = productSearch('',filters=filters)
		self.assertEqual(1,len(search_result))

	def test_Available(self):
		filters = { 'only_available': 50 }
		search_result = productSearch('',filters=filters)
		self.assertEqual(2,len(search_result))

	def test_BasicTag(self):
		filters = { 'disease_treated': ['rabies'] }
		search_result = productSearch('',filters=filters)
		self.assertEqual(1,len(search_result))

	def test_TwoTag(self):
		filters = { 'disease_treated': ['rabies','herpes'] }
		search_result = productSearch('',filters=filters)
		self.assertEqual(1,len(search_result))

	def test_FailedTag(self):
		filters = { 'disease_treated': ['rabies','herpes','enterovirus'] }
		search_result = productSearch('',filters=filters)
		self.assertEqual(0,len(search_result))

	def test_IntTag(self):
		filters = { 'length': [40,50] }
		search_result = productSearch('',filters=filters)
		self.assertEqual(1,len(search_result))
		filters = { 'length': [50,60] }
		search_result = productSearch('',filters=filters)
		self.assertEqual(0,len(search_result))








