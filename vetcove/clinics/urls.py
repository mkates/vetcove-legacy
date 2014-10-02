from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',

	### New clinic sign up procedure
    url(r'^newclinic/basics', views.NewClinicBasics.as_view(),name='new_clinic_basics'),
    url(r'^newclinic/verify', views.NewClinicVerify.as_view(),name='new_clinic_verify'),
    url(r'^newclinic/tos', views.NewClinicTOS.as_view(),name='new_clinic_tos'),
    url(r'^newclinic/complete', views.NewClinicComplete.as_view(),name='new_clinic_complete'),

    ### Sales Exemption Form
    url(r'^salesexempt', views.SalesExempt.as_view(),name='sales_exempt'),
)
