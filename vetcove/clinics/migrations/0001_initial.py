# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import clinics.models
import django.utils.timezone
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('practitioner_name', models.CharField(max_length=60)),
                ('license_no', models.CharField(null=True, max_length=60, blank=True)),
                ('state', models.CharField(max_length=60)),
                ('license', imagekit.models.fields.ProcessedImageField(null=True, blank=True, upload_to=clinics.models.create_license_path)),
                ('license_expiration', models.DateField(null=True, blank=True)),
                ('salesexemption_no', models.CharField(max_length=60, blank=True)),
                ('salesexemption', models.FileField(null=True, blank=True, upload_to=clinics.models.create_salesexemption_path)),
                ('organization_type', models.CharField(max_length=100)),
                ('number_of_vets', models.PositiveIntegerField(default=1)),
                ('practice_size', models.PositiveIntegerField(default=1)),
                ('practice_type', models.CharField(default='', choices=[('small_animal', 'Small Animal'), ('large_animal', 'Large Animal'), ('mixed', 'Mixed')], max_length=60)),
                ('tos', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GPO',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('clinics', models.ManyToManyField(to='clinics.Clinic')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
