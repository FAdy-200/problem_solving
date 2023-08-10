# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
from USEFUL_CODES.LC import *


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        l, r = 0, len(nums) - 1
        if target == nums[l] or target == nums[r]:
            return True
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] == nums[r]:
                return self.search(nums[:mid], target) or self.search(nums[mid + 1:], target)
            elif nums[mid] >= nums[l]:
                if nums[mid] > target >= nums[l]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[l]:
                    l = mid + 1
                else:
                    r = mid

        return True if nums[l] == target else False


S = Solution()
X = S.search(nums=[1,3,1,1], target=3)
print(X)
