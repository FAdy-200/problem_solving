# https://leetcode.com/problems/sqrtx/description

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        l, h = 0, x

        while l < h:
            mid = (l + h) / 2
            if abs(mid * mid - x) < 1e-5:
                return int(mid)
            if mid * mid > x:
                h = mid
            else:
                l = mid
