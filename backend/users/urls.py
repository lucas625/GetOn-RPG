# -*- coding: utf-8 -*-

"""Users app urls module."""

from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . import views


ROUTER = routers.DefaultRouter()

app_name = 'users'

urlpatterns = [
    path('{}/'.format(app_name), views.index, name='indexUser'),
]
