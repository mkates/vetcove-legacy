from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
   
	### New supplier sign up procedure
    url(r'^newsupplier/basics', views.NewSupplierBasics.as_view(),name='new_supplier_basics'),
    url(r'^newsupplier/contact', views.NewSupplierContact.as_view(),name='new_supplier_contact'),
    url(r'^newsupplier/tos', views.NewSupplierTOS.as_view(),name='new_supplier_tos'),
    url(r'^newsupplier/complete', views.NewSupplierComplete.as_view(),name='new_supplier_complete'),

)
