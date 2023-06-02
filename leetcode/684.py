# https://leetcode.com/problems/redundant-connection/
from typing import List, DefaultDict, Set
from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Since there is only one extra edge it will create a circle thus we need to find the circle in the graph then find which of the circle's edges to cut
        Time: O(m*n)
        Space: O(m)
        where n = total edges, m = edges in the circle
        """
        graph: DefaultDict[int, Set[int]] = defaultdict(set)
        for i, val in enumerate(edges):
            graph[val[0]].add(val[1])
            graph[val[1]].add(val[0])

        def dfs(s: int, last: int, route: Set[int]) -> List[int]:
            route.add(s)
            for node in graph[s]:
                if node in route and node != last:
                    return [node,s]
                if node != last:
                    if x := dfs(node, s, route):
                        if x[0] != x[-1]:
                            x.append(s)
                        return x
            return []

        circle = dfs(1, 0, set())
        ans = 0
        for i in range(len(circle)-1):
            ans = max(ans,edges.index([min(circle[i],circle[i+1]),max(circle[i],circle[i+1])]))
        return edges[ans]

S = Solution()
X = S.findRedundantConnection([[3,4],[1,2],[2,4],[3,5],[2,5]])
print(X)
