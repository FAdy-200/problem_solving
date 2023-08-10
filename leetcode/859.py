# https://leetcode.com/problems/buddy-strings/description/
from USEFUL_CODES.LC import *


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(goal)
        if c1 != c2:
            return False
        d = ""
        t = ""
        for i in range(len(s)):
            if s[i] != goal[i]:
                if d:
                    if s[i] != d or goal[i] != t:
                        return False
                else:
                    d = goal[i]
                    t = s[i]
        if d:
            return True
        if s != goal:
            return False
        if max(c1.values()) > 1:
            return True
        return False


S = Solution()
X = S.buddyStrings("abac",
"abad")
print(X)
