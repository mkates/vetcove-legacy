from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',

	### Index ###
    url(r'^$', views.Index.as_view(),name='index'),

    ### Company ###
    url(r'^company/about/', views.About.as_view(),name='about'),
    url(r'^company/careers/', views.Careers.as_view(),name='careers'),
    url(r'^company/presskit/', views.PressKit.as_view(),name='presskit'),
    url(r'^company/feedback/', views.Feedback.as_view(),name='feedback'),
    url(r'^company/', views.Company.as_view(),name='company'),

    ### Legal ###
    url(r'^legal/overview/', views.GeneralPolicy.as_view(),name='generalpolicy'),
    url(r'^legal/privacy/', views.PrivacyPolicy.as_view(),name='privacypolicy'),
    url(r'^legal/tos/', views.TermsOfService.as_view(),name='termsofservice'),
    url(r'^legal/seller/', views.SellerAgreement.as_view(),name='selleragreement'),

    ### Support ###
    url(r'^support/', views.Support.as_view(),name='support'),
    url(r'^faq/', views.FAQ.as_view(), name='faq'),

   	### Explore ###
    url(r'^explore/features/', views.Features.as_view(),name='features'),
    url(r'^explore/suppliers/', views.Suppliers.as_view(),name='suppliers'),
    url(r'^explore/dashboard/', views.Dashboard.as_view(),name='dashboard'),
    url(r'^lead/', views.Lead.as_view(),name='lead'),
   
)
