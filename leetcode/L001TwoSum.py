# %%
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        adict = {}
        for i, v in enumerate(nums):
            sub = target - v
            if sub in adict:
                return (adict.get(sub), i)

            adict[v] = i

        return []
# %%
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum([3, 3], 6))

