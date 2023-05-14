# https://leetcode.com/problems/maximize-score-after-n-operations/
from functools import cache
from typing import *
from math import gcd
import bisect


class Solution:
    def maxScoreOLD(self, nums: List[int]) -> int:
        n = len(nums) // 2
        gcds = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                g = (gcd(nums[i], nums[j]), i, j)
                bisect.insort(gcds, g)

        d = {}

        def myFilter(local_gcds, ind):
            ele = set(local_gcds[ind][1:])

            def test(x):
                if x[1] in ele or x[2] in ele:
                    return False
                return True

            return list(filter(test, local_gcds))

        def DB(local_gcds, local_n) -> int:
            if not local_n:
                return 0
            if (tuple(local_gcds), local_n) in d:
                return d[(tuple(local_gcds), local_n)]
            if len(local_gcds) == 1:
                d[(tuple(local_gcds), local_n)] = local_gcds[0][0] * local_n
                return d[(tuple(local_gcds), local_n)]
            ans = DB(myFilter(local_gcds[:], -1), local_n - 1) + local_n * local_gcds[-1][0]
            local_i = len(local_gcds) - 2
            while local_i:
                t1 = DB(myFilter(local_gcds[:], local_i), local_n - 1) + local_n * local_gcds[local_i][0]
                ans = t1 if t1 > ans else ans
                local_i -= 1
            d[(tuple(local_gcds), local_n)] = ans
            return ans

        return DB(gcds, n)

    def maxScore(self, nums: List[int]) -> int:
        @cache
        def DB(local_nums, n):
            if not local_nums:
                return 0
            ans = 0
            for i in range(len(local_nums)):
                for j in range(i + 1, len(local_nums)):
                    new = local_nums[:i] + local_nums[i + 1:j] + local_nums[j + 1:]
                    ans = max(ans, n * gcd(local_nums[i], local_nums[j]) + DB(tuple(new), n - 1))
            return ans

        return DB(tuple(nums), len(nums) // 2)


S = Solution()
# X = S.maxScore([6, 3, 4, 3, 5, 3, 5, 10, 10, 3, 1, 7, 3, 3])
X = S.maxScore(
    [109497, 983516, 698308, 409009, 310455, 528595, 524079, 18036, 341150, 641864, 913962, 421869, 943382, 295019])
# Y = S.maxScore1(
#     [109497, 983516, 698308, 409009, 310455, 528595, 524079, 18036, 341150, 641864, 913962, 421869, 943382, 295019])
print(X)
