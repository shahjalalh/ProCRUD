__author__ = 'shahjalal'

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.user_info, name='user_info'),
]