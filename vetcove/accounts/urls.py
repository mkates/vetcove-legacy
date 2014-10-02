from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^signin/', views.SignIn.as_view(),name='signin'),
    url(r'^signup/', views.SignUp.as_view(),name='signup'),
    url(r'^password/', views.Password.as_view(),name='password'),
)
