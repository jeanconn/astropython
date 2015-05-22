from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from taggit.managers import TaggableManager

from djangoratings.fields import RatingField
from tinymce import models as tinymce_models

from astropython.settings import STATE_CHOICES

TYPE_CHOICES = (
    ('ANNOUNCEMENTS', "Announcements"), ('UPCOMING_EVENTS', "Upcoming Events"), ('NEWS', "News"),('GENERAL_BLOG', "Blog")
)

class Post(models.Model):
    categories = models.ManyToManyField('category.Category')
    title = models.CharField(max_length=200)
    desciption = models.TextField(null=True,blank=True)
    authors = models.ForeignKey(User,blank=True,null=True)
    body = tinymce_models.HTMLField()
    slug = models.SlugField(unique=True)
    post_type = models.CharField(max_length=60,choices=TYPE_CHOICES,default='Blog')
    state = models.CharField(max_length=60,choices=STATE_CHOICES,default='raw')
    tags=TaggableManager()
    rating=RatingField(range=2)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)  # when first revision was created
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)  # when last revision was created (even if not published)
    published = models.DateTimeField(null=True, blank=True,editable=False)  # when last published

    def __unicode__(self):
		return self.title


class FileUpload(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    post = models.ForeignKey(Post)

