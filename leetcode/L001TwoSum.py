
# %%

from typing import List


def twoSum(nums, target):
    # def twoSum(nums: List[int], target: int) -> List[int]:
    myDict = dict()
    for i in range(0, len(nums)):
        j = myDict.get(target - nums[i], -1)
        if (j != -1):
            return [i, j]
        myDict[nums[i]] = i

    return []


# %%
print(twoSum([2, 7, 11, 15], 9))
