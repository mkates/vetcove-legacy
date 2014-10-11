from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r'^product/test', views.Test.as_view(),name='test'),
    # Product
    url(r'^product/product', views.Product.as_view(),name='product'),
)
