# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicLead',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('clinic_name', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=5)),
                ('state', models.CharField(max_length=30)),
                ('practice_type', models.CharField(max_length=50, choices=[('small_animal_exclusive', 'Small Animal Exclusive'), ('small_animal_predominant', 'Small Animal Predominant'), ('large animal predominant', 'Large Animal Predominant'), ('large_animal_exclusive', 'Large Animal Exclusive'), ('equine_exclusive', 'Equine Exclusive'), ('equine_predominant', 'Equine Predominant'), ('other', 'Other')])),
                ('number_of_licensed_veterinarians', models.IntegerField(max_length=3)),
                ('total_employees', models.IntegerField(max_length=3)),
                ('clinic_website', models.CharField(null=True, max_length=30, blank=True)),
                ('your_name', models.CharField(max_length=100)),
                ('your_position', models.CharField(null=True, max_length=100, blank=True)),
                ('your_email', models.CharField(max_length=200)),
                ('phone_number', models.CharField(null=True, max_length=25, blank=True)),
                ('placing_orders', models.BooleanField(default=False)),
                ('authorized', models.BooleanField(default=False)),
                ('feature_sales', models.BooleanField(default=False)),
                ('feature_support', models.BooleanField(default=False)),
                ('feature_analytics', models.BooleanField(default=False)),
                ('feature_invoicing', models.BooleanField(default=False)),
                ('feature_webpresence', models.BooleanField(default=False)),
                ('beta_user', models.BooleanField(default=False)),
                ('howdidyouhear', models.CharField(max_length=20, choices=[('conference', 'Conference'), ('personal referral', 'Personal Referral'), ('website', 'Website'), ('email', 'Email'), ('other', 'Other')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SupplierLead',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('company', models.CharField(max_length=100)),
                ('company_type', models.CharField(max_length=25, choices=[('manufacturer', 'Manufacturer'), ('distributor', 'Distributor'), ('compounding pharmacy', 'Compounding Pharmacy'), ('reseller', 'Reseller')])),
                ('company_size', models.CharField(max_length=100, choices=[('< 5', '< 5 employees'), ('5-10', '5-9 employees'), ('10-20', '10-20 employees'), ('21-50', '21-50 employees'), ('51-100', '51-100 employees'), ('101-500', '101-500 employees'), ('500+', '500+ employees')])),
                ('feature_sales', models.BooleanField(default=False)),
                ('feature_support', models.BooleanField(default=False)),
                ('feature_analytics', models.BooleanField(default=False)),
                ('feature_invoicing', models.BooleanField(default=False)),
                ('feature_webpresence', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(null=True, max_length=100, blank=True)),
                ('sell_method', models.CharField(max_length=30, choices=[('exclusive_distribution', 'Exclusively through distribution'), ('predominant_distribution', 'Predominantly through distribution'), ('mixed', 'Mixed between distribution and direct to vets'), ('predominant_direct', 'Predominantly direct to vets'), ('exclusive_direct', 'Exclusively direct to vets')])),
                ('selldirect', models.BooleanField(default=False)),
                ('managing_presence', models.BooleanField(default=None)),
                ('authorized', models.BooleanField(default=None)),
                ('next_steps', models.CharField(max_length=100, choices=[('betauser', "Beta User: We'd like first access to Vetcove as a beta user"), ('confirmed', 'Confirmed: We Plan to begin using Vetcove once the site is live'), ('undecided', 'Undecided: Speak with us to learn more between now and launch day')])),
                ('howdidyouhear', models.CharField(null=True, choices=[('conference', 'Conference'), ('personal_referral', 'Personal Referral'), ('google', 'Google'), ('emailmarketing', 'Email Marketing')], max_length=200, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
