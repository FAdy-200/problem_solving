# https://leetcode.com/contest/biweekly-contest-105/problems/extra-characters-in-a-string/
from typing import List
from functools import cache


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        @cache
        def DP(s: str) -> int:
            ans = len(s)
            for i in dictionary:
                if i in s:
                    t = 0
                    for k in s.split(i):
                        if k:
                            t += DP(k)
                    ans = min(t, ans)
            return ans

        return DP(s)
