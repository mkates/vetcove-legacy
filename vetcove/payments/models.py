from django.db import models

from model_utils.models import TimeStampedModel

from accounts.models import Group

###########################################
############ Payment Objects ##############
###########################################


class Payment(TimeStampedModel):

	'''
	A Payment Method: Credit Card, Bank Account, or Invoice

	'''

	group = models.ForeignKey('accounts.group')


class Card(Payment):
	'''
	Stripe Debit/Credit Card
	'''
	### Stripe Specific Information
	token = models.CharField(max_length=100)
	livemode = models.BooleanField(default=False) # Boolean of whether this token was created with a live or test API key
	used = models.BooleanField(default=False)
	currency = models.CharField(max_length=10,default="usd")

	### Card Details For Display Purposes ###
	brand = models.CharField(max_length=100) # Visa, American Express, MasterCard, Discover, JCB, Diners Club, or Unknown
	exp_month = models.IntegerField(max_length=2)
	exp_year = models.IntegerField(max_length=4)
	last_four = models.IntegerField(max_length=4)

	fingerprint = models.CharField(max_length=250)
	funding = models.CharField(max_length=100) # credit, debit, prepaid, or unknown

	### Card Address Details ###
	name = models.CharField(max_length=250)
	address_line_one = models.CharField(max_length=250)
	address_line_two = models.CharField(max_length=250)
	address_city = models.CharField(max_length=250)
	address_state = models.CharField(max_length=250)
	address_zip = models.CharField(max_length=250)
	address_country = models.CharField(max_length=250)


class BankAccount(Payment):
	'''
	Stripe Bank Account
	'''
	### Stripe Specific Information
	livemode = models.BooleanField(default=False) # Boolean of whether this token was created with a live or test API key
	used = models.BooleanField(default=False)
	currency = models.CharField(max_length=10,default="usd")

	### Bank Account Object ###
	object_id = models.CharField(max_length=100)
	last_four = models.IntegerField(max_length=4)
	country = models.CharField(max_length=10,default="US")
	currency = models.CharField(max_length=10,default="usd")
	status = models.CharField(default="new",max_length=100) # New, Validated, Verified, or Errored
	fingerprint = models.CharField(max_length=250)
	bank_name = models.CharField(max_length=250)


############################################
######### Transfers ########################
############################################

class Transfer(models.Model):
	'''
	Payouts to bank accounts and cards
	'''
	recipient = models.ForeignKey('accounts.Group')
	payment = models.ForeignKey(Payment) # The object the transfer was made to 

	token = models.CharField(max_length=100)
	date = models.BigIntegerField(max_length=14) # Date the transfer was initiated
	livemode = models.BooleanField(default=False) # Boolean of whether this token was created with a live or test API key
	amount = models.BigIntegerField(max_length=20)
	date = models.DateTimeField(auto_now_add = True)
	TYPE_CHOICES = (('bank_account','Bank Account'),('card','Card'))
	type = models.CharField(max_length=12,choices=TYPE_CHOICES) # Bank Account or Card
	description = models.TextField() # Internal description of this transaction
	statement_description = models.CharField(max_length=250) #Extra information about a transfer to be displayed on the user’s bank statement. 

	### On Failures ###
	failure_code = models.CharField(max_length=250,blank=True)
	failure_message = models.TextField(blank=True)





