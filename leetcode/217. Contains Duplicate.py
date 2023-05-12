# https://leetcode.com/problems/contains-duplicate/
from typing import *


def containsDuplicate(nums: List[int]) -> bool:
    nums = sorted(nums)
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


print(containsDuplicate([1, 2, 2]))
