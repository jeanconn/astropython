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
import watson

from astropython.settings import STATE_CHOICES,INPUT_CHOICES

PACKAGE_CHOICES = (
	('Recommended', 'Recommended'),
	('Others', 'Others'),
 )

class BasePost(models.Model):
    title = models.CharField(max_length=200)#Title of the Post
    input_type=models.CharField(max_length=60,choices=INPUT_CHOICES)
    abstract = models.TextField(null=True,blank=True) #Short abstract of the tutorial
    authors = models.ManyToManyField(User,blank=True,null=True) # Collaborators of a tutorial
    body = models.TextField(blank=False)
    slug = models.SlugField(unique=True) #Slug to a tutorial
    state = models.CharField(max_length=60,choices=STATE_CHOICES,default='raw') #State of a tutorial
    tags=TaggableManager() #Tags
    hits = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)  # Date when first revision was created
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)  # Date when last revision was created (even if not published)

    def __unicode__(self):
		return self.title

    class Meta:
        abstract=True

class Tutorial(BasePost):

    def get_absolute_url(self):
        return reverse('main.views.single',kwargs={'section':'tutorials','slug':self.slug})

class Snippet(BasePost):

    def get_absolute_url(self):
        return reverse('main.views.single',kwargs={'section':'snippets','slug':self.slug})

class Wiki(BasePost):

    def get_absolute_url(self):
        return reverse('main.views.single',kwargs={'section':'wiki','slug':self.slug})

class Announcement(BasePost):

    def get_absolute_url(self):
        return reverse('main.views.single',kwargs={'section':'announcements','slug':self.slug})

class News(BasePost):

    def get_absolute_url(self):
        return reverse('main.views.single',kwargs={'section':'news','slug':self.slug})

class Blog(BasePost):

    def get_absolute_url(self):
        return reverse('main.views.single',kwargs={'section':'blog','slug':self.slug})

class Package(BasePost):
    category=models.CharField(max_length=60,choices=PACKAGE_CHOICES,default="Others")
    homepage=models.URLField(blank=True)#URL : homepage of the packages
    docs = models.URLField(blank=True)

    def get_absolute_url(self):
        return reverse('main.views.single',kwargs={'section':'packages','slug':self.slug})

class SeriesTutorial(models.Model):
    title = models.CharField(max_length=200)#Title of the Post
    input_type=models.CharField(max_length=60,choices=INPUT_CHOICES)
    abstract = models.TextField(null=True,blank=True) #Short abstract of the tutorial
    authors = models.ManyToManyField(User,blank=True,null=True) # Collaborators of a tutorial
    tut_series=models.ForeignKey('TutorialSeries',blank=False,null=False)
    order_id=models.IntegerField(default=0)
    body = models.TextField(blank=False)
    slug = models.SlugField(unique=True) #Slug to a tutorial
    created = models.DateTimeField(auto_now_add=True, auto_now=False)  # Date when first revision was created
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)  # Date when last revision was created (even if not published)

    def __unicode__(self):
		return self.title

class TutorialSeries(models.Model):
    title = models.CharField(max_length=200)#Title of the Series
    authors = models.ManyToManyField(User,blank=True,null=True) # Collaborators of a tutorial series
    abstract = models.TextField(null=True,blank=True) #Short abstract of the tutorial series
    slug = models.SlugField(unique=True) #Slug to a tutorial series
    state = models.CharField(max_length=60,choices=STATE_CHOICES,default='raw') #State of a tutorial series
    tags=TaggableManager() #Tags
    created = models.DateTimeField(auto_now_add=True, auto_now=False)  # Date when first revision was created
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)  # Date when last revision was created (even if not published)
    published = models.DateTimeField(null=True, blank=True,editable=False)  # Date when last published
    hits = models.IntegerField(default=0)

    def __unicode__(self):
		return self.title

class EducationalResource(BasePost):
    start_date = models.DateTimeField(null=True, blank=True,help_text="Format : YYYY-MM-DD")#Date the course starts
    instructor_names = models.CharField(max_length=400)#Names of Instructors
    website = models.URLField(blank=True)#Website hosting the course, or having more info about the course
    contents = models.TextField(blank=True) #Syllabus or contents of the course
    background = models.TextField()#Recommended Backgroud
    faq=models.TextField(blank=True)#FAQ if any
    language = models.CharField(max_length=200,blank=True)#Language in which course is to be conducted

    def get_absolute_url(self):
        return reverse('main.views.single',kwargs={'section':'education','slug':self.slug})

"""
Events model are associated with any future events that are planned
"""
class Event(models.Model):
    title = models.CharField(max_length=200)
    input_type=models.CharField(max_length=60,choices=INPUT_CHOICES)
    authors = models.ManyToManyField(User,blank=True,null=True) # Collaborators of a tutorial
    body =models.TextField(blank=False)
    location = models.CharField(max_length=1000,blank=True)
    website = models.URLField(blank=True)
    slug = models.SlugField(unique=True)
    state = models.CharField(max_length=60,choices=STATE_CHOICES,default='raw')
    tags=TaggableManager()
    hits = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)  # Date when first revision was created
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)  # Date when last revision was created (even if not published)
    start_date_time = models.DateTimeField(help_text="Format : YYYY-MM-DD")#start time
    end_date_time = models.DateTimeField(blank=True, null=True,help_text="Format : YYYY-MM-DD")#When dies the event end
    all_day_event = models.BooleanField(default=False)#If it is an all day event

    def __unicode__(self): #Format of representation of event
        date_format = '%Y-%m-%d %I:%M %p'
        if self.all_day_event:
            date_format = '%Y-%m-%d'
        return '%(n)s (%(d)s)' % {'n': self.title, 'd': self.start_date_time.strftime(date_format), }

    def active(self):#IF event is active
        if self.start_date_time and self.end_date_time:
            t = timezone.now()
            return self.start_date_time <= t and self.end_date_time >= t
        return False
    active.boolean = True

    def get_absolute_url(self):
        return reverse('main.views.single',kwargs={'section':'events','slug':self.slug})

secretballot.enable_voting_on(Tutorial)
secretballot.enable_voting_on(Snippet)
secretballot.enable_voting_on(Wiki)
secretballot.enable_voting_on(Announcement)
secretballot.enable_voting_on(News)
secretballot.enable_voting_on(Blog)
secretballot.enable_voting_on(Event)
secretballot.enable_voting_on(TutorialSeries)
secretballot.enable_voting_on(EducationalResource)

watson.register(Tutorial)
watson.register(Snippet)
watson.register(Wiki)
watson.register(Announcement)
watson.register(News)
watson.register(Blog)
watson.register(EducationalResource)
watson.register(Package)
watson.register(Event)