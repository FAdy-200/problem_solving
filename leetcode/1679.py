# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75
from USEFUL_CODES.LC import *

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        ans = 0
        while i < j:
            if (x := nums[i] + nums[j]) > k:
                j -= 1
            elif x < k:
                i += 1
            else:
                ans += 1
                i += 1
                j -= 1
        return ans
