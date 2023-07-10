# https://leetcode.com/problems/count-all-possible-routes/
from USEFUL_CODES.LC import *

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        d_locations = {j:i for i,j in enumerate(locations)}
        mod = 10**9 + 7
        @cache
        def DP(i,f):
            if not f:
                if i == finish:
                    return 1
                return 0
            l_ans = int(i == finish)
            for k in range(1,f+1):
                if (x:=locations[i] - k) in d_locations:
                    l_ans = (l_ans + DP(d_locations[x],f-k))%mod
                if (x:=locations[i] + k) in d_locations:
                    l_ans = (l_ans + DP(d_locations[x],f-k))%mod
            return l_ans%mod

        return DP(start,fuel)

S = Solution()
X = S.countRoutes([2,3,6,8,4],1,3,5)
print(X)
