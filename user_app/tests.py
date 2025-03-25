from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth.models import User
from django.urls import reverse



class RegisterTestCase(APITestCase):
    
    def test_register(self):
        print("======== running user registration test ==============")
        data = {
            "username" : "testuser",
            "email" : "testuser@example.com",
            "password" : "pass@123",
            "password2" : "pass@123"
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)




class LoginLogoutTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='example', password='pass@123')
       
        
    def test_login(self):
        print("======== running user login test ==============")
        data = {
            "username" : "example",
            "password" : "pass@123",
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
    def test_logout(self):
        print("======== running user logout test ==============")
        self.token = Token.objects.get(user__username='example')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)