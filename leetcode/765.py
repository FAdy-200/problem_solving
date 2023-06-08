# https://leetcode.com/problems/couples-holding-hands/
from USEFUL_CODES.LC import *


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        """
        if we look at the example [4,1,6,2,0,8,7,5,9,3] and by creating a graph where each node represents a couch and each connection represents the existence of a partner:
        we start in the first couch and populate the graph in a dfs like search
        (4,1) 4's partner is 5
          |
        (7,5) 7's partner is 6
          |
        (6,0) 0's partner is 1

        we can see that there is a loop and in fact there will always be a loop in the graph:
        (3,9) 3's partner is 2
          |
        (2,8) 8's partner is 9

        if we count the number of edges in this graph (discarding the last edge in the circle) we will get our answer as each edge is a necessary swap
        Time: O(n)
        Space: O(n)
        :param row:
        :return:
        """
        graph = {}
        partner = {}
        for i in range(0, len(row), 2):
            graph[row[i]] = row[i + 1]
            graph[row[i + 1]] = row[i]
            partner[i] = i + 1
            partner[i + 1] = i
        seen = set()
        ans = 0
        for i in partner.keys():
            if i in seen:
                continue
            seen.add(i)
            seen.add(partner[i])
            t = graph[i]
            while t != partner[i]:
                seen.add(t)
                seen.add(partner[t])
                t = graph[partner[t]]
                ans += 1
        return ans


S = Solution()
X = S.minSwapsCouples([10, 5, 1, 12, 8, 0, 2, 16, 14, 4, 7, 11, 6, 9, 13, 15, 3, 17])
print(X)
