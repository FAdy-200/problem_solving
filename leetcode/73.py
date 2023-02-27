# https://leetcode.com/problems/set-matrix-zeroes/description/
from typing import *


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []
        n = len(matrix[0])
        for i in range(len(matrix)):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        for i in range(len(matrix)):
            if i in rows:
                matrix[i] = [0]*n
            else:
                for j in range(n):
                    if j in cols:
                        matrix[i][j] = 0
