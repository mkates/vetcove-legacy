# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('seller_type', models.CharField(max_length=4, choices=[('manu', 'Manufacturer'), ('dist', 'Distributor'), ('comp', 'Compounding Pharmacy'), ('rsell', 'Reseller')])),
                ('sells_rx', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('manufacturer', models.ManyToManyField(to='products.Manufacturer')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
