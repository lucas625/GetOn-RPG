# -*- coding: utf-8 -*-

"""Module for testing users app rest API."""

from django.test import TestCase,Client
from users.models.models import UserForm


class APIRestGetTestUser(TestCase):

    @classmethod
    def setUpTestData(cls):
        super(APIRestGetTestUser, cls)
        cls._url = '/api/users/'

    def setUp(self):
        self.client = Client()

    def test_get_clients(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code,200)

    def test_save_user(self):   
        form = UserForm(data={'email' : 'user@user.com', 'password' : 'user', 'name' : 'user'})
        self.assertTrue(form.is_valid())   

    def test_save_user_empty_data(self):
        form = UserForm(data={})
        self.assertFalse(form.is_valid())

    def test_save_user_without_email(self):
        form = UserForm(data={'password' : 'user', 'name' : 'user'})
        self.assertFalse(form.is_valid())

    def test_save_user_without_name(self):
        form = UserForm(data={'email' : 'user@user.com','password' : 'user',})
        self.assertFalse(form.is_valid())

    def test_save_user_without_password(self):
        form = UserForm(data={'email' : 'user@user.com','name' : 'user'})
        self.assertFalse(form.is_valid())