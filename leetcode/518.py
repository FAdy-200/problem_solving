# https://leetcode.com/problems/coin-change-ii/
from typing import *
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        coins.sort(reverse=True)
        for i in coins:
            for j in range(1, amount+1):
                if j-i>=0:
                    dp[j] += dp[j-i]
        return dp[-1]



S = Solution()
X = S.change(amount = 5, coins = [1,2,5])
print(X)