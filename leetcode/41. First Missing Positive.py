# https://leetcode.com/problems/first-missing-positive/
from typing import *


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        t = 1
        while t in s:
            t += 1
        return t
