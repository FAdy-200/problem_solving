# https://leetcode.com/problems/regular-expression-matching/
from USEFUL_CODES.LC import *


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def check(j):
            i = j + 1
            while i < len(p):
                if p[i] != "*":
                    return False
                i += 2
            if i == len(p) + 1:
                return True
            return False

        @cache
        def DP(i, j):
            if i == len(s) and (j >= len(p) or check(j)):
                return True
            if i >= len(s) or j >= len(p):
                return False
            if j < len(p) - 1 and p[j + 1] == "*":
                if p[j] == "." or p[j] == s[i]:
                    return DP(i + 1, j) or DP(i, j + 2)
                return DP(i, j + 2)
            if p[j] == ".":
                return DP(i + 1, j + 1)
            if p[j] == s[i]:
                return DP(i + 1, j + 1)
            return False

        return DP(0, 0)


S = Solution()
X = S.isMatch("aa", p=".*c")
print(X)
