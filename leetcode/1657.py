# https://leetcode.com/problems/determine-if-two-strings-are-close/
from USEFUL_CODES.LC import *


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return Counter((c1 := Counter(word1)).values()) == Counter(
            (c2 := Counter(word2)).values()) and c1.keys() == c2.keys()
