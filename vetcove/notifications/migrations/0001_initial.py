# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('viewed', models.BooleanField(default=False)),
                ('type', models.CharField(max_length=20, choices=[('referral', 'referral')])),
                ('text', models.TextField()),
                ('group', models.ForeignKey(to='accounts.Group')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
