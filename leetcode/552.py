# https://leetcode.com/problems/student-attendance-record-ii/
from functools import cache
from sys import setrecursionlimit


class Solution:

    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[1, 1], [1, 0], [0, 0]]  # dp[0] => has 0 L , dp[0][0] has 0 A dp[0][1] has [A]
        for i in range(1, n):
            t1 = dp[0][0] + dp[1][0] + dp[2][0]
            t2 = t1 + dp[0][1] + dp[1][1] + dp[1][2]
            dp = [[t1 % MOD, t2 % MOD], dp[0], dp[1]]
        return sum([i[0] for i in dp]) + sum([i[1] for i in dp])

    def checkRecord1(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        d = {}

        # @cache
        def DPF(i: int, a: int, l: int) -> int:
            if (x := (i, a, l)) in d:
                return d[x]
            if i == n:
                return 1
            lans = DPF(i + 1, a, 0) % MOD
            if a:
                if (l + 1) % 3:
                    lans += DPF(i + 1, a, (l + 1) % 3) % MOD
            else:
                lans += DPF(i + 1, 1, 0) % MOD
                if (l + 1) % 3:
                    lans += DPF(i + 1, a, (l + 1) % 3) % MOD
            d[x] = lans % MOD
            return d[x]

        # @cache
        dd = {}

        def DPB(i: int, a: int, l: int) -> int:
            if (x := (i, a, l)) in dd:
                return dd[x]
            if i == 0:
                return 1
            lans = 0
            if l:
                lans += DPB(i - 1, a, l - 1) % MOD
            else:
                if a:
                    lans += DPB(i - 1, a - 1, 0) % MOD
                    if i >= 2:
                        lans += DPB(i - 1, a - 1, 1) % MOD
                        if i > 2:
                            lans += DPB(i - 1, a - 1, 2) % MOD
                if i > a:
                    lans += DPB(i - 1, a, 0) % MOD
                    if i >= a + 2:
                        lans += DPB(i - 1, a, 1) % MOD
                        if i > a + 2:
                            lans += DPB(i - 1, a, 2) % MOD
            dd[x] = lans % MOD
            return lans % MOD

        t1 = DPB(n, 1, 0)
        t2 = DPB(n, 0, 0)
        t3 = DPB(n, 0, 1)
        ans = (t1 + t2 + t3) % MOD
        if n >= 2:
            ans += (DPB(n, 1, 1) + DPB(n, 0, 2)) % MOD
        if n >= 3:
            ans += DPB(n, 1, 2) % MOD
        return ans % MOD, DPF(0, 0, 0)
        # return DPF(0,0,0)


setrecursionlimit(10 ** 5)
S = Solution()
X = S.checkRecord1(1)
Y = S.checkRecord(1)
print(X, Y)
