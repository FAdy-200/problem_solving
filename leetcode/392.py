# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75

from USEFUL_CODES.LC import *


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                j += 1
            i += 1
        if j == len(s):
            return True
        return False


S = Solution()
X = S.isSubsequence("abd","ahbgdc")
print(X)
