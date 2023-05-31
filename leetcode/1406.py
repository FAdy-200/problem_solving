# https://leetcode.com/problems/stone-game-iii/
from typing import List
from functools import cache

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        su = sum(stoneValue)/2
        @cache
        def DB(i:int,j:int) -> int:
            if i >= n:
                return 0
            if j:
                ans = stoneValue[i] + DB(i+1,0)
                for it in range(2,4):
                    ans = max(ans,sum(stoneValue[i:i+it]) + DB(i+it,0))
                return ans
            else:
                ans = float("inf")
                for it in range(1, 4):
                    ans = min(ans, DB(i + it, 1))
                return ans
        alice = DB(0,1)
        print(alice)
        if alice == su:
            return "Tie"
        elif alice > su:
            return "Alice"
        return "Bob"


S = Solution()
X = S.stoneGameIII([-1,-2,-3])
print(X)
