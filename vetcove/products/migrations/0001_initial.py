# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone
import core.models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=100)),
                ('level', models.IntegerField(default=1, max_length=1)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('photo', imagekit.models.fields.ProcessedImageField(upload_to=core.models.get_file_path_original)),
                ('photo_small', imagekit.models.fields.ProcessedImageField(upload_to=core.models.get_file_path_small)),
                ('photo_medium', imagekit.models.fields.ProcessedImageField(upload_to=core.models.get_file_path_medium)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=100)),
                ('manufacturer_no', models.CharField(blank=True, null=True, max_length=25)),
                ('description', models.TextField()),
                ('msrp_price', models.BigIntegerField(max_length=13)),
                ('purchases', models.IntegerField(default=0)),
                ('itemimage', models.ForeignKey(null=True, to='products.Image', blank=True, related_name='itemimage')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('image', models.ForeignKey(null=True, to='products.Image', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('views', models.IntegerField(default=0)),
                ('category', models.ForeignKey(to='products.Category')),
                ('mainimage', models.ForeignKey(null=True, to='products.Image', blank=True)),
                ('manufacturer', models.ForeignKey(to='products.Manufacturer')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('key', models.CharField(max_length=20, choices=[('rx', 'rx'), ('compendium', 'compendium'), ('length', 'length'), ('wound_support', 'wound_support'), ('colors', 'colors'), ('year', 'year'), ('contract', 'contract')])),
                ('value', models.CharField(max_length=100)),
                ('products', models.ManyToManyField(to='products.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='item',
            name='product',
            field=models.ForeignKey(to='products.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='item',
            field=models.ForeignKey(to='products.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='industry',
            field=models.ManyToManyField(to='products.Industry'),
            preserve_default=True,
        ),
    ]
