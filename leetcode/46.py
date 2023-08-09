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

    def permuteOld(self, nums: List[int]) -> List[List[int]]:
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


    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        taken = [0]*6
        def backtrack(sub_ans:List[int]):
            if len(sub_ans) == n:
                ans.append(sub_ans[:])
                return
            for j in range(0,n):
                if not taken[j]:
                    taken[j] = 1
                    sub_ans.append(nums[j])
                    backtrack(sub_ans)
                    sub_ans.pop()
                    taken[j] = 0
        backtrack([])
        return ans


S = Solution()
X = S.permute([1, 2, 3])
print(X)
