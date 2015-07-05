# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_feed_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='title',
            field=models.CharField(default='AstroPython (Old)', max_length=120),
            preserve_default=False,
        ),
    ]
