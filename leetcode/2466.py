# https://leetcode.com/problems/count-ways-to-build-good-strings/
from typing import *
from collections import defaultdict
import sys, threading

sys.setrecursionlimit(1000001)


# threading.stack_size(2 ** 27)


class Solution:
    def same(self, low: int, high: int, one: int) -> int:
        d = {}
        seen = set()
        ans = [0]
        d[one] = 2
        if low <= one <= high:
            ans[-1] += 2

        def backtrack(i: int):
            if i in d:
                if low <= i < high:
                    if i not in seen:
                        ans[-1] = (ans[-1] + d[i]) % (10 ** 9 + 7)
                        seen.add(i)
                return d[i]
            if i < 0:
                return 0
            if (i - one) in d:
                d[i] = 2 * d[i - one]
            else:
                d[i] = 2 * backtrack(i - one)
            if low <= i <= high:
                if i not in seen:
                    ans[-1] = (ans[-1] + d[i]) % (10 ** 9 + 7)
                    seen.add(i)
            return d[i]

        backtrack(high)
        return ans[-1]

    def dif(self, low: int, high: int, zero: int, one: int) -> int:
        d = {}
        seen = set()
        ans = [0]
        d[min(zero, one)] = 1
        d[max(zero, one)] = 1 if max(zero, one) % min(zero, one) else 2
        if low <= max(zero, one) <= high:
            ans[-1] = (ans[-1] + d[max(zero, one)]) % (10 ** 9 + 7)
        if low <= min(zero, one) <= high:
            if min(zero, one) not in seen:
                ans[-1] = (ans[-1] + d[min(zero, one)]) % (10 ** 9 + 7)

        def backtrack(i: int):
            if i in d:
                if low <= i < high:
                    if i not in seen:
                        ans[-1] = (ans[-1] + d[i]) % (10 ** 9 + 7)
                        seen.add(i)
                return d[i]
            if i < 0:
                return 0
            if (i - zero) in d:
                t1 = d[i - zero]
            else:
                t1 = backtrack(i - zero)
            if (i - one) in d:
                t2 = d[i - one]
            else:
                t2 = backtrack(i - one)
            d[i] = t1 + t2
            if low <= i <= high:
                if i not in seen:
                    ans[-1] = (ans[-1] + d[i]) % (10 ** 9 + 7)
                    seen.add(i)
            return d[i]

        backtrack(high)
        return ans[-1]

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        dp[0] = 1
        ans = 0
        for i in range(min(zero, one), high + 1):
            if i >= zero:
                dp[i] = (dp[i - zero] + dp[i]) % (10 ** 9 + 7)
            if i >= one:
                dp[i] = (dp[i - one] + dp[i]) % (10 ** 9 + 7)
            if low <= i <= high:
                ans += (dp[i])% (10 ** 9 + 7)
        return ans

S = Solution()
X = S.countGoodStrings(1, 100000, 1, 1)
print(X)
