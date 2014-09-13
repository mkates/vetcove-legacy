# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import accounts.models
import django.core.validators
import model_utils.fields
import imagekit.models.fields
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('suppliers', '0001_initial'),
        ('clinics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], verbose_name='username', max_length=30, unique=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')),
                ('first_name', models.CharField(verbose_name='first name', max_length=30, blank=True)),
                ('last_name', models.CharField(verbose_name='last name', max_length=30, blank=True)),
                ('email', models.EmailField(verbose_name='email address', max_length=75, blank=True)),
                ('is_staff', models.BooleanField(verbose_name='staff status', help_text='Designates whether the user can log into this admin site.', default=False)),
                ('is_active', models.BooleanField(verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('address_one', models.CharField(max_length=100)),
                ('address_two', models.CharField(null=True, max_length=100, blank=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(default='United States', max_length=50)),
                ('postalcode', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('name', models.CharField(null=True, max_length=60, blank=True)),
                ('phonenumber', models.IntegerField(max_length=15)),
                ('website', models.CharField(null=True, max_length=60, blank=True)),
                ('image', imagekit.models.fields.ProcessedImageField(null=True, blank=True, upload_to=accounts.models.create_group_path)),
                ('referrer_id', models.CharField(max_length=10)),
                ('balanceduri', models.CharField(null=True, max_length=255, blank=True)),
                ('credits', models.BigIntegerField(default=0, max_length=12)),
                ('verified', models.BooleanField(default=False)),
                ('group_type', models.CharField(choices=[('clinic', 'clinic'), ('supplier', 'supplier')], max_length=10)),
                ('address', models.ForeignKey(null=True, to='accounts.Address', related_name='main_address', blank=True)),
                ('administrator', models.ForeignKey(related_name='group_administrator', to=settings.AUTH_USER_MODEL)),
                ('clinic', models.OneToOneField(null=True, to='clinics.Clinic', blank=True)),
                ('referrer_user', models.ForeignKey(null=True, to='accounts.Group', blank=True)),
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
            field=models.ForeignKey(null=True, to='accounts.Group', related_name='address_group', blank=True),
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
            field=models.ManyToManyField(to='auth.Group', related_query_name='user', related_name='user_set', verbose_name='groups', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='basicuser',
            name='user_permissions',
            field=models.ManyToManyField(to='auth.Permission', related_query_name='user', related_name='user_set', verbose_name='user permissions', blank=True, help_text='Specific permissions for this user.'),
            preserve_default=True,
        ),
    ]
