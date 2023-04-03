# https://leetcode.com/problems/single-element-in-a-sorted-array/
from typing import *
import bisect


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums) - 1
        while l < r - 1:
            mid = (l + r) // 2
            if nums[mid] == nums[mid - 1]:
                if not mid % 2:
                    r = mid
                else:
                    l = mid
            elif nums[mid] == nums[mid + 1]:
                if not mid % 2:
                    l = mid
                else:
                    r = mid
            else:
                return nums[mid]
        return nums[l + 1] if l else nums[l]


S = Solution()
X = S.singleNonDuplicate([1, 2, 2])
print(X)
