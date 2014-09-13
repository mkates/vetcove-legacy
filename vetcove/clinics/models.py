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
	return os.path.join('licenses', filename)

##### Paths for Sales Tax Exemption ########
def create_salesexemption_path(instance, filename):
	ext = filename.split('.')[-1]
	filename = "%s.%s" % (str(uuid.uuid4()), ext)
	return os.path.join('salesexemption', filename)


############################################
####### Clinic #############################
############################################

class Clinic(TimeStampedModel):

	### Basic Information ###
	practitioner_name= models.CharField(max_length=60)
	license_no = models.CharField(max_length=60,blank=True,null=True)
	state = models.CharField(max_length=60)
	license = ProcessedImageField(upload_to=create_license_path,format='JPEG',options={'quality': 60},null=True,blank=True)
	license_expiration = models.DateField(null=True,blank=True)
	salesexemption_no = models.CharField(max_length=60,blank=True)
	salesexemption = models.FileField(upload_to=create_salesexemption_path,null=True,blank=True)
	
	### Details ###
	organization_type = models.CharField(max_length=100)
	number_of_vets = models.PositiveIntegerField(default=1)
	practice_size = models.PositiveIntegerField(default=1)
	PRACTICE_TYPES = (('small_animal','Small Animal'),('large_animal','Large Animal'),('mixed','Mixed'))
	practice_type = models.CharField(max_length=60,choices=PRACTICE_TYPES,default='')
	tos = models.BooleanField(default=False) # Did they agree to the TOS?

	def __str__(self):
		return str(self.group)

############################################
####### GPO ################################
############################################

class GPO(models.Model):
	name = models.CharField(max_length=50,unique=True)
	clinics = models.ManyToManyField(Clinic)

