# https://leetcode.com/problems/longest-increasing-subsequence/description/
from USEFUL_CODES.LC import *


class Solution:
    def lengthOfLISTable(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        ans = 1
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        if dp[i] > ans:
                            ans = dp[i]
        return ans

    def lengthOfLISMem(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def DP(i:int,last:str) -> int:
            if i == n:
                return 1
            c1 = DP(i+1,str(nums[i]))
            ans = 1
            if last and nums[i] > int(last):
                ans += c1
            elif not last:
                ans = c1
            if (c2:= DP(i+1,last)) > ans:
                ans = c2
            return ans
        return DP(0,"")

    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.lengthOfLISTable(nums)

S = Solution()
X = S.lengthOfLIS([10,9,2,5,3,7,101,18])
print(X)
