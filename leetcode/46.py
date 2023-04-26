# https://leetcode.com/problems/permutations/description/
from typing import *
from itertools import permutations
from copy import deepcopy


class Solution:
    def __init__(self):
        self.d = {}

    def permuteChese(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))

    def helper(self, s, m):
        ts = tuple(s)
        if (ts, m) in self.d:
            return self.d[ts, m]
        if not len(s):
            return [[m]]
        temp = []
        for i in s:
            cs = deepcopy(s)
            cs.remove(i)
            if z := self.helper(cs, i):
                temp += z
        self.d[ts, m] = list(map(lambda x: x + [m], temp))
        return self.d[ts, m]

    def permute(self, nums: List[int]) -> List[List[int]]:
        s = set(nums)
        ts = tuple(s)
        if ts in self.d:
            return [self.d[ts]]
        if len(s) == 1:
            return [nums]
        temp = []
        for i in s:
            cs = deepcopy(s)
            cs.remove(i)
            if z := self.helper(cs, i):
                temp += z
        return temp


S = Solution()
X = S.permute([1, 2, 3])
print(X)
