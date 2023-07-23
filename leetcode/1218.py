# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
from USEFUL_CODES.LC import *


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp: Dict[int, int] = {}
        for i in arr[::-1]:
            if i + difference in dp:
                dp[i] = dp[i + difference] + 1
            else:
                dp[i] = 1
        return max(dp.values())


S = Solution()
X = S.longestSubsequence([1, 2, 3, 4], 1)
print(X)
