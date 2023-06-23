from django.conf.urls import url
from django.urls import path, re_path
from home import views


urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^home$', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
]