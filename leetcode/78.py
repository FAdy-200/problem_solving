# https://leetcode.com/problems/subsets/
from typing import *


class Solution:
    def __init__(self):
        self.ans = []
        self.nums = None

    def subsets1(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i in nums:
            tans = [[*k] for k in ans]
            for j in tans:
                j.append(i)
                ans.append(j)
        return ans

    def helper(self, so_far, at):
        self.ans.append(so_far[:])
        for i in range(at, len(self.nums)):
            so_far.append(self.nums[i])
            self.helper(so_far, i + 1)
            so_far.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.helper([], 0)
        return self.ans


S = Solution()
X = S.subsets([1, 2, 3])
print(X)
