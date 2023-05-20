# https://leetcode.com/problems/partition-equal-subset-sum/
from typing import *
from functools import cache


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        su = [sum(nums[i:]) for i in range(len(nums))]
        if su[0] % 2:
            return False
        su[0] = su[0] // 2
        n = len(nums)
        d = {}

        # @cache
        def DB(so_far, i):
            if (so_far, i) in d:
                return d[(so_far, i)]
            if so_far == su[0]:
                d[(so_far, i)] = True
                return True
            for j in range(i, n):
                if so_far + nums[j] <= su[0] <= so_far + su[j]:
                    if DB(so_far + nums[j], j + 1):
                        d[(so_far, i)] = True
                        return True
            d[(so_far, i)] = True
            return False

        return DB(nums[0], 1)


S = Solution()
Z = S.canPartition([3, 3, 3, 4, 5])

X = S.canPartition(
    [5, 79, 2, 4, 8, 16, 32, 64, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100])
print(Z, X)
