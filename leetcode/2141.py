# https://leetcode.com/problems/maximum-running-time-of-n-computers/

from USEFUL_CODES.LC import *


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        extra = sum(batteries[:-n])

        running = batteries[-n:]
        for i in range(n - 1):
            if extra // (i + 1) < running[i + 1] - running[i]:
                return running[i] + extra // (i + 1)
            extra -= (i + 1) * (running[i + 1] - running[i])
        return running[-1] + extra // n


S = Solution()
X = S.maxRunTime(12,
                 [11, 89, 16, 32, 70, 67, 35, 35, 31, 24, 41, 29, 6, 53, 78, 83])
print(X)
