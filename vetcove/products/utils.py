from .models import *

from fuzzywuzzy import fuzz, process

### Utility functions for finding and searching through products ###


def getSubCategoriesFromACategory(category):
	'''
	This function takes in a category object and returns all of the 
	categories that are below it in the category tree
	Input: category object
	Output: A list of categories, including itself
	'''
	CATEGORY_LEVELS = 4 # The depth of our category tree
	category_level = category.level # The level of the category we are looking at
	# The category list stores all the sub categories, including itself
	master_category_list = [category]

	# Work our way down the chain
	while category_level < CATEGORY_LEVELS:
		# For each category in our list at the category_level, grab its subcategories
		# and add it to the master list
		for cat in [cat for cat in master_category_list if cat.level == category_level]:
			new_categories = Category.objects.filter(parents=cat,level=category_level+1)
			master_category_list += list(new_categories)
		# Move down to the next level
		category_level += 1

	return master_category_list


def getProductsFromACategory(category):
	'''
	Returns all of the products for a Category (including subcategories)
	'''
	return Product.objects.filter(category__in=getSubCategoriesFromACategory(category))



def productScore(search,product):
	'''
	Gives a search rank score for each product and search word (out of 100).
	Will eventually include things like order history and past viewed products
	to boost the score. 
	'''
	sorted_string = sorted(search.lower().split(" "))
	# We use partial ratio as a way to capture searches that only
	# incorporate a piece of the match
	return fuzz.partial_ratio(product.name,''.join(sorted_string))


def productSearch(search,filters={},page_number=1,results=10):
	'''
	Takes a search word, and a dictionary of filters, and returns 
	an ordered list of products. 
	Filter Keys: 
	Category_id: pk of category
	Compounds: 'y' (yes),'n' (no), or 'b' (both)
	Manufacturers: List of IDs, i.e. [1,4,10]
	'''

	### 1. Create the filters for the product search with the default filters ###
	
	kwargs = {} # Filters list, '{0}__{1}'.format('name', 'startswith'): 'A',

	# Category Filter
	if 'category' in filters:
		category = Category.objects.get(id=filters['category'])
		kwargs['category__in'] = getSubCategoriesFromACategory(category)

	# Compounds Filter
	if 'compounds' in filters:
		if filters['compounds'] == 'n':
			kwargs['is_compound'] = False
		elif filters['compounds'] == 'y':
			kwargs['is_compound'] = True

	# Manufacturer Filter
	if 'manufacturers' in filters:
		kwargs['manufacturer__in'] = filters['manufacturers']

	# Price Filters
	if 'high_price' in filters:
		kwargs['low_price__lte'] = filters['high_price']
	if 'low_price' in filters:
		kwargs['high_price__gte'] = filters['low_price']

	# Rating
	if 'rating' in filters:
		kwargs['rating__gte'] = filters['rating']

	# Discount
	if 'discount' in filters:
		kwargs['discount__gte'] = filters['discount']

	# Include unavailable
	if 'only_available' in filters:
		kwargs['available'] = True
	
	# @TODO: Short date items

	# Filter the products in one massive query
	products = Product.objects.filter(**kwargs)
	### 2. Filter by the custom tags 

	# Convert the custom filter's tags into a better format
	# (Tag Name, Tag Value, Tag Filter Type)
	# Tag Filter Types: Match (text), GTE (integers), LTE (integers)
	required_tags = []
	# Get the TagClasses that we need to filter by
	for tag_class in TagClass.objects.filter(name__in=list(filters.keys())):
		# Meta Tag Information
		tag_type = tag_class.tag_type
		tag_value = filters[tag_class.name]
		# If the tag is a text tag
		if tag_type == 'tex':
			for tv in tag_value:
				required_tags.append((tag_class,tv,'match'))
		# If the tag is a number tag
		elif tag_type == 'num':
			required_tags.append((tag_class,tag_value[0],'gte'))
			required_tags.append((tag_class,tag_value[1],'lte'))

	# Filter out products that do not have all the required_tags
	final_products = []
	for product in products:
		# Grab a product's tags, which we check each required_tag against
		product_tags = product.tag_set.all().prefetch_related('tag_class')
		success = True
		for tag in required_tags:
			if tag[2] == 'match':
				if not product_tags.filter(tag_class=tag[0],value=tag[1]).exists():
					success=False
					break
			if tag[2] == 'gte':
				if not product_tags.filter(tag_class=tag[0],value__gte=tag[1]).exists():
					success=False
					break
			if tag[2] == 'lte':
				if not product_tags.filter(tag_class=tag[0],value__lte=tag[1]).exists():
					success=False
					break
		if success:
			final_products.append(product)
	
	### 3. Rank the products, and sort by product score
	ranked_products = sorted(final_products,key=lambda product: productScore(search,product), reverse=True) 


	### 4. Return by page number and results
	results_size = page_number*results
	return ranked_products[(results_size-results):results_size]





