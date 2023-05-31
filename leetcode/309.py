# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
from typing import List
from functools import cache


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def DB(i: int, val: int) -> int:
            if i < 0:
                return 0
            if val!=-1 and val - prices[i] > 0:
                return max(val - prices[i] + DB(i - 2, -1), DB(i - 1, val))
            elif prices[i] - val <= 0:
                return DB(i - 1, val)
            else:
                return max(DB(i - 1, prices[i]), DB(i - 1, -1))
        return DB(len(prices)-1, -1)

S = Solution()
X = S.maxProfit([3,3])
print(X)