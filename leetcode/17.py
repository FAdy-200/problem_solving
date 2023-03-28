# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import *
from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        return [i[0] + i[1] for i in product(*[d[i] for i in digits])]


S = Solution()
X = S.letterCombinations("23")
print(X)
