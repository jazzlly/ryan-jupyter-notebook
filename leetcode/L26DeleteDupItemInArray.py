


#%%

from typing import List
import unittest

# 1 2 3
# [0  ,1   ,   1,    1,   1,  2,   2,   3,   3,   4]
#     s       e

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        start = 0
        for end in range(1, len(nums)):
            if nums[start] != nums[end]:
                start += 1
                nums[start] = nums[end]

        print('nums: %s' % nums)
        return start + 1

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution();

    def boundary(self):
        self.assertEquals(self.solution.removeDuplicates(None), 0)
        self.assertEquals(self.solution.removeDuplicates([]), 0)
        self.assertEquals(self.solution.removeDuplicates([1]), 1)

    def smoke(self):
        self.assertEquals(self.solution.removeDuplicates([1,1,1]), 1)
        self.assertEquals(self.solution.removeDuplicates([1,2,3]), 3)
        self.assertEquals(self.solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]), 5)


suite = unittest.TestSuite()
suite.addTest(Test('smoke'))
suite.addTest(Test('boundary'))

runner = unittest.TextTestRunner()
runner.run(suite)


