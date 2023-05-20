# https://leetcode.com/problems/is-graph-bipartite/
from typing import *


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        s1 = {0}
        s2 = set()
        unchecked = set()
        n = len(graph)

        for i in range(n):
            if i in s2:
                for j in graph[i]:
                    if j in s2:
                        return False
                    s1.add(j)
            elif i in s1:
                for j in graph[i]:
                    if j in s1:
                        return False
                    s2.add(j)
            else:
                unchecked.add(i)
        i = unchecked.pop()
        while len(unchecked):
            if i in s2:
                for j in graph[i]:
                    if j in s2:
                        return False
                    s1.add(j)
                i = unchecked.pop()
            elif i in s1:
                for j in graph[i]:
                    if j in s1:
                        return False
                    s2.add(j)
                i = unchecked.pop()
            else:
                put = 0
                for j in graph[i]:
                    if j in s1:
                        put = 1
                        s2.add(i)
                        break
                    if j in s2:
                        put = 1
                        s1.add(i)
                        break
                if not put:
                    s1.add(i)
        return True


S = Solution()
X = S.isBipartite([[3], [2], [1], [0 , 1]])
print(X)
