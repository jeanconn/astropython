# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import tinymce.models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('body', tinymce.models.HTMLField()),
                ('slug', models.SlugField(unique=True)),
                ('state', models.CharField(default=b'raw', max_length=60, choices=[(b'raw', b'raw'), (b'submitted', b'submitted'), (b'published', b'published'), (b'closed', b'closed')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('published', models.DateTimeField(null=True, editable=False, blank=True)),
                ('start_date_time', models.DateTimeField()),
                ('end_date_time', models.DateTimeField(null=True, blank=True)),
                ('all_day_event', models.BooleanField(default=False)),
                ('rating_votes', models.PositiveIntegerField(default=0, editable=False, blank=True)),
                ('rating_score', models.IntegerField(default=0, editable=False, blank=True)),
                ('creator', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MarkdownPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('desciption', models.TextField(null=True, blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('post_type', models.CharField(default=b'Blog', max_length=60, choices=[(b'ANNOUNCEMENTS', b'Announcements'), (b'NEWS', b'News'), (b'GENERAL_BLOG', b'Blog')])),
                ('state', models.CharField(default=b'raw', max_length=60, choices=[(b'raw', b'raw'), (b'submitted', b'submitted'), (b'published', b'published'), (b'closed', b'closed')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('published', models.DateTimeField(null=True, editable=False, blank=True)),
                ('rating_votes', models.PositiveIntegerField(default=0, editable=False, blank=True)),
                ('rating_score', models.IntegerField(default=0, editable=False, blank=True)),
                ('body', models.TextField()),
                ('body_html', models.TextField(editable=False)),
                ('authors', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('categories', models.ManyToManyField(to='category.Category')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WYSIWYGPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('desciption', models.TextField(null=True, blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('post_type', models.CharField(default=b'Blog', max_length=60, choices=[(b'ANNOUNCEMENTS', b'Announcements'), (b'NEWS', b'News'), (b'GENERAL_BLOG', b'Blog')])),
                ('state', models.CharField(default=b'raw', max_length=60, choices=[(b'raw', b'raw'), (b'submitted', b'submitted'), (b'published', b'published'), (b'closed', b'closed')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('published', models.DateTimeField(null=True, editable=False, blank=True)),
                ('rating_votes', models.PositiveIntegerField(default=0, editable=False, blank=True)),
                ('rating_score', models.IntegerField(default=0, editable=False, blank=True)),
                ('body', tinymce.models.HTMLField()),
                ('authors', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('categories', models.ManyToManyField(to='category.Category')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
