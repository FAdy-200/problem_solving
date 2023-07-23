# https://leetcode.com/problems/knight-probability-in-chessboard/
from USEFUL_CODES.LC import *


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if not k:
            return 1.0
        moves = ((2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2))

        @cache
        def DP(r: int, c: int, l_k: int) -> float:
            if 0 > r or r > n - 1 or 0 > c or c > n - 1:
                return 0.0
            if not l_k:
                return (1/8)**k
            ans = 0.0
            for i, j in moves:
                ans += DP(r + i, c + j, l_k - 1)
            return ans

        return DP(row, column, k)

S = Solution()
X = S.knightProbability(5,3,2,0)
print(X)
