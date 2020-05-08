# -*- coding: utf-8 -*-

"""Core app urls module."""

from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from core.viewsets.template_model_viewset import TemplateModelViewSet


ROUTER = routers.DefaultRouter()
ROUTER.register('template-model', TemplateModelViewSet)

app_name = 'core'

urlpatterns = [  # pylint: disable=invalid-name
    path('', include(ROUTER.urls)),
]
