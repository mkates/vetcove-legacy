# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
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
