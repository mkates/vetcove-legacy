# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20141002_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='image',
            name='photo_medium',
        ),
        migrations.RemoveField(
            model_name='image',
            name='photo_small',
        ),
    ]
