from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from taggit.managers import TaggableManager

from djangoratings.fields import RatingField
from tinymce import models as tinymce_models
from epiced.models import EpicEditorField

from astropython.settings import STATE_CHOICES

TYPE_CHOICES = (
    ('ANNOUNCEMENTS', "Announcements"), ('NEWS', "News"),('GENERAL_BLOG', "Blog")
)

class Base(models.Model):
    categories = models.ManyToManyField('category.Category')
    title = models.CharField(max_length=200)
    desciption = models.TextField(null=True,blank=True)
    authors = models.ForeignKey(User,blank=True,null=True)
    slug = models.SlugField(unique=True)
    post_type = models.CharField(max_length=60,choices=TYPE_CHOICES,default='Blog')
    state = models.CharField(max_length=60,choices=STATE_CHOICES,default='raw')
    tags=TaggableManager()
    rating=RatingField(range=5)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)  # when first revision was created
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)  # when last revision was created (even if not published)
    published = models.DateTimeField(null=True, blank=True)  # when last published

    def __unicode__(self):
		return self.title

    class Meta:
        abstract=True

class MarkdownPost(Base):
    body = EpicEditorField()

class WYSIWYGPost(Base):
    body = tinymce_models.HTMLField()

class Event(models.Model):
    name = models.CharField(max_length=200)
    creator = models.ForeignKey(User,blank=True,null=True)
    body = tinymce_models.HTMLField()
    slug = models.SlugField(unique=True)
    state = models.CharField(max_length=60,choices=STATE_CHOICES,default='raw')
    tags=TaggableManager()
    rating=RatingField(range=5)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)  # when first revision was created
    published = models.DateTimeField(null=True, blank=True,editable=False)  # when last published
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField(blank=True, null=True)
    all_day_event = models.BooleanField(default=False)

    def get_absolute_update_url(self):
        url = reverse('admin:%s_%s_change' %(self._meta.app_label,  self._meta.module_name),  args=[self.id] )
        return url
    def __unicode__(self):
        date_format = '%Y-%m-%d %I:%M %p'
        if self.all_day_event:
            date_format = '%Y-%m-%d'
        return '%(n)s (%(d)s)' % {'n': self.name, 'd': self.start_date_time.strftime(date_format), }

    def active(self):
        if self.start_date_time and self.end_date_time:
            t = timezone.now()
            return self.start_date_time <= t and self.end_date_time >= t
        return False
    active.boolean = True