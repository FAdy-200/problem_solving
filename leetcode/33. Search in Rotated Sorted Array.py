# https://leetcode.com/problems/search-in-rotated-sorted-array/
from USEFUL_CODES.LC import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1
        while l<r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]:
                if nums[mid] >= target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

S = Solution()
X = S.search([6, 1, 3, 5], 1)
print(X)
