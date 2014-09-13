# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierInformation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('company', models.CharField(max_length=100)),
                ('current_selling_method', models.CharField(max_length=100)),
                ('interest_listings', models.BooleanField(default=False)),
                ('interest_community', models.BooleanField(default=False)),
                ('interest_promotions', models.BooleanField(default=False)),
                ('interest_direct', models.BooleanField(default=False)),
                ('product_size', models.CharField(max_length=100)),
                ('referral_source', models.CharField(max_length=100, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
