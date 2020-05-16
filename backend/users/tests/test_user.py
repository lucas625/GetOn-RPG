# -*- coding: utf-8 -*-

"""Module for testing core app rest API."""

from django.test import TestCase
from users.models.models import UserModel


class APIRestGetTestUser(TestCase):
    """Test cases for rest API get."""

    @classmethod
    def setUpTestData(cls):
        super(APIRestGetTestUser, cls)
        cls._url = '/api/users/'

    def test_create_object_user(self):
        UserModel(email="testeteste@xxx.com",name="testeteste",password="123456")

    def test_save_user(self):
        user = UserModel(email="testeteste@xxx.com",name="testeteste",password="123456")
        user.save()
