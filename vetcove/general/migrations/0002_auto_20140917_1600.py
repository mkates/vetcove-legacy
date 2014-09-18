# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierLead',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('company', models.CharField(max_length=100)),
                ('current_selling_method', models.CharField(max_length=100)),
                ('interest_listings', models.BooleanField(default=False)),
                ('interest_community', models.BooleanField(default=False)),
                ('interest_promotions', models.BooleanField(default=False)),
                ('interest_direct', models.BooleanField(default=False)),
                ('product_size', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='SupplierInformation',
        ),
    ]
