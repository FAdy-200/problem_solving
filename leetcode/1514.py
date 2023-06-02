# https://leetcode.com/problems/path-with-maximum-probability/
from typing import List
import heapq


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [[] for _ in range(n)]
        for i, val in enumerate(edges):
            graph[val[0]].append((val[1], succProb[i]))
            graph[val[1]].append((val[0], succProb[i]))
        probs = [0]*n
        st = []

        def dfs(s: int, v: int) -> None:
            for li in graph[s]:
                if probs[li[0]] < v * li[1]:
                    probs[li[0]] = v * li[1]
                    heapq.heappush(st, (-v * li[1], li[0]))  # optimized route
            while st:
                it = heapq.heappop(st)
                dfs(it[1], -it[0])

        dfs(start, 1)
        return probs[end]

S = Solution()
X = S.maxProbability(3
,[[0,1],[1,2],[0,2]]
,[0.5,0.5,0.2]
,0
,2)
print(X)
