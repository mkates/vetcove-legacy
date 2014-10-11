from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('shop',
    url(r'orderhistory', views.OrderHistory.as_view(),name='orderhistory'),
    url(r'cart', views.Cart.as_view(),name='cart'),
    url(r'checkout/shipping', views.CheckoutShipping.as_view(),name='checkout-shipping'),
    url(r'checkout/billing', views.CheckoutBilling.as_view(),name='checkout-billing'),
    url(r'checkout/review', views.CheckoutReview.as_view(),name='checkout-review')
)
