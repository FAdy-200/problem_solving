# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/
from typing import List, DefaultDict, Tuple
import heapq
from collections import defaultdict


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pen = m * n + 1
        q = m+n
        working = []
        heapq.heappush(working, (m + n, 0, 0, 0))
        heur = [[inf] * n for _ in range(m)]
        while working:
            node = heapq.heappop(working)
            if node[1] == m - 1 and node[2] == n - 1: return node[3]
            for x, y in (
                    (node[1] + 1, node[2]), (node[1], node[2] + 1), (node[1] - 1, node[2]), (node[1], node[2] - 1)):
                if m > x >= 0 and n > y >= 0:
                    t = (q - x - y + (node[3] + grid[x][y]) * pen)
                    if heur[x][y] > t:
                        heapq.heappush(working, (t, x, y, node[3] + grid[x][y]))
                        heur[x][y] = t



inf = float("inf")

S = Solution()
with open("2290.txt", "r") as inp:
    p1 = eval(inp.readline())
X = S.minimumObstacles(p1)
print(X)
