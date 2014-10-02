# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='products',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
        migrations.RemoveField(
            model_name='category',
            name='industry',
        ),
        migrations.RemoveField(
            model_name='item',
            name='itemimage',
        ),
        migrations.RemoveField(
            model_name='item',
            name='purchases',
        ),
        migrations.RemoveField(
            model_name='product',
            name='views',
        ),
        migrations.AddField(
            model_name='category',
            name='parents',
            field=models.ForeignKey(blank=True, to='products.Category', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='original',
            field=models.ImageField(blank=True, upload_to='product', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(blank=True, to='products.Product', null=True, related_name='image_product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='mainimage',
            field=models.ForeignKey(blank=True, to='products.Image', null=True, related_name='item_mainimage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='unit',
            field=models.CharField(max_length=100, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='level',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], max_length=1, default=1),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='image',
            name='item',
            field=models.ForeignKey(blank=True, to='products.Item', null=True),
        ),
        migrations.AlterField(
            model_name='industry',
            name='name',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='mainimage',
            field=models.ForeignKey(blank=True, to='products.Image', null=True, related_name='product_mainimage'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.TextField(max_length=200),
        ),
    ]
