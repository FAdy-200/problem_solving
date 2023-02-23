# https://leetcode.com/problems/longest-repeating-character-replacement/
from typing import *
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(lambda: 0)
        ans = 1
        i = 0
        j = 0
        n = len(s)
        if not n:
            return 0
        freq[s[i]] += 1
        while j < n - 1:
            j += 1
            freq[s[j]] += 1
            if (j - i + 1) - max(freq.values()) > k:
                freq[s[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
        return ans


S = Solution()
x = S.characterReplacement("AABABBA", 1)
z = S.characterReplacement("ABAB", 2)
print(x,z)