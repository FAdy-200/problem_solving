# https://leetcode.com/problems/wildcard-matching/
from USEFUL_CODES.LC import *
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def check(j):
            for i in p[j:]:
                if i != "*":
                    return False
            return True

        @cache
        def DP(i, j):
            if i == len(s) and (j == len(p) or check(j)):
                return True
            if i >= len(s) or j >= len(p):
                return False
            if p[j] == "?":
                return DP(i + 1, j + 1)
            if p[j] == "*":
                return DP(i + 1, j + 1) or DP(i, j + 1) or DP(i + 1, j)
            if p[j] == s[i]:
                return DP(i + 1, j + 1)
            return False

        return DP(0, 0)