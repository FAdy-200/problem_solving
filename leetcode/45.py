# https://leetcode.com/problems/jump-game-ii/
from typing import *


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        ans = 0
        while i < n - 1:
            if i + nums[i] >= n - 1:
                return ans + 1
            ma = [float("-inf"), 0]
            for j in range(1, nums[i] + 1):
                if nums[i + j]:
                    if (x := nums[i + j] + j) > ma[0]:
                        ma[0] = x
                        ma[1] = j
            i += ma[1]
            ans += 1

        return ans

S = Solution()
X = S.jump([1,1,1,1])
print(X)