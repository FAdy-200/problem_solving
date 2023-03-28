# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
from collections import Counter
from typing import *

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k or k >= len(nums):
            return False
        freq = Counter(nums)
        fr = list(set(nums))
        fr.sort()
        i = 0
        while i < len(fr) and i+k <= len(fr):
            for j in range(k):
                if freq[fr[i + j]] > 0 and (j == 0 or fr[i + j] == fr[i + j - 1] + 1):
                    freq[fr[i + j]] -= 1
                else:
                    return False
            while i < len(fr) and freq[fr[i]] == 0:
                i += 1
        return True if sum(freq.values())==0 else False


S = Solution()
X = S.isPossibleDivide([1,1,2,2,3,3], 2)
print(X)
