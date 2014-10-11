from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('core',
    url(r'^all/', views.Review.as_view(),name='review'),
    url(r'^write/', views.WriteReview.as_view(),name='write-review'),
)
