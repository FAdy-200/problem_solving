# https://leetcode.com/problems/permutations/description/
from typing import *
from itertools import permutations


class Solution:
    def __init__(self):
        self.d = {(): []}

    def permuteChese(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))

    def permute(self, nums: List[int]) -> List[List[int]]:
        pass


S = Solution()
X = S.permute([1, 2, 3])
print(X)
