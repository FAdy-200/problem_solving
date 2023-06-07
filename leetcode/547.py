# https://leetcode.com/problems/number-of-provinces/
from typing import List, DefaultDict
from collections import defaultdict, deque


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        This is a typical UnionFind problem, but I altered it and made all the nodes that are from the same union have a mapping to an increasing integer, so I have the number of unions at the end without going through them again
        :param isConnected:
        :return:
        """
        union: DefaultDict[int, int] = defaultdict(int)
        n = len(isConnected)
        ma = 1
        for i in range(n):
            if not union[i]:
                d = deque()
                d.append(i)
                while d:
                    node = d.popleft()
                    union[node] = ma
                    for j in range(n):
                        if isConnected[node][j] and not union[j]:
                            d.append(j)
                ma += 1
        return ma - 1


S = Solution()
X = S.findCircleNum([[1, 1, 0], [1, 1, 1], [0, 0, 1]])
print(X)
