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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('clinic_name', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=5)),
                ('state', models.CharField(max_length=2)),
                ('practice_type', models.CharField(choices=[('small_animal_exclusive', 'Small Animal Exclusive'), ('small_animal_predominant', 'Small Animal Predominant'), ('large animal predominant', 'Large Animal Predominant'), ('large_animal_exclusive', 'Large Animal Exclusive'), ('equine_exclusive', 'Equine Exclusive'), ('equine_predominant', 'Equine Predominant'), ('other', 'Other')], max_length=50)),
                ('number_of_licensed_veterinarians', models.IntegerField(max_length=3)),
                ('total_employees', models.IntegerField(max_length=3)),
                ('clinic_website', models.CharField(blank=True, null=True, max_length=30)),
                ('your_name', models.CharField(max_length=100)),
                ('your_position', models.CharField(blank=True, null=True, max_length=100)),
                ('your_email', models.CharField(max_length=200)),
                ('phone_number', models.CharField(blank=True, null=True, max_length=25)),
                ('placing_orders', models.BooleanField(default=False)),
                ('authorized', models.BooleanField(default=False)),
                ('feature_sales', models.BooleanField(default=False)),
                ('feature_support', models.BooleanField(default=False)),
                ('feature_analytics', models.BooleanField(default=False)),
                ('feature_invoicing', models.BooleanField(default=False)),
                ('feature_webpresence', models.BooleanField(default=False)),
                ('beta_user', models.BooleanField(default=False)),
                ('howdidyouhear', models.CharField(choices=[('conference', 'Conference'), ('personal referral', 'Personal Referral'), ('website', 'Website'), ('email', 'Email'), ('other', 'Other')], max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SupplierLead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('company', models.CharField(max_length=100)),
                ('company_type', models.CharField(choices=[('manufacturer', 'Manufacturer'), ('distributor', 'Distributor'), ('compounding pharmacy', 'Compounding Pharmacy'), ('reseller', 'Reseller')], max_length=25)),
                ('company_size', models.CharField(choices=[('< 5', '< 5 employees'), ('5-10', '5-9 employees'), ('10-20', '10-20 employees'), ('21-50', '21-50 employees'), ('51-100', '51-100 employees'), ('101-500', '101-500 employees'), ('500+', '500+ employees')], max_length=100)),
                ('feature_sales', models.BooleanField(default=False)),
                ('feature_support', models.BooleanField(default=False)),
                ('feature_analytics', models.BooleanField(default=False)),
                ('feature_invoicing', models.BooleanField(default=False)),
                ('feature_webpresence', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(blank=True, null=True, max_length=100)),
                ('sell_method', models.CharField(choices=[('exclusive_distribution', 'Exclusively through distribution'), ('predominant_distribution', 'Predominantly through distribution'), ('mixed', 'Mixed between distribution and direct to vets'), ('predominant_direct', 'Predominantly direct to vets'), ('exclusive_direct', 'Exclusively direct to vets')], max_length=30)),
                ('selldirect', models.BooleanField(default=False)),
                ('managing_presence', models.BooleanField(default=None)),
                ('authorized', models.BooleanField(default=None)),
                ('next_steps', models.CharField(choices=[('betauser', "Beta User: We'd like first access to Vetcove as a beta user"), ('confirmed', 'Confirmed: We Plan to begin using Vetcove once the site is live'), ('undecided', 'Undecided: Speak with us to learn more between now and launch day')], max_length=100)),
                ('howdidyouhear', models.CharField(blank=True, choices=[('conference', 'Conference'), ('personal_referral', 'Personal Referral'), ('google', 'Google'), ('emailmarketing', 'Email Marketing')], null=True, max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
