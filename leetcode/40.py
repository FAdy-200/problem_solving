# https://leetcode.com/problems/combination-sum-ii/
from typing import *


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()

        def helper(so_far, at):
            if (x := sum(so_far)) == target:
                ans.add(tuple(sorted(so_far)))
                return
            if x > target:
                return

            for i in range(at, len(candidates)):
                so_far.append(candidates[i])
                if tuple(sorted(so_far)) not in ans:
                    helper(so_far, i + 1)
                if len(so_far) == len(candidates) and x + candidates[i] < target:
                    return
                so_far.pop()

        helper([], 0)

        return ans


S = Solution()
X = S.combinationSum2(
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 30)
print(X)