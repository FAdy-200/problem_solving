# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import *


def findMin(nums: List[int]) -> tuple:
    target = nums[0]
    a = 0
    b = len(nums) - 1
    if b <= 1:
        ans = min(nums)
        return ans, nums.index(ans)
    ind = 0
    mid = (a + b) // 2
    while a <= b:
        if nums[mid] > target:
            a = mid + 1
        elif nums[mid] < target:
            b = mid - 1
            target = nums[mid]
            ind = mid
        mid = (a + b) // 2
    return target, ind


def search(nums: List[int], target: int) -> int:
    _, ind = findMin(nums)
    if nums[-1] >= target:
        a = ind
        b = len(nums) - 1
    else:
        a = 0
        b = ind
    mid = (a + b) // 2
    while a <= b:
        if nums[mid] > target:
            b = mid - 1
        elif nums[mid] < target:
            a = mid + 1
        else:
            return mid
        mid = (a + b) // 2

    return -1


ans = search([1, 3, 5], 1)
print(ans)
