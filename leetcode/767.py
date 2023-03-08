# https://leetcode.com/problems/reorganize-string/

from collections import defaultdict


class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = defaultdict(lambda: 0)
        for i in s:
            freq[i] += 1
        return ""
