# https://leetcode.com/problems/maximum-subarray/
from typing import *


def max_sub_array(nums: List[int]) -> int:
    s = nums[0]
    ts = nums[0]
    for i in nums[1:]:
        if i > ts:
            if ts < 0:
                ts = i
            else:
                ts+=i
        else:
            ts += i
        if ts > s:
            s = ts
    return s


ans = max_sub_array([1,2])
print(ans)
