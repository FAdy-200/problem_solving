# https://leetcode.com/problems/move-zeroes/
from typing import *


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        while j < len(nums) and nums[j] != 0:
            j += 1
        i = j
        while i < len(nums) and nums[i] == 0:
            i += 1
        while len(nums) > j and len(nums) > i:
            print(i, j)
            nums[i], nums[j] = nums[j], nums[i]
            while j < len(nums) and nums[j] != 0:
                j += 1
            while i < len(nums) and nums[i] == 0:
                i += 1


S = Solution()
X = S.moveZeroes([0, 1, 0, 3, 12])
print(X)
