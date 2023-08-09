# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/
from USEFUL_CODES.LC import *


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        def calc(speed: int) -> float:
            if not speed:
                return inf
            ans = 0.0
            for i in dist[:-1]:
                ans += ceil(i / speed)
            ans += dist[-1] / speed
            return ans

        l, h = 0, (max(dist) + 1) * 100
        while l < h:
            mid = (l + h) // 2
            x = calc(mid)
            if x > hour:
                l = mid + 1
            else:
                h = mid
        return l if calc(l) <= hour else -1


S = Solution()
X = S.minSpeedOnTime([1, 3, 2], 6)
print(X)
