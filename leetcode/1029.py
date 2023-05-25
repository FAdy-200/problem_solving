# https://leetcode.com/problems/two-city-scheduling/
from typing import List
from functools import cache


class Solution:
    def twoCitySchedCostDB(self, costs: List[List[int]]) -> int:
        _2n = len(costs)
        n = _2n // 2
        d = {}

        # @cache
        def DB(i: int, a: int, b: int) -> int:
            if (x := (i, a, b)) in d:
                return d[x]
            if i == _2n:
                d[x] = 0
                return 0
            if a < n and b < n:
                d[x] = min(DB(i + 1, a + 1, b) + costs[i][0], DB(i + 1, a, b + 1) + costs[i][1])
                return d[x]
            elif a < n:
                d[x] = DB(i + 1, a + 1, b) + costs[i][0]
                return d[x]
            else:
                d[x] = DB(i + 1, a, b + 1) + costs[i][1]
                return d[x]

        return DB(0, 0, 0)

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr = list(sorted(costs,key=lambda x:x[0]-x[1]))
        n = len(costs)
        j = 0
        ans = 0
        for i,val in enumerate(arr):
            ans += val[j]
            if i == n//2 - 1:
                j = 1
        return ans

S = Solution()
X = S.twoCitySchedCost(
    [[10,20],[30,200],[400,50],[30,20]])
print(X)
