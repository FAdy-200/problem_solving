# https://leetcode.com/problems/container-with-most-water/
from typing import *


class Solution:
    def maxArea(self, height: List[int]) -> int:
        x = list(sorted(enumerate(height), key=lambda _: _[1], reverse=True))
        n = len(x)
        ma = x[0][1]
        i = 0
        ans = 0
        while (i < n) and (x[i][1] == ma):
            for j in range(i, n):
                temp = min(x[i][1], x[j][1]) * abs(x[i][0] - x[j][0])
                if temp > ans:
                    ans = temp
            i += 1
        return ans


s = Solution()
print(s.maxArea([1, 1]))
