# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20140912_1520'),
        ('suppliers', '0002_inventory'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now)),
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
