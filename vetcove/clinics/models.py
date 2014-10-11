# Standard Library Imports

# Django Imports
from django.db import models

# Third Party App Imports
from imagekit.processors import ResizeToFill, ResizeToFit
from imagekit.models import ProcessedImageField
from model_utils.models import TimeStampedModel


####### Paths for Licenses  ###############
def create_license_path(instance, filename):
	ext = filename.split('.')[-1]
	filename = "%s.%s" % (str(uuid.uuid4()), ext)
	return os.path.join('license', filename)

####### Paths for Sales Exemption Certs ####
def create_sales_exempt_path(instance, filename):
	ext = filename.split('.')[-1]
	filename = "%s.%s" % (str(uuid.uuid4()), ext)
	return os.path.join('sales_certificate', filename)

############################################
####### Clinic #############################
############################################

class Clinic(TimeStampedModel):
	'''
	The credentials of a clinic and some details about their practice
	'''
	### Basic Information ###
	first_name= models.CharField(
		max_length=60,
		verbose_name="First Name"
	)
	middle_initial = models.CharField(
		max_length=1,
		verbose_name="M.I.",
		blank=True,
	)
	last_name = models.CharField(
		max_length=60,
		verbose_name="Last Name"
	)
	license_state = models.CharField(
		max_length=2,
		verbose_name = "State of License"
	)
	# We use file field to accrpt both images and PDFs of the license
	license_image = models.FileField(
		upload_to=create_license_path,
		blank=True
	)
	license_no = models.CharField(
		max_length=60,
		verbose_name = "Veterinary License Number",
	)
	license_expiration = models.DateField(
		verbose_name = "License Expiration Date",
	)
	
	### Details ###
	number_of_vets = models.PositiveIntegerField(
		default=1,
		verbose_name="Number of veterinarians in the clinic"
	)
	PRACTICE_TYPES = (
		('sae','Small Animal Exclusive'),
		('msa','Mixed, Mostly Small Animal'),
		('mla','Mixed, Mostly Large Animal'),
		('lae','Large Animal Exclusive'),
		('e','Equine'), # Horse
		('p','Porcine'), # Pigs
		('f','Feline'), # Cats
		('b','Bovine'), # Cows
		('gov','Government'),
		('ri','Research Institution'),
		('ti','Teaching Institution'),
		('o','Other')
	)
	practice_type = models.CharField(
		max_length=3,
		choices=PRACTICE_TYPES,
		verbose_name = "Practice Type",
		default='o'
	)

	def __str__(self):
		''' Return the name of the group'''
		return str(self.group)

	def name(self):
		''' Returns the full name of the licensed practitioner'''
		middle_initial = self.middle_initial+" " if self.middle_initial else ""
		return str(self.first_name)+str(self.middle_initial)+str(self.last_name)

class SalesExemption(TimeStampedModel):
	'''
	Sales Exemption Model, including the categories that a practice is exempt
	'''
	clinic = models.ForeignKey(Clinic)
	approved = models.BooleanField(default=False)
	full_exempt = models.BooleanField(default=False)
	sales_exemption_number = models.CharField(max_length=100)
	## TODO: COMPLETE THIS MODEL


############################################
####### GPO ################################
############################################

class GPO(models.Model):
	name = models.CharField(max_length=50,unique=True)
	clinics = models.ManyToManyField(Clinic)

