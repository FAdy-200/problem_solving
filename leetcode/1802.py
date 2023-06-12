# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/
from USEFUL_CODES.LC import *


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def calc(x, y):
            if x == 0:
                return 0
            start = max(y - x, 0)
            sum1 = y * (1 + y) // 2
            sum2 = start * (1 + start) // 2
            return sum1 - sum2

        maxSum -= n
        l, r = 0, maxSum
        while l <= r:
            mid = (l + r) // 2
            if calc(index + 1, mid) + calc(n - index - 1, mid - 1) <= maxSum:
                l = mid + 1
            else:
                r = mid - 1
        return l


S = Solution()
# X = S.maxValue(6773685, 5166078, 49851224)
X = S.maxValue(4, 0, 4)
print(X)
