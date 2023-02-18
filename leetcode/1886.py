# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/?envType=study-plan&id=programming-skills-ii
from typing import *


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        c1, c2, c3, c4 = True, True, True, True
        for i, k in enumerate(mat):
            for j, m in enumerate(k):
                if i == n // 2 and j == n // 2 and n%2:
                    if target[i][j] != m:
                        return False
                elif i == n // 2 and n%2:
                    if target[i][j] != m:
                        c1 = False
                    if target[j][i] != m:
                        c2 = False
                    if target[i][n - j - 1] != m:
                        c3 = False
                    if target[n - j - 1][i] != m:
                        c4 = False
                elif j == n // 2 and n%2 :
                    if target[i][j] != m:
                        c1 = False
                    if target[j][n - i - 1] != m:
                        c2 = False
                    if target[n - i - 1][j] != m:
                        c3 = False
                    if target[j][i] != m:
                        c4 = False
                else:
                    if target[i][j] != m:
                        c1 = False
                    if target[j][n - i - 1] != m:
                        c2 = False
                    if target[n - i - 1][n - j - 1] != m:
                        c3 = False
                    if target[n - j - 1][i] != m:
                        c4 = False
        return c1 | c2 | c3 | c4

S = Solution()
x = S.findRotation([[1,2,3],[4,5,6],[7,8,9]],[[3,6,9],[2,5,8],[1,4,7]])
print(x)

