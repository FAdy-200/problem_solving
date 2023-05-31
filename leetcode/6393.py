# https://leetcode.com/contest/biweekly-contest-105/problems/maximum-strength-of-a-group/

from typing import List


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: abs(x), reverse=True)
        ans = 0
        last = float("-inf")
        for i in nums:
            if i == 0:
                continue
            if ans:
                ans *= i
            else:
                ans = i
            if i < 0:
                last = max(i, last)
        if ans < 0 and ans != last:
            ans /= last
        return int(ans) if ans else 0


S = Solution()
X = S.maxStrength([-1, -7, -5, 7, 7, 0, 9, 0, -5, -6])
print(X)
