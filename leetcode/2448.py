# https://leetcode.com/problems/minimum-cost-to-make-array-equal/
from USEFUL_CODES.LC import *


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        l, h = min(nums), max(nums)

        def calc(i: int) -> int:
            l_ans = 0
            for k in range(len(nums)):
                l_ans += abs(i - nums[k]) * cost[k]
            return l_ans

        while l < h:
            mid = (l + h) // 2
            x, y = calc(mid - 1), calc(mid)
            if x < y:
                h = mid - 1
            else:
                l = mid + 1

        return min(calc(l), calc(l - 1))


S = Solution()
X = S.minCost(
    [1, 2, 3, 4, 5],
    [4, 2, 8, 1, 3])
print(X)
