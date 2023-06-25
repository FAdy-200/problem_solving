# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/
from USEFUL_CODES.LC import *


class Solution:
    def countPaths(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]
        mod = 10**9 + 7


        def dfs(lx, ly):
            if dp[lx][ly] > 0:
                return dp[lx][ly]
            t = 0
            for i, j in ((lx + 1, ly), (lx, ly + 1), (lx - 1, ly), (lx, ly - 1)):
                if m > i >= 0 and n > j >= 0:
                    if matrix[lx][ly] > matrix[i][j]:
                        t = (t+dfs(i, j))%mod
            dp[lx][ly] = (t + 1)%mod
            return (t + 1)%mod

        ans = 0
        for x in range(m):
            for y in range(n):
                ans = (ans + dfs(x, y))%mod
        return ans
with open("2328.txt","r") as inp:
    p1 = eval(inp.readline())
S = Solution()
X = S.countPaths(p1)
print(X)
