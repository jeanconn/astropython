# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeTutorial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('desciption', models.TextField(null=True, blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('state', models.CharField(default=b'raw', max_length=60, choices=[(b'raw', b'raw'), (b'submitted', b'submitted'), (b'published', b'published'), (b'closed', b'closed')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('published', models.DateTimeField(null=True, editable=False, blank=True)),
                ('rating_votes', models.PositiveIntegerField(default=0, editable=False, blank=True)),
                ('rating_score', models.IntegerField(default=0, editable=False, blank=True)),
                ('body', models.TextField()),
                ('notes', models.TextField()),
                ('notes_html', models.TextField(editable=False)),
                ('authors', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
                ('categories', models.ManyToManyField(to='category.Category')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MarkdownTutorial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('desciption', models.TextField(null=True, blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('state', models.CharField(default=b'raw', max_length=60, choices=[(b'raw', b'raw'), (b'submitted', b'submitted'), (b'published', b'published'), (b'closed', b'closed')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('published', models.DateTimeField(null=True, editable=False, blank=True)),
                ('rating_votes', models.PositiveIntegerField(default=0, editable=False, blank=True)),
                ('rating_score', models.IntegerField(default=0, editable=False, blank=True)),
                ('body', models.TextField()),
                ('body_html', models.TextField(editable=False)),
                ('authors', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
                ('categories', models.ManyToManyField(to='category.Category')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TutorialSeries',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('desciption', models.TextField(null=True, blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('state', models.CharField(default=b'raw', max_length=60, choices=[(b'raw', b'raw'), (b'submitted', b'submitted'), (b'published', b'published'), (b'closed', b'closed')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('published', models.DateTimeField(null=True, editable=False, blank=True)),
                ('rating_votes', models.PositiveIntegerField(default=0, editable=False, blank=True)),
                ('rating_score', models.IntegerField(default=0, editable=False, blank=True)),
                ('authors', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
                ('categories', models.ManyToManyField(to='category.Category')),
                ('ctutorials', models.ManyToManyField(to='tutorials.CodeTutorial', null=True)),
                ('mtutorials', models.ManyToManyField(to='tutorials.MarkdownTutorial', null=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WYSIWYGTutorial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('desciption', models.TextField(null=True, blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('state', models.CharField(default=b'raw', max_length=60, choices=[(b'raw', b'raw'), (b'submitted', b'submitted'), (b'published', b'published'), (b'closed', b'closed')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('published', models.DateTimeField(null=True, editable=False, blank=True)),
                ('rating_votes', models.PositiveIntegerField(default=0, editable=False, blank=True)),
                ('rating_score', models.IntegerField(default=0, editable=False, blank=True)),
                ('body', tinymce.models.HTMLField()),
                ('authors', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
                ('categories', models.ManyToManyField(to='category.Category')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tutorialseries',
            name='wtutorials',
            field=models.ManyToManyField(to='tutorials.WYSIWYGTutorial', null=True),
            preserve_default=True,
        ),
    ]
