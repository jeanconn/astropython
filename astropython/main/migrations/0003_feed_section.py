# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_feed'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='section',
            field=models.CharField(default=b'blog', max_length=60, choices=[(b'tutorials', b'Tutorials'), (b'snippets', b'Code Snippets'), (b'education', b'Educational Resources'), (b'wiki', b'Wiki Pages'), (b'announcements', b'Announcements'), (b'news', b'News'), (b'blog', b'Blog'), (b'packages', b'Packages'), (b'events', b'Events')]),
        ),
    ]
