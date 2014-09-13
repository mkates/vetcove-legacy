# Django Imports
from django.db import models

# Third Party App Imports
from model_utils.models import TimeStampedModel

# In App Imports
from accounts.models import Group

############################################
####### Supplier ###########################
############################################

class Notification(TimeStampedModel):

	''' The notification object. A notification can be any one of the following:
	questions-answer: An answer to your question
	question-answercomment: A comment on an answer to a question


	'''
	group = models.ForeignKey('accounts.Group')
	viewed = models.BooleanField(default=False)
	NOTIFICATION_TYPES = [('referral','referral')]
	type = models.CharField(max_length=20,choices=NOTIFICATION_TYPES)
	text = models.TextField()

	def __str__(self):
		return str(self.group)