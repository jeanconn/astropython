"""
Define structures of models.
Each model is automatically translated to database schemas.
"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from taggit.managers import TaggableManager

import secretballot

from astropython.settings import STATE_CHOICES,INPUT_CHOICES

"""
Base Model is an abstract model i.e. It doesn't physically exist in our DB
but merely acts as a common wireframe to create child models. It contains common
properties that we want the child models to have.
"""

class Tutorial(models.Model):
    categories = models.ManyToManyField('category.Category') #Categories of tutorial
    title = models.CharField(max_length=200)#Title of the Post
    input_type=models.CharField(max_length=60,choices=INPUT_CHOICES)
    abstract = models.TextField(null=True,blank=True) #Short abstract of the tutorial
    authors = models.ManyToManyField(User,blank=True,null=True) # Collaborators of a tutorial
    body = models.TextField(blank=False)
    slug = models.SlugField(unique=True) #Slug to a tutorial
    state = models.CharField(max_length=60,choices=STATE_CHOICES,default='raw') #State of a tutorial
    tags=TaggableManager() #Tags
    created = models.DateTimeField(auto_now_add=True, auto_now=False)  # Date when first revision was created
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)  # Date when last revision was created (even if not published)
    published = models.DateTimeField(null=True, blank=True,editable=False)  # Date when last published

    def __unicode__(self):
		return self.title


class CodeSnippet(Tutorial):
    snippet = models.TextField(blank=False)#Additional Notes in Markdown

    def __unicode__(self):
		return self.title

class SeriesTutorial(models.Model):
    title = models.CharField(max_length=200)#Title of the Post
    input_type=models.CharField(max_length=60,choices=INPUT_CHOICES)
    abstract = models.TextField(null=True,blank=True) #Short abstract of the tutorial
    authors = models.ManyToManyField(User,blank=True,null=True) # Collaborators of a tutorial
    tut_series=models.ForeignKey('TutorialSeries',blank=False,null=False)
    body = models.TextField(blank=False)
    slug = models.SlugField(unique=True) #Slug to a tutorial
    created = models.DateTimeField(auto_now_add=True, auto_now=False)  # Date when first revision was created
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)  # Date when last revision was created (even if not published)

    def __unicode__(self):
		return self.title

class TutorialSeries(models.Model): #Add different tutorials to a series
    categories = models.ManyToManyField('category.Category') #Categories of tutorial series
    title = models.CharField(max_length=200)#Title of the Series
    authors = models.ManyToManyField(User,blank=True,null=True) # Collaborators of a tutorial series
    abstract = models.TextField(null=True,blank=True) #Short abstract of the tutorial series
    included_tutorial = models.ManyToManyField(SeriesTutorial,blank=True,related_name="inc_tut")
    slug = models.SlugField(unique=True) #Slug to a tutorial series
    state = models.CharField(max_length=60,choices=STATE_CHOICES,default='raw') #State of a tutorial series
    tags=TaggableManager() #Tags
    created = models.DateTimeField(auto_now_add=True, auto_now=False)  # Date when first revision was created
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)  # Date when last revision was created (even if not published)
    published = models.DateTimeField(null=True, blank=True,editable=False)  # Date when last published

    def __unicode__(self):
		return self.title

class EducationalResource(Tutorial):
    start_date = models.DateTimeField(null=True, blank=True)#Date the course starts
    instructor_names = models.CharField(max_length=400)#Names of Instructors
    website = models.URLField(blank=True)#Website hosting the course, or having more info about the course
    contents = models.TextField(blank=True) #Syllabus or contents of the course
    background = models.TextField()#Recommended Backgroud
    faq=models.TextField(blank=True)#FAQ if any
    language = models.CharField(max_length=200,blank=True)#Language in which course is to be conducted

    def __unicode__(self):
		return self.title

secretballot.enable_voting_on(Tutorial)
secretballot.enable_voting_on(TutorialSeries)
secretballot.enable_voting_on(EducationalResource)
secretballot.enable_voting_on(CodeSnippet)