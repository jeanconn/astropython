from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.sites.models import Site

class Category(models.Model):
    """
    Category model to be used for categorization of content. Categories are
    high level constructs to be used for grouping and organizing content,
    thus creating a site's table of contents.
    """
    title = models.CharField(
        max_length=200,
        help_text='Short descriptive name for this category.',
    )
    subtitle = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default='',
        help_text='Some titles may be the same and cause confusion in admin '
                  'UI. A subtitle makes a distinction.',
    )
    slug = models.SlugField(
        max_length=255,
        db_index=True,
        unique=True,
        help_text='Short descriptive unique name for use in urls.',
    )
    parent = models.ForeignKey('self', null=True, blank=True)
    sites = models.ManyToManyField('sites.Site',
        blank=True,
        null=True,
        help_text='Limits category scope to selected sites.',
    )

    def __unicode__(self):
        if self.subtitle:
            return '%s - %s' % (self.title, self.subtitle)
        else:
            return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        # Raise on circular reference
        parent = self.parent
        while parent is not None:
            if parent == self:
                raise RuntimeError, "Circular references not allowed"
            parent = parent.parent

        super(Category, self).save(*args, **kwargs)

    @property
    def children(self):
        return self.category_set.all().order_by('title')

    def get_absolute_url(self):
        return reverse('category_object_list', kwargs={'category_slug': self.slug})