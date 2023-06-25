# https://leetcode.com/problems/k-radius-subarray-averages/
from USEFUL_CODES.LC import *


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        k2 = 2 * k + 1
        ans = [-1] * n
        if k2 > n:
            return ans

        m = n - k
        su = sum(nums[:k2])
        ans[k] = su // k2

        for i in range(k + 1, m):
            su -= nums[i - k - 1]
            su += nums[i + k]
            ans[i] = su // k2
        return ans


S = Solution()
X = S.getAverages(nums=[7, 4, 4, 3, 5], k=2)
print(X)
