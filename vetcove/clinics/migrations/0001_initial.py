# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import clinics.models
import model_utils.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('first_name', models.CharField(max_length=60)),
                ('middle_initial', models.CharField(blank=True, null=True, max_length=1)),
                ('last_name', models.CharField(max_length=60)),
                ('license_state', models.CharField(max_length=2)),
                ('license_image', models.FileField(blank=True, upload_to=clinics.models.create_license_path, null=True)),
                ('license_no', models.CharField(blank=True, null=True, max_length=60)),
                ('license_expiration', models.DateField(blank=True, null=True)),
                ('salesexemption_no', models.CharField(blank=True, max_length=60)),
                ('salesexemption', models.FileField(blank=True, upload_to=clinics.models.create_sales_exempt_path, null=True)),
                ('number_of_vets', models.PositiveIntegerField(default=1)),
                ('practice_type', models.CharField(default='o', max_length=3, choices=[('sae', 'Small Animal Exclusive'), ('msa', 'Mixed, Mostly Small Animal'), ('mla', 'Mixed, Mostly Large Animal'), ('lae', 'Large Animal Exclusive'), ('e', 'Equine'), ('p', 'Porcine'), ('f', 'Feline'), ('b', 'Bovine'), ('gov', 'Government'), ('ri', 'Research Institution'), ('ti', 'Teaching Institution'), ('o', 'Other')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GPO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('clinics', models.ManyToManyField(to='clinics.Clinic')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
