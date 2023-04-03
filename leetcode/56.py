# https://leetcode.com/problems/merge-intervals/
from collections import defaultdict
import bisect
from typing import *


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key=lambda z: z[0])
        x = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= x[1]:
                x[1] = max(x[1], intervals[i][1])
            else:
                ans.append(x)
                x = intervals[i]
        ans.append(x)
        return ans


S = Solution()
X = S.merge([[1,3],[0,4]])
print(X)
