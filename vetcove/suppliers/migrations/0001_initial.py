# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('sku', models.CharField(blank=True, null=True, max_length=25)),
                ('quantity_available', models.IntegerField(max_length=8)),
                ('price', models.BigIntegerField(max_length=14)),
                ('short_date', models.BooleanField(default=False)),
                ('short_date_expiration', models.DateField(blank=True, null=True)),
                ('item', models.ForeignKey(to='products.Item')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('company_type', models.CharField(max_length=4, choices=[('manu', 'Manufacturer'), ('dist', 'Distributor'), ('comp', 'Compounding Pharmacy'), ('rsell', 'Reseller')])),
                ('sells_rx', models.BooleanField(default=False)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='inventory',
            name='supplier',
            field=models.ForeignKey(to='suppliers.Supplier'),
            preserve_default=True,
        ),
    ]
