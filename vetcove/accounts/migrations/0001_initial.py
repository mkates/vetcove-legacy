# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import accounts.models
from django.conf import settings
import django.core.validators
import django.utils.timezone
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0001_initial'),
        ('suppliers', '0001_initial'),
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(verbose_name='username', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')),
                ('first_name', models.CharField(verbose_name='first name', blank=True, max_length=30)),
                ('last_name', models.CharField(verbose_name='last name', blank=True, max_length=30)),
                ('email', models.EmailField(verbose_name='email address', blank=True, max_length=75)),
                ('is_staff', models.BooleanField(verbose_name='staff status', default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(verbose_name='active', default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('address_one', models.CharField(max_length=100)),
                ('address_two', models.CharField(blank=True, null=True, max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(default='United States', max_length=50)),
                ('postalcode', models.CharField(max_length=10)),
                ('phone_number', models.BigIntegerField(blank=True, null=True, max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('name', models.CharField(blank=True, null=True, max_length=60)),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_position', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, null=True, max_length=150)),
                ('phone_number', models.BigIntegerField(blank=True, null=True, max_length=15)),
                ('website', models.CharField(blank=True, null=True, max_length=60)),
                ('logo', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=accounts.models.create_logo_path, null=True)),
                ('referral_id', models.CharField(max_length=10)),
                ('balanceduri', models.CharField(blank=True, null=True, max_length=255)),
                ('signup_stage', models.PositiveIntegerField(default=1)),
                ('verified', models.BooleanField(default=False)),
                ('group_type', models.CharField(max_length=10, choices=[('clinic', 'clinic'), ('supplier', 'supplier')])),
                ('address', models.ForeignKey(null=True, to='accounts.Address', blank=True, related_name='main_address')),
                ('administrator', models.ForeignKey(related_name='group_administrator', to=settings.AUTH_USER_MODEL)),
                ('clinic', models.OneToOneField(null=True, to='clinics.Clinic', blank=True)),
                ('referred_by', models.ForeignKey(null=True, to='accounts.Group', blank=True)),
                ('supplier', models.OneToOneField(null=True, to='suppliers.Supplier', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='address',
            name='group',
            field=models.ForeignKey(null=True, to='accounts.Group', blank=True, related_name='address_group'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='basicuser',
            name='group',
            field=models.ForeignKey(null=True, to='accounts.Group', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='basicuser',
            name='groups',
            field=models.ManyToManyField(blank=True, related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', to='auth.Group', verbose_name='groups', related_name='user_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='basicuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_query_name='user', help_text='Specific permissions for this user.', to='auth.Permission', verbose_name='user permissions', related_name='user_set'),
            preserve_default=True,
        ),
    ]
