from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^order/', views.order, name='order'),
    url(r'^order_make/', views.order_make, name='order_make'),
    url(r'^register/', views.register, name='register'),
    url(r'^details/(?P<id>[^/]+)', views.details, name='details')
]