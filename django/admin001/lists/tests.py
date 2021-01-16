#%%
from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

class HomePageTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def testOpen(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

