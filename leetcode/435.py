# https://leetcode.com/problems/non-overlapping-intervals/
from typing import *

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        points = intervals
        ans = []
        points.sort(key=lambda z: z[0])
        x = points[0]
        for i in range(1, len(points)):
            if points[i][0] < x[1]:
                x[1] = min(x[1], points[i][1])
            else:
                ans.append(x)
                x = points[i]
        ans.append(x)
        return len(intervals) - len(ans)


S = Solution()
X = S.eraseOverlapIntervals([[1,2],[2,3]])
print(X)
