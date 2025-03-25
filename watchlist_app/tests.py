from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth.models import User
from django.urls import reverse

from . import models
from .api import serializers



class StreamPlatformTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='example', password='pass@123')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.stream = models.StreamPlatform.objects.create(name="hulu", about="streaming platform", website="https://hulu.net")
        
      
        
    def test_streamplatform_create(self):
        print("======== running streamplatform create test ==============")
        data = {
            "name" : "Netflix",
            "about" : "streaming platform",
            "website" : "https://www.netflix.com"
            
        }
        response = self.client.post(reverse('stream'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
     
        
    def test_streamplatform_list(self):
        print("======== running streamplatform list test ==============")
        response = self.client.get(reverse('stream'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
     
        
    def test_streamplatform_get_object(self):
        print("======== running streamplatform get object test ==============")
        response = self.client.get(reverse('stream-details', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
    def test_streamplatform_update(self):
        print("======== running streamplatform update test ==============")
        new_data = {
            "name" : "Netflix",
            "about" : "streaming platform",
            "website" : "https://www.netflix.com"
        }
        response = self.client.put(reverse('stream-details', args=(self.stream.id,)), data=new_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        
    def test_streamplatform_delete(self):
        print("======== running streamplatform delete test ==============")
        response = self.client.delete(reverse('stream-details', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        
        
        


class WatchListTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='example', password='pass@123')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.stream = models.StreamPlatform.objects.create(name="hulu", about="streaming platform", website="https://hulu.net")

    
    def test_watchlist_create(self):
        print("======== running watchlist create test ==============")
        data = {
            "title": "test title",
            "storyline": "test storyline",
            "platform": self.stream,
            "active": True,
        }
        response = self.client.post(reverse('movie-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)