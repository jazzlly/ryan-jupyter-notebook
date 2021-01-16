#%%

#%%

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:8000')

assert 'Django' in browser.title

#%%
import unittest
from selenium import webdriver

class MyTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()
    
    def testOpen(self):
        self.browser.get('http://localhost:8000')
        print('browser title: %s' % self.browser.title)
        self.assertIn('Django', self.browser.title)

suite = unittest.TestSuite()
suite.addTest(MyTest('testOpen'))

runner = unittest.TextTestRunner()
runner.run(suite)
