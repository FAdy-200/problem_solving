# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
from USEFUL_CODES.LC import *


class Solution:
    def maxProfitMem(self, prices: List[int], fee: int) -> int:
        @cache
        def DP(i, s):
            if i == len(prices):
                return 0
            if s:
                i_fee = DP(i + 1, 0) + prices[i] - fee
                __arg2 = DP(i + 1, 1)
                return max(i_fee, __arg2)
            i_ = DP(i + 1, 1) - prices[i]
            __arg3 = DP(i + 1, 0)
            return max(i_, __arg3)

        return DP(0, 0)

    def maxProfitTab(self, prices: List[int], fee: int) -> int:
        d = [[-1] * (len(prices) + 1) for _ in range(2)]
        d[0][-1] = 0
        d[1][-1] = 0
        for i in range(len(prices) - 1, -1, -1):
            d[0][i] = max(d[0][i + 1], d[1][i + 1] - prices[i])
            d[1][i] = max(d[0][i + 1] + prices[i] - fee, d[1][i + 1])
        return d[0][0]

    def maxProfit(self, prices: List[int], fee: int) -> int:
        return self.maxProfitTab(prices, fee)


with open("714.txt", "r") as inp:
    p1 = eval(inp.readline())
    p2 = eval(inp.readline())
S = Solution()
setrecursionlimit(10 ** 5)
X = S.maxProfit(p1,p2)
print(X)
