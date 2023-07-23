# https://leetcode.com/problems/number-of-longest-increasing-subsequence/
from USEFUL_CODES.LC import *


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        count = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[i] == dp[j] + 1:
                        count[i] += count[j]

        ans = 0
        longest = max(dp)
        for i in range(n):
            if dp[i] == longest:
                ans += count[i]
        return ans


S = Solution()
X = S.findNumberOfLIS([1,3,2,5,4,7,6,8,9,10])
print(X)
