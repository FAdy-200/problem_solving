# https://leetcode.com/problems/equal-row-and-column-pairs/
from USEFUL_CODES.LC import *


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        grid_t = ["" for _ in range(n)]
        grid_n = ["" for _ in range(n)]
        for i in range(n):
            for j in range(n):
                grid_t[i] += f'{grid[j][i]} '
                grid_n[i] += f'{grid[i][j]} '
            grid_t[i] = grid_t[i].strip()
            grid_n[i] = grid_n[i].strip()
        ans = 0
        for i in range(n):
            for j in range(n):
                if grid_t[i] == grid_n[j]:
                    ans += 1
        return ans


S = Solution()

X = S.equalPairs([[3,1,2,2],
                  [1,4,4,4],
                  [2,4,2,2],
                  [2,5,2,2]])
print(X)
