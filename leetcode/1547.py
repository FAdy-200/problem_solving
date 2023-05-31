# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
from typing import List
from functools import cache


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()

        @cache
        def cut(i: int, j: int, s: int, f: int) -> int:
            ans = float("inf")
            for m in range(i, j):
                if f > cuts[m] > s:
                    ans = min(ans, cut(i, m, s, cuts[m]) + cut(m + 1, j, cuts[m], f))
            return (f - s) + ans if ans < float("inf") else 0

        return cut(0, len(cuts), 0, n)


S = Solution()
X = S.minCost(n=9, cuts=[5, 6, 1, 4, 2])
print(X)
