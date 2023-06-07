# https://leetcode.com/problems/check-if-it-is-a-straight-line/
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        try:
            m = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
            a = coordinates[1][1] - coordinates[1][0] * m

            def ev(p):
                return p[1] == a + p[0] * m
        except ZeroDivisionError:
            x = coordinates[0][0]

            def ev(p):
                return p[0] == x
        for coord in coordinates:
            if not ev(coord):
                return False
        return True


S = Solution()
X = S.checkStraightLine([[1, 2], [5,2],[564,0]])
print(X)
