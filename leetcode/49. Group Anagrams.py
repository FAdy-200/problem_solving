# https://leetcode.com/problems/group-anagrams/
from typing import *


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            temp = "".join(sorted(i))
            if d.get(temp) is None:
                d[temp] = [i]
            else:
                d[temp].append(i)
        return list(d.values())


S = Solution()
x = S.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(x)
