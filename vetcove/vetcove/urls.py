from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vetcove.views.home', name='home'),
    # url(r'^blog/', include('blog.urls'')),
    # https://docs.djangoproject.com/en/dev/topics/http/urls/


    url(r'^admin/', include(admin.site.urls)),

    # All general URLS (corporate)
    url(r'^', include('general.urls')),
    
    url(r'^clinics/', include('clinics.urls',namespace='clinics')),
    url(r'^emails/', include('emails.urls',namespace='emails')),
    url(r'^news/', include('news.urls',namespace='news')),
    url(r'^notifications/', include('notifications.urls',namespace='notifications')),
    url(r'^payments/', include('payments.urls',namespace='payments')),
    url(r'^products/', include('products.urls',namespace='products')),
    url(r'^questions/', include('questions.urls',namespace='questions')),
    url(r'^recommendations/', include('recommendations.urls',namespace='recommendations')),
    url(r'^reports/', include('reports.urls',namespace='reports')),
    url(r'^reviews/', include('reviews.urls',namespace='reviews')),
    url(r'^rewards/', include('rewards.urls',namespace='rewards')),
    url(r'^search/', include('search.urls',namespace='search')),
    url(r'^shop/', include('shop.urls',namespace='shop')),
    url(r'^staff/', include('staff.urls',namespace='staff')),
    url(r'^suppliers/', include('suppliers.urls',namespace='suppliers'))
)
