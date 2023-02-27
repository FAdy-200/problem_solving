# https://leetcode.com/problems/find-the-middle-index-in-array/
from typing import *


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        su = sum(nums) - nums[0]
        su_so = 0
        if su == su_so:
            return 0
        for i in range(1, len(nums)):
            su_so += nums[i - 1]
            su -= nums[i]
            if su == su_so:
                return i
        return -1


S = Solution()
x = S.findMiddleIndex([4, 1, -1])
print(x)
