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
	first_name= models.CharField(max_length=60)
	middle_initial = models.CharField(max_length=1,null=True,blank=True)
	last_name = models.CharField(max_length=60)
	license_state = models.CharField(max_length=2)
	# We use file field to accrpt both images and PDFs of the license
	license_image = models.FileField(upload_to=create_license_path,null=True,blank=True)
	license_no = models.CharField(max_length=60,blank=True,null=True)
	license_expiration = models.DateField(null=True,blank=True)
	
	### Details ###
	number_of_vets = models.PositiveIntegerField(default=1)
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
	practice_type = models.CharField(max_length=3,choices=PRACTICE_TYPES,default='o')

	def __str__(self):
		return str(self.group)

	def name(self):
		return str(self.first_name)+" "+self

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

