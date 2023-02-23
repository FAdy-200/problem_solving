# https://leetcode.com/problems/minimum-size-subarray-sum/
from typing import *

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 1
        ans = float("inf")
        while len(nums) + 1 > j > i:
            if sum(nums[i:j])>=target:
                ans = min(ans,j-i)
                i+=1
            else:
                j+=1
        return int(ans) if ans != float("inf") else 0


S = Solution()
x = S.minSubArrayLen(396893380,
                    []) 