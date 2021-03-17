import unittest

class Widget():
    def __init__(self, name):
        self.name = name
        self.wsize = (50, 50)
        
    def size(self):
        return self.wsize
    
    def resize(self, width, height):
        self.wsize = (width, height)
    
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')

def suite():
    suite = unittest.TestSuite()
    # suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)
