# https://leetcode.com/problems/spiral-matrix/?envType=study-plan&id=programming-skills-ii

from typing import *
from math import ceil, floor


class Solution:
    def __init__(self):
        self.mat = None

    def pass1(self, s, f):
        return self.mat[len(self.mat[0]) - f][s:f]

    def pass2(self, s, f):
        semi_ans = []
        for i in range(s, f):
            semi_ans.append(self.mat[i][len(self.mat[0]) - s])
        return semi_ans

    def pass3(self, s, f):
        return self.mat[len(self.mat) - f - 1][f:s][::-1]

    def pass4(self, s, f):
        semi_ans = []
        for i in range(s, f, -1):
            semi_ans.append(self.mat[i][f])
        return semi_ans

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.mat = matrix
        ans = []
        n = len(matrix)
        m = len(matrix[0])
        s1, s2, s3, s4 = 0, 1, m - 1, n - 2
        f1, f2, f3, f4 = m, n, 0, 0
        while len(ans) < n * m:
            if s1 < f1:
                ans += self.pass1(s1, f1)
                s1 += 1
                f1 -= 1
            if len(ans) == n * m:
                return ans
            if s2 < f2:
                ans += self.pass2(s2, f2)
                s2 += 1
                f2 -= 1
            if len(ans) == n * m:
                return ans
            if f3 < s3:
                ans += self.pass3(s3, f3)
                s3 -= 1
                f3 += 1
            if len(ans) == n * m:
                return ans
            if f4 < s4:
                ans += self.pass4(s4, f4)
                s4 -= 1
                f4 += 1
        return ans


S = Solution()
x = S.spiralOrder([[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25
    , 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]])
# [1,2,3,20,30,60,90,55,69,66,77,88,99,11,7,4,5,6,50,80,44,33,22,8,9]
# x = S.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])  # [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
# x = S.spiralOrder([[7],[9],[6]])
print(x)
