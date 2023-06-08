# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/
from USEFUL_CODES.LC import *


class Solution:

    def countNegatives1(self, grid: List[List[int]]) -> int:
        """
        Time: O(m*n)
        :param grid:
        :return:
        """
        ans = 0
        for _, row in enumerate(grid):
            for __, val in enumerate(row):
                if val < 0:
                    ans += 1
        return ans

    def countNegatives(self, grid: List[List[int]]) -> int:
        """
        Time: O(m+n)
        :param grid:
        :return:
        """
        ans = 0
        m, n = len(grid), len(grid[0])
        i, j = 0, n - 1
        while i < m:
            t = j
            while j >= 0 > grid[i][j]:
                j -= 1
            ans += (t - j) * (m - i)
            i += 1
        return ans
