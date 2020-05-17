# -*- coding: utf-8 -*-

"""Module for core app template model viewset."""

from rest_framework import viewsets

from users.models import UserModel
from users.serializers.users_model_serializer import UsersModelSerializer


class UserModelViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """
    It provides end-points for CRUD the template model.
    """
    queryset = UserModel.objects.all()
    serializer_class = UsersModelSerializer
