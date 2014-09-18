from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('core',
    url(r'^signin/', views.SignIn.as_view(),name='signin'),
    url(r'^password/', views.Password.as_view(),name='password'),
)
