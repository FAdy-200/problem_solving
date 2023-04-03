# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
from typing import *


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = []
        points.sort(key=lambda z: z[0])
        x = points[0]
        for i in range(1, len(points)):
            if points[i][0] <= x[1]:
                x[1] = min(x[1], points[i][1])
            else:
                ans.append(x)
                x = points[i]
        ans.append(x)
        return len(ans)


S = Solution()
X = S.findMinArrowShots([[1, 2], [2, 4], [2, 4], [2, 5]])
print(X)
