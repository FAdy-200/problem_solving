# https://leetcode.com/problems/all-paths-from-source-to-target/description/
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        dist = len(graph) - 1

        def bfs(i: int) -> List[List[int]]:
            lans = []
            for node in graph[i]:
                if node == dist:
                    lans.append([i, dist])
                else:
                    temp = []
                    for j in bfs(node):
                        temp.append([i, *j])
                    lans += temp

            # return list(filter(lambda x: x[-1] == dist, lans))
            return lans

        return list(filter(lambda x: x[-1] == dist, bfs(0)))
        # return bfs(0)

S = Solution()
X = S.allPathsSourceTarget([[8, 12, 11, 2, 4, 9, 14, 7, 1], [7, 8, 13, 2, 14, 4, 5, 10, 11], [3, 4, 5, 8, 6, 13, 11, 7, 9, 12],
     [6, 10, 13, 9, 4, 12, 7], [6, 8, 12, 10, 7, 9, 5], [14, 8, 13, 9, 7, 10, 12, 6], [8, 7, 13, 9, 11, 14, 12],
     [8, 10, 11, 13, 12, 9, 14], [12, 9, 10, 11, 13, 14], [13, 14, 11, 12, 10], [12, 11], [14, 13, 12], [13], [14], []])
print(X)
