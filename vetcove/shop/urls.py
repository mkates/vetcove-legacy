from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('shop',
    url(r'orderhistory', views.OrderHistory.as_view(),name='orderhistory')
)
