# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import re
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('spirit', '0006_auto_20150327_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'Enter a valid username.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters', unique=True, verbose_name='username', db_index=True),
            preserve_default=True,
        ),
    ]
