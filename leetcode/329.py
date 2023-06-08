# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
from USEFUL_CODES.LC import *


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]

        def dfs(lx: int, ly: int) -> int:
            if dp[lx][ly] > 0:
                return dp[lx][ly]
            t = 0
            for i, j in ((lx + 1, ly), (lx, ly + 1), (lx - 1, ly), (lx, ly - 1)):
                if m > i >= 0 and n > j >= 0:
                    if matrix[lx][ly] > matrix[i][j]:
                        t = max(t, dfs(i, j) + 1)
            if not t:
                dp[lx][ly] = 1
                return 1
            dp[lx][ly] = t
            return t

        ans = 0
        for x in range(m):
            for y in range(n):
                ans = max(ans, dfs(x, y))
        return ans


S = Solution()
X = S.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]])
print(X)
