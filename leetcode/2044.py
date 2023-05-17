# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/
from typing import *
from functools import reduce
from math import factorial


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def OR(a: int, b: int) -> int:
            return a | b

        n = len(nums)
        max_val = [reduce(OR, nums)]
        ans = [0]

        def backtrack(so_far, j):
            if j > len(nums):
                return
            if so_far:
                if reduce(OR, so_far) == max_val[-1]:
                    ans[-1] += 1
            for i in range(j, n):
                so_far.append(nums[i])
                backtrack(so_far, i + 1)
                so_far.pop()

        backtrack([], 0)
        return ans[-1]


S = Solution()
X = S.countMaxOrSubsets([2, 2, 2])
print(X)
"""
an efficient approach: find bitwise OR of array. ith bit contribution to to xor sum is 2**(n-1).
The result is 2**(n-1) * bitORSum

Explanation:

consider ith bit for the final result. If there is no element whose ith bit is 1, then all xor subset 
sums has 0 in ith bit; if there are k (k>=1) elements whose ith bits are 1, then there are in total 
comb(k, 1) + comb(k,3) + .. = 2**(k-1) ways to select odd number our of these k elements to make the subset
xor sum's ith bit to be 1, and there are 2**(n-k) ways to choose from the remaining elements whose ith bits
are 0s. Therefore, we have in total 2**(k-1) * 2**(n-k) = 2**(n-1) subsets whose xor sums have 1 in their
ith bit, which means the contribution to the final sum is 2**(n-1) * 2**i. Notice this result is irrelevant
to k. 

So we only need to determine whether there is any element whose ith bit is 1. We use bitwise OR sum to do this.

Time complexity: O(n), Space: O(1)
"""