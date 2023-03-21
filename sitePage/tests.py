from django.http import HttpResponse
from django.test import TestCase

from .views import *

class SitePageWebPageTestCase(TestCase):
    def setUp(self):
        pass
    
    def test_home_serve(self):
        page = self.client.get('home/')
        self.assertTrue(isinstance(page, HttpResponse))
        
    def test_home_serve(self):
        page = self.client.get('about/')
        self.assertTrue(isinstance(page, HttpResponse))