# https://leetcode.com/problems/combinations/description/
from typing import *


class Solution:
    def mine(self, n, y):
        ans = [[]]
        for i in range(1, n + 1):
            tans = [[*k] for k in ans]
            for j in tans:
                j.append(i)
                ans.append(j)

        return [k for k in ans if len(k) == y]

    def notMine(self, n, k):
        sol = []

        def backtrack(remain, comb, nex):
            # solution found
            if remain == 0:
                sol.append(comb.copy())
            else:
                # iterate through all possible candidates
                for i in range(nex, n + 1):
                    # add candidate
                    comb.append(i)
                    # backtrack
                    backtrack(remain - 1, comb, i + 1)
                    # remove candidate
                    comb.pop()

        backtrack(k, [], 1)
        return sol

    def combine(self, n: int, y: int) -> List[List[int]]:
        return self.notMine(n, y)

S = Solution()
X = S.combine(4, 2)
print(X)