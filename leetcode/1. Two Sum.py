# https://leetcode.com/problems/two-sum/
from typing import *


def twoSum(nums, target: int) -> List[int]:
    nums = list(sorted(enumerate(nums), key=lambda x: x[1]))
    a = 0
    b = len(nums) - 1
    ans = nums[a][1] + nums[b][1]
    while ans != target:

        if ans > target:
            b -= 1
        else:
            a += 1
        ans = nums[a][1] + nums[b][1]
    return [nums[a][0], nums[b][0]]


ans = twoSum([3, 2, 4], 6)
print(ans)
