# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
from USEFUL_CODES.LC import *


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[x] if (x := bisect.bisect_right(letters, target)) < len(letters) else letters[0]
