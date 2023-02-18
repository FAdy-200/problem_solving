# https://leetcode.com/problems/arithmetic-subarrays/?envType=study-plan&id=programming-skills-ii

from typing import *

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i,j in enumerate(l):
            new_array = sorted(nums[j:r[i]+1])
            if len(new_array) < 3:
                ans.append(True)
                continue
            dif =  new_array[1]-new_array[0]
            old = new_array[1]
            torf = True
            for k in new_array[2:]:
                if dif != k-old:
                    torf = False
                    break
                old = k
            ans.append(torf)
        return ans



S =Solution()
x = S.checkArithmeticSubarrays([4,6,5,9,3,7],[0,0,2],[2,3,5])
print(x)