from django.conf.urls import url

from djog.user import views

urlpatterns = [
    url(r'^$', views.UserView.as_view(), name='user')
]
