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
    categories = models.ManyToManyField('category.Category')#Category of packages
    title = models.CharField(max_length=200)#Title of packages
    authors = models.ForeignKey(User,blank=True,null=True)#Author
    url=models.URLField(blank=True)#URL : homepage of the packages
    slug = models.SlugField(unique=True) #Slug to navigate the webpage
    state = models.CharField(max_length=60,choices=STATE_CHOICES,default='raw') #State of post
    tags=TaggableManager() #tags
    rating=RatingField(range=5) #Ratings
    created = models.DateTimeField(auto_now_add=True, auto_now=False)  # when first revision was created
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)  # when last revision was created (even if not published)
    published = models.DateTimeField(null=True, blank=True,editable=False)  # when last published

    def __unicode__(self):
		return self.title

    class Meta:
        abstract=True

class MarkdownInput(Base):
    body = EpicEditorField() #Markdown Input

class WYSIWYGInput(Base):
    body = tinymce_models.HTMLField() #TinyMCE input


