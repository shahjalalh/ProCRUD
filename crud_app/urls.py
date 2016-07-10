__author__ = 'shahjalal'

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.user_list, name='user_list'),
    url(r'^user/user_info/$', views.user_info, name='user_info'),
    url(r'^user/(?P<pk>\d+)/$', views.user_detail, name='user_detail'),
    url(r'^user/(?P<pk>\d+)/update/$', views.user_update, name='user_update'),
]
