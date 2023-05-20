# https://leetcode.com/problems/house-robber/
from typing import *

class Solution:
    def rob(self, nums: List[int]) -> int:
        taken = [nums[0]]
        notTaken = [0]
        for i in nums[1:]:
            taken.append(max(notTaken[-1]+i,taken[-1]))
            notTaken.append(max(taken[-2],notTaken[-1]))
        return max(taken[-1],notTaken[-1])
