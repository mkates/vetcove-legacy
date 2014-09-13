# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='telephone',
            field=models.BigIntegerField(blank=True, max_length=15, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='phonenumber',
            field=models.BigIntegerField(max_length=15),
        ),
    ]
