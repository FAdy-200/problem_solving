# https://leetcode.com/problems/k-closest-points-to-origin/
from typing import *
from math import sqrt


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return list(sorted(points, key=lambda x: sqrt(x[0] ** 2 + x[1] ** 2)))[:k]
