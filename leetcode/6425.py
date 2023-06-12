from USEFUL_CODES.LC import *
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:

        @cache
        def DP(i, j, p):
            if j == len(s) - 1:
                return j - i + 1
            if p is None:
                if s[j] == s[j + 1]:
                    t=DP(i, j + 1, j + 1)
                    return t
                t=DP(i, j + 1, None)
                return t
            else:
                if s[j] == s[j + 1]:
                    t=max(j - i + 1, DP(p, j + 1, j + 1))
                    return t
                t=DP(i, j + 1, p)
                return t


        return DP(0, 0, None)

S = Solution()
X = S.longestSemiRepetitiveSubstring("52233")
print(X)