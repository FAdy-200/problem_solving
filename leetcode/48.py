# https://leetcode.com/problems/rotate-image/description/?envType=study-plan&id=programming-skills-ii
from typing import *
from typing import List, Tuple
import numpy as np


class Solution:
    def rotate2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = np.array(matrix).transpose().tolist()
        for i in range(len(matrix)):
            matrix[i] = temp[i][::-1]

    def swap(self, matrix, li):
        for i in li:
            t1 = matrix[i[0][0]][i[0][1]]
            for j in range(1, 4):
                t2 = matrix[i[j][0]][i[j][1]]
                matrix[i[j][0]][i[j][1]] = t1
                t1 = t2
            matrix[i[0][0]][i[0][1]] = t1

    def calcPairs(self, i: int, j: int, n: int) -> List[Tuple[int, int]]:
        ans = [(i, j)]
        if i == j:
            ans.append((i, n - j - 1))
            ans.append((n - i - 1, n - j - 1))
            ans.append((n - i - 1, j))
            return ans
        ans.append((j, n - i - 1))
        ans.append((n - i - 1, n - j - 1))
        ans.append((n - j - 1, i))
        return ans

    def rotate3(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        swaps = []
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                swaps.append(self.calcPairs(i, j, n))
        self.swap(matrix, swaps)


    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                t1 = matrix[i][j]
                if i==j:
                    t2 = matrix[i][n-j-1]
                    matrix[i][n - j - 1] = t1
                    t1 = t2

                    t2 = matrix[n-i-1][n-j-1]
                    matrix[n-i-1][n - j - 1] = t1
                    t1 = t2

                    t2 = matrix[n-i-1][j]
                    matrix[n-i-1][j] = t1
                    t1 = t2


                    matrix[i][j] = t1
                else:
                    t2 = matrix[j][n - i - 1]
                    matrix[j][n - i - 1] = t1
                    t1 = t2

                    t2 = matrix[n - i - 1][n - j - 1]
                    matrix[n - i - 1][n - j - 1] = t1
                    t1 = t2

                    t2 = matrix[n-j-1][i]
                    matrix[n-j-1][i] = t1
                    t1 = t2

                    matrix[i][j] = t1


S = Solution()
x = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
S.rotate(x)
z = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]