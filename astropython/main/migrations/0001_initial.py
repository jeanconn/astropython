# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('input_type', models.CharField(default=b'Markdown', help_text=b'All current editor contents will be lost once editors are switched', max_length=60, verbose_name=b'Text Editor Choice', choices=[(b'WYSIWYG', b'WYSIWYG'), (b'Markdown', b'Markdown')])),
                ('abstract', models.TextField(help_text=b'Optional Summary of Post', null=True, blank=True)),
                ('body', models.TextField(verbose_name=b'Page Body / Contents')),
                ('slug', models.SlugField(unique=True)),
                ('state', models.CharField(default=b'raw', max_length=60, choices=[(b'raw', b'raw'), (b'submitted', b'submitted')])),
                ('hits', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('authors', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('input_type', models.CharField(default=b'Markdown', help_text=b'All current editor contents will be lost once editors are switched', max_length=60, verbose_name=b'Text Editor Choice', choices=[(b'WYSIWYG', b'WYSIWYG'), (b'Markdown', b'Markdown')])),
                ('abstract', models.TextField(help_text=b'Optional Summary of Post', null=True, blank=True)),
                ('body', models.TextField(verbose_name=b'Page Body / Contents')),
                ('slug', models.SlugField(unique=True)),
                ('state', models.CharField(default=b'raw', max_length=60, choices=[(b'raw', b'raw'), (b'submitted', b'submitted')])),
                ('hits', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('authors', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=60)),
                ('email', models.URLField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EducationalResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('input_type', models.CharField(default=b'Markdown', help_text=b'All current editor contents will be lost once editors are switched', max_length=60, verbose_name=b'Text Editor Choice', choices=[(b'WYSIWYG', b'WYSIWYG'), (b'Markdown', b'Markdown')])),
                ('abstract', models.TextField(help_text=b'Optional Summary of Post', null=True, blank=True)),
                ('body', models.TextField(verbose_name=b'Page Body / Contents')),
                ('slug', models.SlugField(unique=True)),
                ('state', models.CharField(default=b'raw', max_length=60, choices=[(b'raw', b'raw'), (b'submitted', b'submitted')])),
                ('hits', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateTimeField(help_text=b'Format : YYYY-MM-DD', null=True, blank=True)),
                ('instructor_names', models.CharField(max_length=400)),
                ('website', models.URLField(verbose_name=b'Course Website', blank=True)),
                ('contents', models.TextField(verbose_name=b'Course Contents', blank=True)),
                ('background', models.TextField(verbose_name=b'Recommended Background', blank=True)),
                ('faq', models.TextField(verbose_name=b'Frequently Asked Questions', blank=True)),
                ('language', models.CharField(max_length=200, verbose_name=b'Language of Instruction', blank=True)),
                ('authors', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('input_type', models.CharField(default=b'Markdown', help_text=b'All current editor contents will be lost once editors are switched', max_length=60, verbose_name=b'Text Editor Choice', choices=[(b'WYSIWYG', b'WYSIWYG'), (b'Markdown', b'Markdown')])),
                ('body', models.TextField(verbose_name=b'Page Body / Contents')),
                ('location', models.CharField(max_length=1000, blank=True)),
                ('website', models.URLField(blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('state', models.CharField(default=b'raw', max_length=60, choices=[(b'raw', b'raw'), (b'submitted', b'submitted')])),
                ('hits', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('start_date_time', models.DateTimeField(help_text=b'Format : YYYY-MM-DD')),
                ('end_date_time', models.DateTimeField(help_text=b'Format : YYYY-MM-DD', null=True, blank=True)),
                ('all_day_event', models.BooleanField(default=False)),
                ('authors', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('input_type', models.CharField(default=b'Markdown', help_text=b'All current editor contents will be lost once editors are switched', max_length=60, verbose_name=b'Text Editor Choice', choices=[(b'WYSIWYG', b'WYSIWYG'), (b'Markdown', b'Markdown')])),
                ('abstract', models.TextField(help_text=b'Optional Summary of Post', null=True, blank=True)),
                ('body', models.TextField(verbose_name=b'Page Body / Contents')),
                ('slug', models.SlugField(unique=True)),
                ('state', models.CharField(default=b'raw', max_length=60, choices=[(b'raw', b'raw'), (b'submitted', b'submitted')])),
                ('hits', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('authors', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('input_type', models.CharField(default=b'Markdown', help_text=b'All current editor contents will be lost once editors are switched', max_length=60, verbose_name=b'Text Editor Choice', choices=[(b'WYSIWYG', b'WYSIWYG'), (b'Markdown', b'Markdown')])),
                ('abstract', models.TextField(help_text=b'Optional Summary of Post', null=True, blank=True)),
                ('body', models.TextField(verbose_name=b'Page Body / Contents')),
                ('slug', models.SlugField(unique=True)),
                ('state', models.CharField(default=b'raw', max_length=60, choices=[(b'raw', b'raw'), (b'submitted', b'submitted')])),
                ('hits', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(default=b'Others', help_text=b'Packages not actively mantained are labelled "Others"', max_length=60, choices=[(b'Recommended', b'Recommended'), (b'Others', b'Others')])),
                ('homepage', models.URLField(verbose_name=b'Homepage URL', blank=True)),
                ('docs', models.URLField(verbose_name=b'URL to Docs', blank=True)),
                ('authors', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('input_type', models.CharField(default=b'Markdown', help_text=b'All current editor contents will be lost once editors are switched', max_length=60, verbose_name=b'Text Editor Choice', choices=[(b'WYSIWYG', b'WYSIWYG'), (b'Markdown', b'Markdown')])),
                ('abstract', models.TextField(help_text=b'Optional Summary of Post', null=True, blank=True)),
                ('body', models.TextField(verbose_name=b'Page Body / Contents')),
                ('slug', models.SlugField(unique=True)),
                ('state', models.CharField(default=b'raw', max_length=60, choices=[(b'raw', b'raw'), (b'submitted', b'submitted')])),
                ('hits', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('authors', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('input_type', models.CharField(default=b'Markdown', help_text=b'All current editor contents will be lost once editors are switched', max_length=60, verbose_name=b'Text Editor Choice', choices=[(b'WYSIWYG', b'WYSIWYG'), (b'Markdown', b'Markdown')])),
                ('abstract', models.TextField(help_text=b'Optional Summary of Post', null=True, blank=True)),
                ('body', models.TextField(verbose_name=b'Page Body / Contents')),
                ('slug', models.SlugField(unique=True)),
                ('state', models.CharField(default=b'raw', max_length=60, choices=[(b'raw', b'raw'), (b'submitted', b'submitted')])),
                ('hits', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('authors', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Wiki',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('input_type', models.CharField(default=b'Markdown', help_text=b'All current editor contents will be lost once editors are switched', max_length=60, verbose_name=b'Text Editor Choice', choices=[(b'WYSIWYG', b'WYSIWYG'), (b'Markdown', b'Markdown')])),
                ('abstract', models.TextField(help_text=b'Optional Summary of Post', null=True, blank=True)),
                ('body', models.TextField(verbose_name=b'Page Body / Contents')),
                ('slug', models.SlugField(unique=True)),
                ('state', models.CharField(default=b'raw', max_length=60, choices=[(b'raw', b'raw'), (b'submitted', b'submitted')])),
                ('hits', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('authors', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
