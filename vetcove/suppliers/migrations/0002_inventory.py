# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now)),
                ('sku', models.CharField(blank=True, max_length=25, null=True)),
                ('quantity_available', models.IntegerField(max_length=8)),
                ('price', models.BigIntegerField(max_length=14)),
                ('item', models.ForeignKey(to='products.Item')),
                ('supplier', models.ForeignKey(to='suppliers.Supplier')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
