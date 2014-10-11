# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('suppliers', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='supplier',
            field=models.OneToOneField(null=True, blank=True, to='suppliers.Supplier'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='group',
            field=models.ForeignKey(null=True, blank=True, to='accounts.Group', related_name='address_group'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='basicuser',
            name='group',
            field=models.ForeignKey(null=True, blank=True, to='accounts.Group'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='basicuser',
            name='groups',
            field=models.ManyToManyField(to='auth.Group', verbose_name='groups', related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', blank=True, related_query_name='user'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='basicuser',
            name='user_permissions',
            field=models.ManyToManyField(to='auth.Permission', verbose_name='user permissions', related_name='user_set', help_text='Specific permissions for this user.', blank=True, related_query_name='user'),
            preserve_default=True,
        ),
    ]
