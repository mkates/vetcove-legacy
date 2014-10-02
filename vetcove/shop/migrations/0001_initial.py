# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('quantity', models.IntegerField(default=1, max_length=4)),
                ('address', models.ForeignKey(to='accounts.Address')),
                ('group', models.ForeignKey(to='accounts.Group')),
                ('inventory', models.ForeignKey(to='suppliers.Inventory')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
