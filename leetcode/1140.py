# https://leetcode.com/problems/stone-game-ii/description/
from typing import List
from functools import cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @cache
        def DB(i:int,m:int,turn:int) -> int:
            if i > len(piles):
                return 0
            if turn: # Alice's turn
                ans = 0
                for j in range(1,2*m + 1):
                    ans = max(ans,sum(piles[i:i+j]) + DB(i+j,max(m,j),0))
                return ans
            else:
                ans = float("inf")
                for j in range(1,2*m + 1):
                    ans = min(ans,DB(i+j,max(m,j),1))
                return ans
        return DB(0,1,1)

S = Solution()
X = S.stoneGameII([2,7,9,4,4])
print(X)