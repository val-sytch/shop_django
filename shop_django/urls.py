from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('djog.urls')),
    url(r'^shopping-cart/', include('shopping.urls', namespace="cart")),
]
