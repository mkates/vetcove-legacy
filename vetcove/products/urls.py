from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r'^test', views.Test.as_view(),name='test'),
)
