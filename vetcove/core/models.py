# Standard Library Imports
import ast
# Django Imports
from django.db import models

# Third Party App Imports
from imagekit.processors import ResizeToFill, ResizeToFit
from imagekit.models import ProcessedImageField, ImageSpecField



###########################################
###### Slug Field Model ###################
###########################################

class SlugModel(models.Model):
    """
    An abstract base class model that provides a slug
    field that is automatically created from the model's name.
    Requires a name field
    """
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SlugModel, self).save(*args, **kwargs)

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



