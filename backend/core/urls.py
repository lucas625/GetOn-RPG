# -*- coding: utf-8 -*-

"""Core app urls module."""

from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from core.viewsets.template_model_viewset import TemplateModelViewSet
from users.viewsets.user_api_view import UserModelViewSet


ROUTER = routers.DefaultRouter()
ROUTER.register('template-model', TemplateModelViewSet)
ROUTER.register(r'users',UserModelViewSet)

app_name = 'core'

urlpatterns = [
    path('', include(ROUTER.urls)),
]