# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/
from USEFUL_CODES.LC import *


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort(key=lambda x: x[0])

        class WorkAround(Sequence):
            def __init__(self, it):
                self.it = it
                self.n = len(it)

            def __getitem__(self, i):
                return self.it[i][0]

            def __len__(self):
                return self.n

        bi_events = WorkAround(events)
        dp = [[-1] * k for _ in range(n)]
        def DP(l_i: int, l_k: int) -> int:
            if l_i >= n or not l_k:
                return 0
            if dp[l_i][l_k - 1] > -1:
                return dp[l_i][l_k - 1]
            ans = 0
            p = bisect.bisect_right(bi_events, events[l_i][1])
            if p != n and events[p][0] == events[l_i][1]:
                p += 1
            if (c1 := DP(p, l_k - 1) + events[l_i][2]) > ans:
                ans = c1
            if (c2 := DP(l_i + 1, l_k)) > ans:
                ans = c2
            dp[l_i][l_k - 1] = ans
            return ans

        return DP(0, k)

setrecursionlimit(1000000)
S = Solution()
with open("1751.txt", "r") as inp:
    p1 = eval(inp.readline())
    p2 = eval(inp.readline())
X = S.maxValue(p1, p2)
print(X)
