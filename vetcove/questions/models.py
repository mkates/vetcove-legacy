# Standard Library Imports

# Django Imports
from django.db import models

# Third Party App Imports
from model_utils.models import TimeStampedModel

# In App Imports
from accounts.models import Group
from products.models import Product


############################################
#######  Question ##########################
############################################
class Question(TimeStampedModel):

	'''The base question model'''

	### General Information ###
	question = models.TextField()
	product = models.ForeignKey('products.Product')
	author = models.CharField(max_length=60)
	group = models.ForeignKey('accounts.Group')


############################################
####### Answer #############################
############################################
class Answer(TimeStampedModel):

	'''Answers to a question'''

	### General Information ###
	answer = models.TextField()
	question = models.ForeignKey(Question)
	author = models.CharField(max_length=60)
	group = models.ForeignKey('accounts.Group')


############################################
####### Question Upvotes ###################
############################################
class QuestionVote(TimeStampedModel):

	'''Upvote for a question'''

	group = models.ForeignKey('accounts.Group')
	question = models.ForeignKey(Question)
	is_upvote = models.BooleanField(default=True) #True: Upvote, False: Downvote


############################################
####### Answer Upvotes #####################
############################################
class AnswerVote(TimeStampedModel):

	'''Upvote for a answer'''

	group = models.ForeignKey('accounts.Group')
	answer = models.ForeignKey(Answer)
	is_upvote = models.BooleanField(default=True) #True: Upvote, False: Downvote

############################################
####### Answer Comment #####################
############################################
class AnswerComment(TimeStampedModel):

	'''Comments on an answer'''

	group = models.ForeignKey('accounts.Group')
	answer = models.ForeignKey(Answer)
	comment = models.TextField()
	author = models.CharField(max_length=60)


