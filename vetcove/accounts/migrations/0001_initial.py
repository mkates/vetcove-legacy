# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import accounts.models
import django.core.validators
from django.conf import settings
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], max_length=30, unique=True)),
                ('first_name', models.CharField(verbose_name='first name', max_length=30, blank=True)),
                ('last_name', models.CharField(verbose_name='last name', max_length=30, blank=True)),
                ('email', models.EmailField(verbose_name='email address', max_length=75, blank=True)),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', verbose_name='staff status', default=False)),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address_one', models.CharField(help_text='Street Address, P.O. Box, Company Name c/o', verbose_name='Address Line 1', max_length=100)),
                ('address_two', models.CharField(verbose_name='Apartment, Suite, Unit, Building, Floor, etc.', max_length=100, blank=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=3, default='usa')),
                ('postalcode', models.CharField(verbose_name='Zipcode', max_length=6)),
                ('phone_number', models.BigIntegerField(verbose_name='Phone Number', max_length=15, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BuyingGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('slug', models.SlugField()),
                ('name', models.CharField(verbose_name='Company Name', max_length=100, blank=True)),
                ('contact_name', models.CharField(verbose_name='Primary Contact Name', max_length=100)),
                ('contact_position', models.CharField(verbose_name='Position of Primary Contact', max_length=100)),
                ('phone_number', models.BigIntegerField(verbose_name='Phone Number', max_length=15, null=True, blank=True)),
                ('website', models.CharField(max_length=60, blank=True)),
                ('logo', models.ImageField(upload_to=accounts.models.create_logo_path, null=True, blank=True)),
                ('referral_id', models.CharField(max_length=10)),
                ('balanceduri', models.CharField(null=True, max_length=255, blank=True)),
                ('signup_stage', models.PositiveIntegerField(default=1)),
                ('verified', models.BooleanField(default=False)),
                ('group_type', models.CharField(max_length=10, choices=[('clinic', 'clinic'), ('supplier', 'supplier')])),
                ('address', models.ForeignKey(to='accounts.Address', related_name='main_address')),
                ('administrator', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='group_administrator')),
                ('buying_groups', models.ManyToManyField(to='accounts.BuyingGroup', null=True, blank=True)),
                ('clinic', models.OneToOneField(null=True, blank=True, to='clinics.Clinic')),
                ('referred_by', models.ForeignKey(null=True, blank=True, to='accounts.Group')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
