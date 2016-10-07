from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'djog.views.index', name='index'),
    url(r'^login/', 'djog.views.login', name='login'),
    url(r'^logout/', 'djog.views.logout', name='logout'),
    url(r'^cart/', 'djog.views.cart', name='cart'),
    url(r'^register/', 'djog.views.register', name='register'),
    url(r'^details/', 'djog.views.details', name='details')
]
