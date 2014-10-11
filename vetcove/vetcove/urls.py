from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vetcove.views.home', name='home'),
    # url(r'^blog/', include('blog.urls'')),
    # https://docs.djangoproject.com/en/dev/topics/http/urls/

    url(r'^admin/', include(admin.site.urls)),

    ### General URLS (takes the namespaces of company,legal,and explore)
    url(r'^', include('general.urls',namespace='general')),

    ### All activity related to accounts (signin,singout,password,etc.)
    url(r'^', include('accounts.urls',namespace='accounts')),
    
    ### Products, which owns the following namespaces: product,category,manufacturer,company ###
    url(r'^', include('products.urls',namespace='products')),

    url(r'^clinics/', include('clinics.urls',namespace='clinics')),
    url(r'^emails/', include('emails.urls',namespace='emails')),
    url(r'^news/', include('news.urls',namespace='news')),
    url(r'^notifications/', include('notifications.urls',namespace='notifications')),
    url(r'^payments/', include('payments.urls',namespace='payments')),
    url(r'^questions/', include('questions.urls',namespace='questions')),
    url(r'^recommendations/', include('recommendations.urls',namespace='recommendations')),
    url(r'^reports/', include('reports.urls',namespace='reports')),
    url(r'^reviews/', include('reviews.urls',namespace='reviews')),
    url(r'^rewards/', include('rewards.urls',namespace='rewards')),
    url(r'^shop/', include('shop.urls',namespace='shop')),
    url(r'^staff/', include('staff.urls',namespace='staff')),
    url(r'^suppliers/', include('suppliers.urls',namespace='suppliers'))


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
The last line static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
is used to serve user uploaded media files in development, as specified in the
official django docs
'''
