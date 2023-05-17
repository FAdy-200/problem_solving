# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/
from typing import *
from USEFUL_CODES.LinkedList import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        thead = head
        n = 0
        while thead:
            thead = thead.next
            n += 1

        nodes = []
        ans = 0
        thead = head
        i = 0
        while thead:
            if i < n // 2:
                nodes.append(thead.val)
            else:
                ans = max(ans, nodes.pop() + thead.val)
            thead = thead.next
            i += 1

        return ans
