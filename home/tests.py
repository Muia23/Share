from django.test import TestCase
from models import location,category,Post
# Create your tests here.

class LocationTestCase(TestCase):

    #set up method
    def setUp(self):
        self.ruiru = location(name = 'Ruiru')
    
    #test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.ruiru,location))

class CategoryTestCase(TestCase):

    #set up method
    def setUp(self):
        self.test = category(cat = '#test')
    
    #test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.test,category))