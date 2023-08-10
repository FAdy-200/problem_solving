# https://leetcode.com/problems/single-number-ii/description/
from USEFUL_CODES.LC import *


class Solution:
    def singleNumberCheese(self, nums: List[int]) -> int:
        return min((z := Counter(nums)).keys(), key=lambda x: z[x])

    def singleNumber(self, nums: List[int]) -> int:
        bits = [0] * 32
        for i in nums:
            for j in range(32):
                if i & 1:
                    bits[j] += 1
                i = i >> 1
        ans = ["1" if i%3 else "0" for i in bits]
        return int.from_bytes(int(''.join(ans[::-1]),2).to_bytes(4,'little'),'little',signed=True)


S = Solution()
X = S.singleNumber([2,2,2,-1,-1,-1,8,-7,0,-7,0,-7,0])
print(X)
