# https://leetcode.com/problems/find-all-anagrams-in-a-string/?envType=study-plan&id=programming-skills-ii
from typing import *

from collections import defaultdict


class Solution:
    def findAnagrams2(self, s: str, p: str) -> List[int]:
        np = sorted(p)
        checked = defaultdict(lambda: [False, False])
        ans = []
        for i in range(len(s) - len(p) + 1):
            if not checked[s[i:i + len(p)]][0]:
                if sorted(s[i:i + len(p)]) == np:
                    ans.append(i)
                    checked[s[i:i + len(p)]][1] = True
                checked[s[i:i + len(p)]][0] = True
            else:
                if checked[s[i:i + len(p)]][1]:
                    ans.append(i)
        return ans

    def check(self, dp, ds):
        for i, j in dp.items():
            if ds[i] != j:
                return False
        return True

    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        dp = defaultdict(lambda: 0)
        ds = defaultdict(lambda: 0)
        for i in p:
            dp[i] += 1
        for j in s[:len(p)]:
            ds[j] += 1

        for i in range(len(s) - len(p)):
            if self.check(dp, ds):
                ans.append(i)
            ds[s[i]] -= 1
            ds[s[i+len(p)]]+=1
        return ans


S = Solution()
x = S.findAnagrams("cbaebabacd", "abc")
print(x)
