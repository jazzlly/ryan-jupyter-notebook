#%%

import unittest

class TestStringMethod(unittest.TestCase):
    def setUp(self):
        print("begin test")
        
    def tearDown(self):
        print("end test")
    
    def testUpper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        
    def testIsUpper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    
    def testSplit(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        
        with self.assertRaises(TypeError):
            s.split(2)
    
'''
可以输入模块，测试类，函数

运行模块
python -m unittest_tutor
python -m unittest unittest_tutor

运行单独函数
python -m unittest unittest_tutor.TestStringMethod.testSplit

输出详细信息
python -m unittest -v unittest_tutor


'''
#%%

class AssertTutor(unittest.TestCase):
    
    def testListEquals(self):
        self.assertEqual(list('abcd'), ['a', 'b', 'c', 'd'])
            
if __name__ == '__main__':
    ## 如果在Jupyter下，请用如下方式运行单元测试    
    unittest.main(argv=['first-arg-is-ignored'], exit=False)    
    # unittest.main()