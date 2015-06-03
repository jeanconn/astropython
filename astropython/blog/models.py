"""
Define structures of models.
Each model is automatically translated to database schemas.
"""
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from taggit.managers import TaggableManager

from astropython.settings import STATE_CHOICES,INPUT_CHOICES

TYPE_CHOICES = (
    ('ANNOUNCEMENTS', "Announcements"), ('NEWS', "News"),('GENERAL_BLOG', "Blog")
)

"""
Base Model is an abstract model i.e. It doesn't physically exist in our DB
but merely acts as a common wireframe to create child models. It contains common
properties that we want the child models to have.
"""
class Post(models.Model):
    categories = models.ManyToManyField('category.Category') #Category
    title = models.CharField(max_length=200)#Title of Post
    desciption = models.TextField(null=True,blank=True) #Short abstract
    input_type=models.CharField(max_length=60,choices=INPUT_CHOICES)
    body =models.TextField(blank=False)
    authors = models.ForeignKey(User,blank=True,null=True) #Author of Blog Post
    slug = models.SlugField(unique=True) #Native Slug
    post_type = models.CharField(max_length=60,choices=TYPE_CHOICES,default='Blog') #Type of Post
    state = models.CharField(max_length=60,choices=STATE_CHOICES,default='raw')#State of post
    tags=TaggableManager()#Tags
    created = models.DateTimeField(auto_now_add=True, auto_now=False)  # when first revision was created
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)  # when last revision was created (even if not published)
    published = models.DateTimeField(null=True, blank=True,editable=False)  # when last published

    def __unicode__(self):
		return self.title

"""
Events model are associated with any future events that are planned
"""
class Event(models.Model):
    name = models.CharField(max_length=200)
    creator = models.ForeignKey(User,blank=True,null=True)
    body =models.TextField(blank=False)
    slug = models.SlugField(unique=True)
    state = models.CharField(max_length=60,choices=STATE_CHOICES,default='raw')
    tags=TaggableManager()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)  # when first revision was created
    published = models.DateTimeField(null=True, blank=True,editable=False)  # when last published
    start_date_time = models.DateTimeField()#start time
    end_date_time = models.DateTimeField(blank=True, null=True)#When dies the event end
    all_day_event = models.BooleanField(default=False)#If it is an all day event

    def __unicode__(self): #Format of representation of event
        date_format = '%Y-%m-%d %I:%M %p'
        if self.all_day_event:
            date_format = '%Y-%m-%d'
        return '%(n)s (%(d)s)' % {'n': self.name, 'd': self.start_date_time.strftime(date_format), }

    def active(self):#IF event is active
        if self.start_date_time and self.end_date_time:
            t = timezone.now()
            return self.start_date_time <= t and self.end_date_time >= t
        return False
    active.boolean = True