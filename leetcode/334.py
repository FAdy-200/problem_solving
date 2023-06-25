# https://leetcode.com/problems/increasing-triplet-subsequence
from USEFUL_CODES.LC import *


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        st = []
        ost = []
        for i in nums:
            while ost and i <= ost[-1]:
                ost.pop()
            ost.append(i)
            if  len(st) >1 and  st[0] < i < st[-1]:
                st.pop()
                st.append(i)
            if st and  i > st[-1]:
                st.append(i)
            if len(st) <= len(ost):
                st = ost[:]

            if len(st) == 3:
                return True
        return False


S = Solution()
X = S.increasingTriplet([20, 100, 10, 12, 5, 13])
print(X)
