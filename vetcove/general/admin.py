from __future__ import absolute_import

from django.contrib import admin

# Register your models here.
from .models import *


class ClinicLeadAdmin(admin.ModelAdmin):
	list_display = ['clinic_name','zipcode','state','practice_type','number_of_licensed_veterinarians',
		'total_employees','clinic_website','your_name','your_position','your_email','phone_number',
		'placing_orders','authorized','feature_sales','feature_support','feature_analytics','feature_invoicing',
		'feature_webpresence','beta_user','howdidyouhear']

class SupplierLeadAdmin(admin.ModelAdmin):
	list_display = ['company','company_type','company_size','feature_sales','feature_support','feature_analytics',
	'feature_invoicing','feature_webpresence','name','position','email','phonenumber','sell_method','selldirect',
	'managing_presence','authorized','next_steps','howdidyouhear']

admin.site.register(ClinicLead,ClinicLeadAdmin)
admin.site.register(SupplierLead,SupplierLeadAdmin)
