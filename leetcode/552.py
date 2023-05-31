# https://leetcode.com/problems/student-attendance-record-ii/
from functools import cache
from sys import setrecursionlimit
# TODO: Finish this
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        d = {}
        # @cache
        def DPF(i:int,a:int,l:int) -> int:
            if (x:=(i,a,l)) in d:
                return d[x]
            if i == n:
                return 1
            lans = DPF(i + 1, a, 0) % MOD
            if a:
                if (l+1)%3:
                    lans += DPF(i + 1, a, (l+1)%3)%MOD
            else:
                lans += DPF(i + 1, 1, 0) % MOD
                if (l+1)%3:
                    lans += DPF(i + 1, a, (l+1)%3)%MOD
            d[x] = lans%MOD
            return d[x]

        @cache
        def DPB(i:int,a:int,l:int) -> int:
            if i == 0:
                return 1
            lans = 0
            if l:
                lans += DPB(i - 1, a, l-1) % MOD
            else:
                if a:
                    lans += DPB(i - 1, a - 1, 0) % MOD
                    if i >= 2:
                        lans += DPB(i - 1, a, 0) % MOD
                        lans += DPB(i - 1, a, 1) % MOD
                        if i > 2:
                            lans += DPB(i - 1, a, 2) % MOD

                else:
                    lans += DPB(i - 1, a, 0) % MOD
                    if i >= 2:
                        lans += DPB(i - 1, a, 1) % MOD
                        if i > 2:
                            lans += DPB(i - 1, a, 2) % MOD
            return lans%MOD
        ans = DPB(n,1,0) + DPB(n,0,0) + DPB(n,0,1)
        if n >= 2:
            ans += DPB(n,1,1) + DPB(n,0,2)
        if n >= 3:
            ans += DPB(n, 1, 2)
        return ans
        # return DPF(0,0,0)

setrecursionlimit(10**5)
S = Solution()
X = S.checkRecord(3)
print(X)
