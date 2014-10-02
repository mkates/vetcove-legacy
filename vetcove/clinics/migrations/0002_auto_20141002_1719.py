# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesExemption',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
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
        migrations.RemoveField(
            model_name='clinic',
            name='salesexemption',
        ),
        migrations.RemoveField(
            model_name='clinic',
            name='salesexemption_no',
        ),
    ]
