# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.test.client import encode_multipart
from rest_framework.authtoken.models import Token
from .models import User
from django.urls import reverse

# Create your tests here.
class LoginTest(APITestCase):

    def setUp(self):
        self.valid_login = {
        'email': 'admin@admin.com',
        'password': 'admin123'
        }
        self.invalid_login = {
            "email": "majezanu@gmail.com",
            "password": "admin"
        }
        self.client = APIClient()
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')

    def test_valid_login(self):
        response = self.client.post('/v1/auth/token/',data=json.dumps(self.valid_login), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response,'access')
        
            
    def test_invalid_login(self):
        response = self.client.post('/v1/auth/token/',data=json.dumps(self.invalid_login), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        

