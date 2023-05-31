# https://leetcode.com/problems/network-delay-time/
from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for i in times:
            graph[i[0] - 1].append(i[1:])
        # print(graph)
        delays = [float("inf")] * n
        delays[k - 1] = 0
        st =[]
        def DFS(s:int, v:int) -> None:
            for li in graph[s - 1]:
                if delays[li[0] - 1] > v + li[1]:
                    delays[li[0] - 1] = v + li[1]
                    heapq.heappush(st,(v + li[1],li[0])) # optimized route
                    # DFS(li[0], delays[li[0] - 1])
            while st:
                it = heapq.heappop(st)
                DFS(it[1],it[0])
        DFS(k, 0)
        # print(delays)
        ans = max(delays)
        return ans if ans < float("inf") else -1


S = Solution()
X = S.networkDelayTime(
    [[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2)
print(X)
