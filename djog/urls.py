from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^register/', views.register, name='register'),
    url(r'^details/', views.details, name='details')
]