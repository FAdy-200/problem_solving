# https://leetcode.com/problems/find-eventual-safe-states/
from USEFUL_CODES.LC import *


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = set()
        seen = set()

        def dfs(node: int):
            if not graph[node]:
                safe.add(node)
                seen.add(node)
                return
            seen.add(node)
            for l_i in graph[node]:
                if l_i not in seen:
                    dfs(l_i)
            add = True
            for l_i in graph[node]:
                if l_i not in safe:
                    add = False
            if add:
                safe.add(node)

        for i in range(len(graph)):
            if i not in seen:
                dfs(i)
        return sorted(safe)


S = Solution()
X = S.eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []])
print(X)
