# https://leetcode.com/problems/trapping-rain-water/
from typing import *


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        if height:
            l, r = 0, len(height) - 1
            lm, rm = height[l], height[r]
            while l < r:
                if height[l] <= height[r]:
                    l += 1
                    lm = max(lm, height[l])
                    ans += lm - height[l]
                else:
                    r -= 1
                    rm = max(rm, height[r])
                    ans += rm - height[r]
        return ans


S = Solution()
X = S.trap([5, 2, 3, 3])
print(X)
