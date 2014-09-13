# Standard Library Imports

# Django Imports
from django.db import models

# Third Party App Imports
from model_utils.models import TimeStampedModel

# In App Imports
from accounts.models import Group
from products.models import Product


############################################
####### Review #############################
############################################
class Review(TimeStampedModel):

	'''The base review model'''

	### General Information ###
	review = models.TextField()
	ratings = models.IntegerField(default=2)
	verified = models.BooleanField(default=False) # Defaults to false until implemented
	product = models.ForeignKey('products.Product')
	group = models.ForeignKey('accounts.Group')
	author = models.CharField(max_length=60)


############################################
####### Review Comment #####################
############################################
class ReviewComment(TimeStampedModel):

	'''Comments on a review'''

	### General Information ###
	comment = models.TextField()
	review = models.ForeignKey(Review)
	author = models.CharField(max_length=60)
	group = models.ForeignKey('accounts.Group')


############################################
####### Review Upvotes ###################
############################################
class ReviewVote(TimeStampedModel):

	'''Vote for a review'''
	
	group = models.ForeignKey('accounts.Group')
	review = models.ForeignKey(Review)
	is_upvote = models.BooleanField(default=True) #True: Upvote, False: Downvote


############################################
####### Answer Upvotes #####################
############################################
class ReviewCommentVote(TimeStampedModel):

	'''Vote for a review comment'''

	group = models.ForeignKey('accounts.Group')
	review_comment = models.ForeignKey(ReviewComment)
	is_upvote = models.BooleanField(default=True) #True: Upvote, False: Downvote



