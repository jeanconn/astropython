"""
Define structures of models.
Each model is automatically translated to database schemas.
"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from taggit.managers import TaggableManager

from djangoratings.fields import RatingField
from epiced.models import EpicEditorField
from tinymce import models as tinymce_models

from astropython.settings import STATE_CHOICES

"""
Base Model is an abstract model i.e. It doesn't physically exist in our DB
but merely acts as a common wireframe to create child models. It contains common
properties that we want the child models to have.
"""
class Base(models.Model):
    categories = models.ManyToManyField('category.Category') #Categories of tutorial
    title = models.CharField(max_length=200)#Title of the Post
    #optional logo
    desciption = models.TextField(null=True,blank=True) #Short abstract of the tutorial
    authors = models.ManyToManyField(User,blank=True,null=True) # Collaborators of a tutorial
    slug = models.SlugField(unique=True) #Slug to a tutorial
    state = models.CharField(max_length=60,choices=STATE_CHOICES,default='raw') #State of a tutorial
    tags=TaggableManager() #Tags
    rating=RatingField(range=5) #Ratings
    created = models.DateTimeField(auto_now_add=True, auto_now=False)  # Date when first revision was created
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)  # Date when last revision was created (even if not published)
    published = models.DateTimeField(null=True, blank=True,editable=False)  # Date when last published

    class Meta:
        abstract = True



class MarkdownTutorial(Base):
    body = EpicEditorField() #Tutorial with Markdown Input

    def __unicode__(self):
		return self.title

class WYSIWYGTutorial(Base):
    body = tinymce_models.HTMLField() #Tutorial with WYSIWYG Input

    def __unicode__(self):
		return self.title

class CodeMarkdownTutorial(Base):
    body = models.TextField(blank=False) # Coding Field
    notes = EpicEditorField() #Additional Notes in Mardown

    def __unicode__(self):
		return self.title

class TutorialSeries(Base): #Add different tutorials to a series
    mtutorials = models.ManyToManyField(MarkdownTutorial,null=True)
    wtutorials = models.ManyToManyField(WYSIWYGTutorial,null=True)
    ctutorials = models.ManyToManyField(CodeTutorial,null=True)

    def __unicode__(self):
		return self.title

