# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import *


def findMin(nums: List[int]) -> int:
    target = nums[0]
    a = 0
    b = len(nums) - 1
    if b <= 1:
        return min(nums)
    mid = (a + b) // 2
    while a <= b:
        if nums[mid] > target:
            a = mid + 1
        elif nums[mid] < target:
            b = mid - 1
            target = nums[mid]
        mid = (a + b) // 2
    return target


ans = findMin([11])
print(ans)
