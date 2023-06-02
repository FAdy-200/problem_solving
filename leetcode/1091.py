# https://leetcode.com/problems/shortest-path-in-binary-matrix/
from typing import List,DefaultDict,Tuple
import heapq
from math import sqrt
from collections import defaultdict


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1
        n = len(grid)
        d:DefaultDict[Tuple[int,int],float|int] = defaultdict(lambda: float("inf"))
        d[(0,0)] = 1
        st:List[Tuple[int,int,int]] = []
        heapq.heappush(st, (1, 0, 0))
        while st:
            node = heapq.heappop(st)
            if node[1] == node[2] == n - 1:
                return node[0]

            for i in range(-1, 2):
                if n > node[1] + i > -1:
                    for j in range(-1, 2):
                        if n > node[2] + j > -1:
                            if not grid[node[1] + i][node[2] + j]:
                                temp = d[(node[1] + i, node[2] + j)]
                                if temp > node[0] + 1:
                                    heapq.heappush(st, (
                                        node[0] + 1, node[1] + i, node[2] + j))
                                    d[(node[1] + i, node[2] + j)] = min(node[0] + 1,temp)
        return -1


S = Solution()
X = S.shortestPathBinaryMatrix(
    [[0,0,1,0,0,1,0,1,0],[0,0,0,0,0,0,0,0,0],[0,1,1,0,1,1,1,1,1],[0,0,0,1,0,0,0,0,0],[1,1,0,0,0,1,0,0,0],[1,0,1,0,0,1,0,0,1],[1,1,1,1,0,0,1,0,0],[1,0,0,1,0,0,1,1,1],[0,0,0,0,0,0,0,0,0]])
print(X)
