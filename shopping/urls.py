from django.conf.urls import url, patterns
from shopping.views import add, remove


urlpatterns = patterns('shopping.views',
    url(r'^add/(?P<id>[0-9]+)$', add, name='shopping-cart-add'),
    url(r'^remove/(?P<id>[0-9]+)$', remove, name='shopping-cart-remove'),
    url(r'^show/$', 'show', name='shopping-cart-show'),
)

