# https://leetcode.com/problems/removing-stars-from-a-string/description
from USEFUL_CODES.LC import *


class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for i in s:
            if i == "*":
                ans.pop()
            else:
                ans.append(i)
        return "".join(ans)
