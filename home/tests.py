from django.test import TestCase
from models import Location,category,Post
from datetime import dt
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
    
class PostTestCase(TestCase):
    def setUp(self):
        #create a location
        self.ruiru = location(name = "Ruiru")
        self.ruiru.save_location()

        #create a category
        self.test = category(cat = "Test")
        self.test.save_category()

        self.new_post = Post(location = self.ruiru, category= self.test, title='This is a test', caption= 'It will be cool')
        