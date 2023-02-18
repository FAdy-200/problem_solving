# https://leetcode.com/problems/find-the-duplicate-number/
from typing import *


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # temp = set()
        # for i in nums:
        #     if i in temp:
        #         return i
        #     temp.add(i)
        joke = [0] * len(nums)
        for i in nums:
            if joke[i] == 0:
                joke[i] = i
            else:
                return i
