# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20141002_1719'),
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='manufacturer',
            field=models.ManyToManyField(to='products.Manufacturer'),
            preserve_default=True,
        ),
    ]
