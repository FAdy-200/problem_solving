# https://leetcode.com/problems/new-21-game/
from math import perm
from functools import cache


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1.0
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        wind = 1.0 / maxPts
        ans = 0.0
        for i in range(1, n + 1):
            dp[i] = wind
            if i < k:
                wind += dp[i] / maxPts
            else:
                ans += dp[i]
            if i >= maxPts:
                wind -= dp[i - maxPts] / maxPts
        return ans


S = Solution()
X = S.new21Game(10, 5, 10)
# X = S.new21Game(n = 21, k = 17, maxPts = 10)
print(X)
# 1
# 11  2
# 111 21 12 3
# 1111 112 211 121 22 31 13  4
# 11111 221 122 212 2111 1211 1121 1112 113 131 311 32 23 41 14 5
