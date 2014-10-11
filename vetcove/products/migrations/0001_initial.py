# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import products.models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('slug', models.SlugField()),
                ('name', models.TextField(max_length=200)),
                ('level', models.IntegerField(max_length=1, choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=1)),
                ('parents', models.ManyToManyField(to='products.Category', null=True, related_name='parents_rel_+', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('slug', models.SlugField()),
                ('name', models.TextField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('sku', models.CharField(null=True, max_length=25, blank=True)),
                ('quantity_available', models.IntegerField(max_length=8)),
                ('price', models.BigIntegerField(max_length=14)),
                ('short_date', models.BooleanField(default=False)),
                ('short_date_expiration', models.DateField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('slug', models.SlugField()),
                ('name', models.TextField(max_length=200)),
                ('manufacturer_no', models.CharField(null=True, max_length=25, blank=True)),
                ('description', models.CharField(max_length=300)),
                ('unit', models.CharField(max_length=100)),
                ('msrp_price', models.BigIntegerField(max_length=13)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('slug', models.SlugField()),
                ('name', models.TextField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('slug', models.SlugField()),
                ('name', models.TextField(max_length=200)),
                ('description', models.TextField()),
                ('is_rx', models.BooleanField(default=False)),
                ('is_compound', models.BooleanField(default=False)),
                ('low_price', models.BigIntegerField(max_length=13)),
                ('high_price', models.BigIntegerField(max_length=13)),
                ('rating', models.IntegerField(max_length=2, default=0)),
                ('discount', models.IntegerField(max_length=2)),
                ('available', models.BooleanField(default=False)),
                ('category', models.ForeignKey(to='products.Category')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('file', models.FileField(upload_to=products.models.file_path)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to=products.models.image_path, null=True, blank=True)),
                ('item', models.ForeignKey(null=True, blank=True, to='products.Item')),
                ('product', models.ForeignKey(to='products.Product', related_name='image_product')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('url', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=2, choices=[('yt', 'YouTube')], default='yt')),
                ('product', models.ForeignKey(to='products.Product')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('value', models.CharField(max_length=200)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TagClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('tag_type', models.CharField(max_length=3, choices=[('tex', 'text'), ('int', 'number')], default='tex')),
                ('searchable', models.BooleanField(default=True)),
                ('category', models.ManyToManyField(to='products.Category', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tag',
            name='tag_class',
            field=models.ForeignKey(to='products.TagClass'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='mainimage',
            field=models.ForeignKey(null=True, blank=True, to='products.ProductImage', related_name='product_mainimage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(to='products.Manufacturer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='image',
            field=models.ForeignKey(null=True, blank=True, to='products.ProductImage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='mainimage',
            field=models.ForeignKey(null=True, blank=True, to='products.ProductImage', related_name='item_mainimage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='product',
            field=models.ForeignKey(to='products.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inventory',
            name='item',
            field=models.ForeignKey(to='products.Item'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inventory',
            name='supplier',
            field=models.ForeignKey(to='accounts.Group'),
            preserve_default=True,
        ),
    ]
