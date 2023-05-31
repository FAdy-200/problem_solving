# https://leetcode.com/problems/course-schedule-ii/
from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph:List[List[int]] = [[] for _ in range(numCourses)]
        for i in prerequisites:
            graph[i[1]].append(i[0])
        in_ord:List[int] = [0] * numCourses
        for i in graph:
            for j in i:
                in_ord[j] += 1
        order:List[int] = []
        d = deque()
        for i,j in enumerate(in_ord):
            if not j:
                d.append(i)
        while d:
            order.append(d.popleft())
            for j in graph[order[-1]]:
                in_ord[j] -= 1
                if not in_ord[j]:
                    d.append(j)
        return order if len(order) == numCourses else []


S = Solution()
X = S.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
print(X)
