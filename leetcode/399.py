# https://leetcode.com/problems/evaluate-division/
from typing import *
from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for i, j in enumerate(equations):
            graph[j[0]][j[1]] = values[i]
            graph[j[1]][j[0]] = 1 / values[i]

        def dfs(src: str, dist: str, visited: set) -> float:
            if src in visited:
                return -1
            if src not in graph:
                return -1
            if src == dist:
                return 1
            visited.add(src)
            for node in graph[src].keys():
                if node == dist:
                    return graph[src][node]
                if (temp := dfs(node, dist, visited)) != -1:
                    return graph[src][node] * temp
            return -1

        ans = []
        for query in queries:
            ans.append(dfs(query[0], query[1], set()))
        return ans


S = Solution()
X = S.calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])
print(X)
