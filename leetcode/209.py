# https://leetcode.com/problems/minimum-size-subarray-sum/
from typing import *


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 1
        ans = float("inf")
        su = nums[0]
        while len(nums) + 1 > j > i:
            if su >= target:
                ans = min(ans, j - i)
                su -= nums[i]
                i += 1

            else:
                su += nums[j] if j < len(nums) else 0
                j += 1
        return int(ans) if ans != float("inf") else 0


S = Solution()
x = S.minSubArrayLen(7,
                     [2, 3, 1, 2, 4, 3])
