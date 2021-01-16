#%%

from typing import List
import unittest

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums) <= 1 or k == 0:
            return

        k = k % len(nums)

        self.__rotate(nums, 0, len(nums)-1)
        self.__rotate(nums, 0, k - 1)
        self.__rotate(nums, k, len(nums)-1)

        print('nums %s' % nums)

    def __rotate(self, nums: List[int], begin: int, end: int) -> None:
        while begin < end:
            tmp = nums[begin]
            nums[begin] = nums[end]
            nums[end] = tmp
            begin += 1
            end -= 1
            
class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution();

    def teardown(self) -> None:
        pass

    def boundary(self):
        self.solution.rotate([], 1)
        self.solution.rotate([1], 12)
        self.solution.rotate([1,2,3], 0)

    def smoke(self):
        self.solution.rotate([1, 2, 3, 4, 5,6,7], 3);
        self.solution.rotate([1, 2, 3, 4, 5,6,7], 17);

suite = unittest.TestSuite()
suite.addTest(Test('smoke'))
suite.addTest(Test('boundary'))

runner = unittest.TextTestRunner()
runner.run(suite)
