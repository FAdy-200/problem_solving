# https://leetcode.com/problems/restore-ip-addresses/
from typing import *


class Solution:
    def __init__(self):
        self.d = {}

    def helper(self, s, m, level):
        if (s, m, level) in self.d:
            return self.d[(s, m, level)]
        if level > 4:
            self.d[(s, m, level)] = []
            return []
        if not len(s) and level == 4:
            self.d[(s, m, level)] = [m]
            return [m]
        elif not len(s):
            self.d[(s, m, level)] = []
            return []
        temp = []
        if z := self.helper(s[1:], s[0], level + 1):
            temp += z
        if s[0] != "0" and len(s) > 1:
            if z := self.helper(s[2:], s[:2], level + 1):
                temp += z
            if len(s) > 2 and int(s[:3]) < 256:
                if z := self.helper(s[3:], s[:3], level + 1):
                    temp += z
        if m:
            self.d[(s, m, level)] = list(map(lambda x: m + '.' + x, temp))
        else:
            self.d[(s, m, level)] = temp
        return self.d[(s, m, level)]

    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.helper(s, "", 0)


S = Solution()
X = S.restoreIpAddresses("25525511135")
print(X)
