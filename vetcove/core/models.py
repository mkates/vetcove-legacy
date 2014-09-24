# Standard Library Imports
import ast
# Django Imports
from django.db import models

# Third Party App Imports
from imagekit.processors import ResizeToFill, ResizeToFit
from imagekit.models import ProcessedImageField



###########################################
###### Slug Field Model ###################
###########################################

class SlugModel(models.Model):
    """
    An abstract base class model that provides a slug
    field that is automatically created from the model's name.
    Adds a slug field and a name field.
    """
    slug = models.SlugField()
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SlugModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

###########################################
###### Image ##############################
###########################################

#This function generates a random name for the uploaded image
def get_file_path_original(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(uuid.uuid4()), ext)
    return os.path.join('userimages', filename)

def get_file_path_small(instance, filename):
    ext = filename.split('.')[-1]
    filenamesmall = "%s.%s" % (str(uuid.uuid4())+"_small", ext)
    return os.path.join('userimages', filenamesmall)
    
def get_file_path_medium(instance, filename):
    ext = filename.split('.')[-1]
    filenamemedium = "%s.%s" % (str(uuid.uuid4())+"_medium", ext)
    return os.path.join('userimages', filenamemedium)

class ImageModel(models.Model):
    photo = ProcessedImageField(upload_to=get_file_path_original,processors=[ResizeToFit(1300, 1000)],format='JPEG',options={'quality': 60})
    photo_small = ProcessedImageField(upload_to=get_file_path_small, processors=[ResizeToFit(100, 100)],format='JPEG',options={'quality': 60})
    photo_medium = ProcessedImageField(upload_to=get_file_path_medium, processors=[ResizeToFit(500, 500)],format='JPEG',options={'quality': 60})

    class Meta:
        abstract = True


###########################################
###### ListField  #########################
###########################################

# Untested and unused
class ListField(models.TextField):

    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []
        if isinstance(value, list):
            return value
        return ast.literal_eval(value)

    def get_prep_value(self, value):
        value = value if not value else str(value)
        return super(ListField, self).get_prep_value(value)



