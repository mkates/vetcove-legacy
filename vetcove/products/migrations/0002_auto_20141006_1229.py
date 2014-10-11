# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=0, max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='high_price',
            field=models.BigIntegerField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='low_price',
            field=models.BigIntegerField(blank=True, max_length=13, null=True),
        ),
    ]
