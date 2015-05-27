from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from taggit.managers import TaggableManager

from djangoratings.fields import RatingField
from epiced.models import EpicEditorField
from tinymce import models as tinymce_models

from astropython.settings import STATE_CHOICES

class Base(models.Model):
    categories = models.ManyToManyField('category.Category')
    title = models.CharField(max_length=200)
    authors = models.ForeignKey(User,blank=True,null=True)
    url=models.URLField(blank=True)
    slug = models.SlugField(unique=True)
    state = models.CharField(max_length=60,choices=STATE_CHOICES,default='raw')
    tags=TaggableManager()
    rating=RatingField(range=5)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)  # when first revision was created
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)  # when last revision was created (even if not published)
    published = models.DateTimeField(null=True, blank=True,editable=False)  # when last published

    def __unicode__(self):
		return self.title

    class Meta:
        abstract=True

class MarkdownInput(Base):
    body = EpicEditorField()

class WYSIWYGInput(Base):
    body = tinymce_models.HTMLField()


