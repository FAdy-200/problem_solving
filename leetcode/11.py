# https://leetcode.com/problems/container-with-most-water/
from typing import *


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        ans = (len(height) - 1) * min(height[i], height[j])
        while i < j:
            mi = min(i, j, key=lambda x: height[x])
            if i == mi:
                i += 1
                x = (j - i) * min(height[i], height[j])
                if x > ans:
                    ans = x
            else:
                j -= 1
                x = (j - i) * min(height[i], height[j])
                if x > ans:
                    ans = x
        return ans


S = Solution()
t = S.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(t)
t = S.maxArea([i for i in range(1, 11)])
print(t)
t = S.maxArea([1])
print(t)
