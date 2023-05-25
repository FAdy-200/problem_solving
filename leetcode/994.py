# https://leetcode.com/problems/rotting-oranges/
from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bfs = deque()
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 2:
                    bfs.append((i, j, 0))
        ans = 0
        while bfs:
            i, j, val = bfs.popleft()
            ans = val
            if i > 0 and grid[i - 1][j] == 1:
                bfs.append((i - 1, j, val + 1))
                grid[i - 1][j] = 2
            if i < len(grid) - 1 and grid[i + 1][j] == 1:
                bfs.append((i + 1, j, val + 1))
                grid[i + 1][j] = 2
            if j > 0 and grid[i][j - 1] == 1:
                bfs.append((i, j - 1, val + 1))
                grid[i][j - 1] = 2
            if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                bfs.append((i, j + 1, val + 1))
                grid[i][j + 1] = 2
        for row in grid:
            for val in row:
                if val == 1:
                    return -1
        return ans

S = Solution()
X = S.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
print(X)