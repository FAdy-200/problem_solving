# https://leetcode.com/problems/greatest-common-divisor-of-strings/
from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ma = gcd(len(str1),len(str2))
        l1 = len(str1)
        l2 = len(str2)
        ans = 0
        for i in range(ma,0,-1):
            if str1[:i]*(l1//i) == str1 and str1[:i]*(l2//i) == str2:
                return str1[:i]
        return ""


S = Solution()
X = S.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX")
print(X)
