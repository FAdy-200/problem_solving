# https://leetcode.com/problems/contains-duplicate-iii/
from typing import *


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List, k: int, t: int) -> bool:
        l = sorted(enumerate(nums), key=lambda x: x[1], reverse=True)
        n = len(l)
        i = 0
        j = 1
        while True:
            if not (i - n):
                return False
            if not (j - n):
                i += 1
                j = i + 1
                continue
            if l[i][1] - l[j][1] <= t:
                if abs(l[i][0] - l[j][0]) <= k:
                    return True
                j += 1
            else:
                i += 1
                j = i + 1


S = Solution()
x = S.containsNearbyAlmostDuplicate([1, 2, 1, 1],
                                    1,
                                    0)
print(x)
