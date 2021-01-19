#%%
# from django.core.urlresolvers import resolve
# from lists.views import home_page
from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

# import unittest
# from selenium import webdriver

class MyTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def testOpen(self):
        self.assertEqual(1+1, 3)

