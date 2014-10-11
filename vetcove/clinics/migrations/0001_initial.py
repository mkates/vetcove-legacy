# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import clinics.models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('first_name', models.CharField(verbose_name='First Name', max_length=60)),
                ('middle_initial', models.CharField(verbose_name='M.I.', max_length=1, blank=True)),
                ('last_name', models.CharField(verbose_name='Last Name', max_length=60)),
                ('license_state', models.CharField(verbose_name='State of License', max_length=2)),
                ('license_image', models.FileField(upload_to=clinics.models.create_license_path, blank=True)),
                ('license_no', models.CharField(verbose_name='Veterinary License Number', max_length=60)),
                ('license_expiration', models.DateField(verbose_name='License Expiration Date')),
                ('number_of_vets', models.PositiveIntegerField(verbose_name='Number of veterinarians in the clinic', default=1)),
                ('practice_type', models.CharField(verbose_name='Practice Type', choices=[('sae', 'Small Animal Exclusive'), ('msa', 'Mixed, Mostly Small Animal'), ('mla', 'Mixed, Mostly Large Animal'), ('lae', 'Large Animal Exclusive'), ('e', 'Equine'), ('p', 'Porcine'), ('f', 'Feline'), ('b', 'Bovine'), ('gov', 'Government'), ('ri', 'Research Institution'), ('ti', 'Teaching Institution'), ('o', 'Other')], max_length=3, default='o')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GPO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('clinics', models.ManyToManyField(to='clinics.Clinic')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SalesExemption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('approved', models.BooleanField(default=False)),
                ('full_exempt', models.BooleanField(default=False)),
                ('sales_exemption_number', models.CharField(max_length=100)),
                ('clinic', models.ForeignKey(to='clinics.Clinic')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
